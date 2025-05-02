Netflix Data Analysis Project
This repository contains code for analyzing Netflix shows and movies data using both Python and R. The analysis includes data preparation, cleaning, exploration, and visualization.
Project Structure
netflix-data-analysis/
│
├── netflix_analysis.py       # Python script for data analysis and visualization
├── netflix_r_visualization.R # R script for visualization
├── paste.txt                 # Original Netflix dataset
├── netflix_shows_movies_cleaned.csv # Cleaned dataset (generated)
├── netflix_visualizations.png       # Python-generated visualizations
├── content_by_year.png              # Content type by year visualization
├── movie_duration.png               # Movie duration visualization
├── netflix_ratings_r.png            # R-generated ratings visualization
├── netflix_genres_r.png             # R-generated genres visualization
└── README.md                 # This documentation file
Requirements
Python

pandas
numpy
matplotlib
seaborn

Install these packages using pip:
pip install pandas numpy matplotlib seaborn
R

ggplot2
dplyr
tidyr
stringr

Install these packages in R:
rinstall.packages(c("ggplot2", "dplyr", "tidyr", "stringr"))
Running the Analysis
Python Analysis

Make sure the dataset paste.txt is in the same directory as the script.
Run the Python script:
python netflix_analysis.py

The script will generate visualization images and a cleaned CSV file.

R Visualization

Make sure the dataset paste.txt is in the same directory as the script.
Run the R script:
Rscript netflix_r_visualization.R

The script will generate visualization images in PNG format.

Analysis Overview
The analysis performs the following tasks:

Data Preparation:

Load the dataset
Rename the dataset to "Netflix_shows_movies"


Data Cleaning:

Identify and handle missing values
Fill missing values with appropriate placeholders


Data Exploration:

Display dataset information (size, shape)
Generate statistical summaries
Analyze content type distribution
Examine release year distribution
Study rating distribution


Data Visualization (Python):

Create visualization for most watched genres
Create visualization for ratings distribution
Generate additional visualizations for content type by year and movie duration


Data Visualization (R):

Recreate the ratings distribution visualization
Recreate the top genres visualization



Key Insights
The analysis provides insights into:

The distribution of content types (Movies vs. TV Shows)
The most popular genres on Netflix
The distribution of content ratings
Trends in content release over the years
Movie duration patterns

Notes on Implementation

The Python implementation uses Matplotlib and Seaborn for creating visualizations.
The R implementation uses ggplot2 for creating equivalent visualizations.
Both implementations handle missing values in a similar manner for consistency.
The dataset is relatively small, making it suitable for in-memory processing in both languages.

Future Improvements

Implement more advanced statistical analysis
Perform sentiment analysis on content descriptions
Create interactive visualizations using Plotly or Shiny
Expand the analysis to include recommendation algorithms
