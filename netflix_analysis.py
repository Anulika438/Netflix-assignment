# Netflix Data Analysis
# Data Preparation, Cleaning, Exploration, and Visualization

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# 1. Data Preparation
# Since the data is already provided, we'll load it directly
# In a real scenario, you would unzip the file first
netflix_data = pd.read_csv('paste.txt', sep='\t')

# Rename the dataset
netflix_shows_movies = netflix_data.copy()

# Display the first few rows to understand the data structure
print("Dataset Preview:")
print(netflix_shows_movies.head())

# 2. Data Cleaning
# Check for missing values
print("\nMissing values in each column:")
print(netflix_shows_movies.isnull().sum())

# Handle missing values - fill with appropriate placeholders based on column type
netflix_shows_movies['director'].fillna('Not Available', inplace=True)
netflix_shows_movies['cast'].fillna('Not Available', inplace=True)
netflix_shows_movies['country'].fillna('Unknown', inplace=True)
netflix_shows_movies['date_added'].fillna('Not Available', inplace=True)

# Verify missing values are handled
print("\nMissing values after cleaning:")
print(netflix_shows_movies.isnull().sum())

# 3. Data Exploration
# Dataset information
print("\nDataset Information:")
print(f"Total entries: {netflix_shows_movies.shape[0]}")
print(f"Total features: {netflix_shows_movies.shape[1]}")

# Statistical summary
print("\nStatistical Summary:")
print(netflix_shows_movies.describe())

# Content type distribution
print("\nContent Type Distribution:")
print(netflix_shows_movies['type'].value_counts())

# Year of release distribution
print("\nRelease Year Distribution:")
print(netflix_shows_movies['release_year'].value_counts().sort_index().head(10))

# Rating distribution
print("\nRating Distribution:")
print(netflix_shows_movies['rating'].value_counts())

# 4. Data Visualization

# Set the aesthetic style of the plots
sns.set_style('darkgrid')
plt.figure(figsize=(12, 10))

# 4.1 Most watched genres visualization
# Extract all genres from the 'listed_in' column
genres = []
for genre_list in netflix_shows_movies['listed_in']:
    for genre in genre_list.split(', '):
        genres.append(genre.strip())

# Count frequency of each genre
genre_counts = Counter(genres)

# Get top 10 genres
top_genres = dict(genre_counts.most_common(10))

# Plot
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
bars = plt.bar(top_genres.keys(), top_genres.values(), color=sns.color_palette('viridis', 10))
plt.title('Top 10 Most Common Genres on Netflix', fontsize=15)
plt.xlabel('Genre', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# 4.2 Ratings distribution visualization
plt.subplot(1, 2, 2)
rating_counts = netflix_shows_movies['rating'].value_counts()
plt.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%',
        colors=sns.color_palette('coolwarm', len(rating_counts)))
plt.title('Distribution of Content Ratings', fontsize=15)
plt.axis('equal')
plt.tight_layout()

plt.savefig('netflix_visualizations.png', dpi=300, bbox_inches='tight')
plt.show()

# Additional Visualizations

# Content type by release year
plt.figure(figsize=(14, 7))
yearly_counts = netflix_shows_movies.groupby(['release_year', 'type']).size().unstack()
yearly_counts.plot(kind='bar', stacked=True)
plt.title('Content Type by Release Year', fontsize=15)
plt.xlabel('Release Year', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Content Type')
plt.tight_layout()
plt.savefig('content_by_year.png', dpi=300, bbox_inches='tight')
plt.show()

# Duration analysis for movies
movies = netflix_shows_movies[netflix_shows_movies['type'] == 'Movie']
# Extract numeric duration
movies['duration_min'] = movies['duration'].str.extract('(\d+)').astype(float)

plt.figure(figsize=(10, 6))
sns.histplot(data=movies, x='duration_min', bins=20, kde=True)
plt.title('Movie Duration Distribution', fontsize=15)
plt.xlabel('Duration (minutes)', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.tight_layout()
plt.savefig('movie_duration.png', dpi=300, bbox_inches='tight')
plt.show()

# Export cleaned data for R integration
netflix_shows_movies.to_csv('netflix_shows_movies_cleaned.csv', index=False)

print("\nAnalysis completed. Visualizations saved and data exported for R integration.")