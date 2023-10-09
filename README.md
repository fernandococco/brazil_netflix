# Analyzing Brazilian Content on Netflix

## Summary

The primary objective of this project is to conduct a comprehensive analysis of Brazilian content within the Netflix platform. We will be utilizing the Kaggle-curated dataset, "netflix_titles.csv," which encompasses a comprehensive listing of all movies and TV shows accessible on Netflix up to the year 2021.

Additionally, a new dataset, "brazil_split.csv," has been added to the project. This dataset is generated after all data processing and manipulation of the "netflix_titles.csv" dataset. It includes data specifically related to Brazilian content on Netflix.

## Dashboard

To visualize the insights and analysis of Brazilian content on Netflix, a dashboard has been created using the Streamlit framework, Plotly Express, and Pandas. The dashboard script can be found in the "brazil_netflix_dashboard.py" file. The dashboard provides interactive visualizations and allows users to explore various aspects of Brazilian content on Netflix.

To run the dashboard, make sure to install the required dependencies listed in the "requirements.txt" file. You can access the live dashboard at [Brazil Netflix Dashboard](https://brazil-netflix-dash.streamlit.app).

## Dataset Columns

1. **Type**: Categorizes the content into two primary types: "Movies" and "TV Shows." It distinguishes between films and television series, providing information on the format of the content.

2. **Country**: Specifies the country or countries associated with the production of the content. For Brazilian content analysis, this column will help identify titles produced in Brazil.

3. **Listed_In**: Contains information about the genres or categories to which the content belongs. Entries in this column are typically in list format, and they represent the various genres, themes, or categories that describe the content. It provides insights into the diversity of genres within the Netflix library.

4. **Rating**: Indicates the content's classification or rating based on age-appropriateness and content maturity. Common ratings include "TV-MA" (Mature Audience), "TV-14" (Teens 14 and older), "R" (Restricted), "PG-13" (Parents Strongly Cautioned), and others. It helps viewers understand the suitability of the content for different age groups.

5. **Release_Year**: Records the year in which the content was released. It provides a temporal dimension to the dataset, enabling analyses related to the growth and evolution of content over time.

Each of these columns plays a crucial role in characterizing and analyzing the content available on Netflix. For the analysis of Brazilian content, focusing on the "Country" column with values related to Brazil and the "Type" column to distinguish between movies and TV shows is particularly relevant. Additionally, the "Listed_In," "Rating," and "Release_Year" columns provide valuable context for understanding content genres, audience suitability, and temporal trends.

## Research Questions (RQ)

The research questions (RQ) that emerged through the dataset are as follows:

1. What type of content has Brazil produced the most or been involved in producing for Netflix?

2. What is the progression of Brazilian content production over time?

3. What kind of movies has Brazil produced the most?

4. What is the progression of Brazilian movie production over time?

5. What kind of TV shows has Brazil produced the most?

6. What is the progression of Brazilian TV show production over time?

7. Which age rating (content rating) has Brazil focused on the most?

8. Is there a relationship between the release year and content rating?

9. Is there a relationship between the release year and the duration of a movie?

10. Do Brazilian TV shows tend to get renewed?

## Instructions

1. Choose the dataset. I used the Netflix Movies and TV Shows dataset, provided as "netflix_titles.csv."

2. Get organized to make the analysis: Have one folder with the Jupyter notebook and the "netflix_titles.csv" file.

3. Analyze the data: An exploratory analysis was performed to answer the RQ.

4. Share the findings: All insights extracted from the data are documented within the Jupyter notebook.

## Tools

In order to complete this project, the following libraries and tools were used: pandas, numpy, Matplotlib, csv, Streamlit and Plotly Express

