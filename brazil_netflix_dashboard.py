import streamlit as st
import pandas as pd
import plotly.express as px

# Dashboard layout
st.set_page_config(layout='wide')
st.title("Exploring Brazilian Content on Netflix 🇧🇷")

# Load DataFrame
@st.cache_data
def load_data():
    df = pd.read_csv('brazil_split.csv')
    df = df.sort_values('release_year')
    df = df.drop(columns=['Unnamed: 0', 'country', 'cast', 'description', 'director'])
    return df

df = load_data()

# Define columns layout
col0, col1, col2 = st.columns([1, 1, 1])
col3, col4 = st.columns([1, 1])

# Filter by content type in col0
with col0:
    selected_types = st.multiselect('Select Content Types', df['type'].unique(), default=[df['type'].unique()[0]])

    # Filter the DataFrame based on the selected types
    @st.cache_data
    def filter_data(df, selected_types):
        return df[df['type'].isin(selected_types)]

    df_filtered = filter_data(df, selected_types)

    # Remove duplicate columns in 'title'
    df_filtered_unique = df_filtered.drop_duplicates(subset='title')
    df_filtered_unique = df_filtered_unique.drop(['type', 'listed_in'], axis=1)
    df_filtered_unique = df_filtered_unique.reset_index(drop=True)

    # Display filtered data with unique 'title' columns in the subheader
    st.write(df_filtered_unique)

    # Creating top_all
    top_all_content = ['Dramas', 'Comedies', 'Documentaries', 'TV Dramas', 'Crime TV Shows', 'Docuseries']
    top_all = df_filtered[df_filtered['listed_in'].isin(top_all_content)]

# Define a custom color scale for col1 based on the number of items
color_scale = px.colors.sequential.Reds[::-1]  # Reverse the color scale for stronger red with higher values
type_counts = df_filtered['listed_in'].value_counts().reset_index()
type_counts.columns = ['Type', 'Count']
color_max = type_counts['Count'].max()
color_scale = [color_scale[int(value / color_max * (len(color_scale) - 1))] for value in type_counts['Count']]

# Line chart with Plotly Express in col1
with col1:
    st.subheader("Content Production Over Time")
    type_year = df_filtered.groupby(['release_year', 'type']).size().reset_index(name='count')
    fig = px.line(type_year, x='release_year', y='count', labels={'release_year': 'Release Year', 'count': 'Count'},
                  color='type',  # Add color based on type (Movie or TV Show)
                  color_discrete_map={'Movie': 'firebrick', 'TV Show':'lightcoral'},
                  title='Brazilian Content Production Over Time'
                  )

    # Set the Y-axis to start from 0
    fig.update_yaxes(range=[0, type_year['count'].max()])

    # Remove dashes between lines (continuous lines)
    for trace in fig.data:
        trace.update(mode='lines+markers')

    st.plotly_chart(fig, use_container_width=True)

# Program Type Distribution in col2
with col2:
    st.subheader("Content Quantity by Category")
    type_counts = df_filtered['listed_in'].value_counts().reset_index()
    type_counts.columns = ['Type', 'Count']
    fig = px.bar(type_counts, x=type_counts['Count'], y=type_counts['Type'], labels={'x': 'Count', 'y': 'Type'},
                 color=type_counts['Count'], color_continuous_scale=color_scale)
    fig.update_layout(barmode='stack')  # Stack the bars horizontally
    fig.update_layout(legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1))  # Move the legend to the bottom
    st.plotly_chart(fig, use_container_width=True)

with col3:
    st.subheader("Top Categories Over the Years")
    listed_in_year = df_filtered.groupby(['release_year', 'listed_in']).size().reset_index(name='count')

    # Fill missing values with zero
    listed_in_year = listed_in_year.pivot(index='release_year', columns='listed_in', values='count').fillna(0).stack().reset_index()
    listed_in_year.rename(columns={0: 'count'}, inplace=True)

    # Get the available options
    available_categories = listed_in_year['listed_in'].unique()

    # Set the default value based on the top_all_content categories that exist in the options
    default_categories = [category for category in top_all_content if category in available_categories]

    # Create a callback to capture the selected categories
    selected_categories = st.multiselect("Select Categories", available_categories, default=default_categories)

    # Filter data based on the selected categories
    filtered_data = listed_in_year[listed_in_year['listed_in'].isin(selected_categories)]

    fig = px.line(filtered_data, x='release_year', y='count', color='listed_in',
                  labels={'release_year': 'Release Year', 'count': 'Count'},
                  category_orders={"release_year": sorted(filtered_data['release_year'].unique())})
    fig.update_yaxes(range=[0, filtered_data['count'].max()])  # Set the Y-axis to start from 0

    # Move the legend below the chart
    fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=0.9))

    st.plotly_chart(fig, use_container_width=True)  # Adjust the height of the chart to fit within the column

# Rating Distribution in col4 (Stacked Bars)
with col4:
    st.subheader("Rating Distribution")

    # Filter data based on the selected categories
    filtered_data = df_filtered[df_filtered['listed_in'].isin(selected_categories)]

    # Create a stacked bar chart for rating distribution
    fig = px.histogram(filtered_data, x='rating', color='listed_in',
                       labels={'x': 'Rating', 'y': 'Count'},
                       category_orders={"rating": ["G", "TV-G", "PG", "TV-Y", "TV-Y7", "TV-Y7-FV", "PG-13", "TV-14", "R", "TV-MA", "NR"]},
                       color_discrete_sequence=px.colors.qualitative.Set1)
    fig.update_layout(barmode='stack')

    st.plotly_chart(fig, use_container_width=True)
