# Install required packages if not already installed
if (!require("ggplot2")) install.packages("ggplot2")
if (!require("dplyr")) install.packages("dplyr")
if (!require("tidyr")) install.packages("tidyr")
if (!require("stringr")) install.packages("stringr")

# Load required libraries
library(ggplot2)
library(dplyr)
library(tidyr)
library(stringr)

# Read the data
netflix_data <- read.delim("paste.txt", sep = "\t", stringsAsFactors = FALSE)

# Rename the dataset
netflix_shows_movies <- netflix_data

# Data Cleaning
# Handle missing values
netflix_shows_movies$director[is.na(netflix_shows_movies$director)] <- "Not Available"
netflix_shows_movies$cast[is.na(netflix_shows_movies$cast)] <- "Not Available"
netflix_shows_movies$country[is.na(netflix_shows_movies$country)] <- "Unknown"
netflix_shows_movies$date_added[is.na(netflix_shows_movies$date_added)] <- "Not Available"

# Check data structure
str(netflix_shows_movies)

# Visualization 1: Rating Distribution
# Count the frequency of each rating
rating_counts <- netflix_shows_movies %>%
  group_by(rating) %>%
  summarise(count = n()) %>%
  arrange(desc(count))

# Create a bar plot of ratings
ggplot(rating_counts, aes(x = reorder(rating, -count), y = count, fill = rating)) +
  geom_bar(stat = "identity") +
  theme_minimal() +
  labs(
    title = "Distribution of Content Ratings on Netflix",
    x = "Rating",
    y = "Count"
  ) +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1),
    plot.title = element_text(hjust = 0.5, size = 16),
    legend.position = "none"
  )

# Save the plot
ggsave("netflix_ratings_r.png", width = 10, height = 6, dpi = 300)

# Visualization 2: Genre Analysis
# Function to extract and process genres
extract_genres <- function(genres_column) {
  genres_list <- strsplit(genres_column, ", ")
  return(unlist(genres_list))
}

# Extract all genres
all_genres <- unlist(lapply(netflix_shows_movies$listed_in, extract_genres))
all_genres <- trimws(all_genres)

# Count genre frequencies
genre_counts <- as.data.frame(table(all_genres))
colnames(genre_counts) <- c("genre", "count")

# Get top 10 genres
top_genres <- genre_counts %>%
  arrange(desc(count)) %>%
  head(10)

# Create a bar plot of top genres
ggplot(top_genres, aes(x = reorder(genre, count), y = count, fill = genre)) +
  geom_bar(stat = "identity") +
  coord_flip() +
  theme_minimal() +
  labs(
    title = "Top 10 Most Common Genres on Netflix",
    x = "Genre",
    y = "Count"
  ) +
  theme(
    plot.title = element_text(hjust = 0.5, size = 16),
    legend.position = "none"
  )

# Save the plot
ggsave("netflix_genres_r.png", width = 10, height = 6, dpi = 300)

# Print completion message
cat("R visualization completed. Plots saved as 'netflix_ratings_r.png' and 'netflix_genres_r.png'.")