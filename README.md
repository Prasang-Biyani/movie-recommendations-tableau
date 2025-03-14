# Movie Recommendation Insights Dashboard

An end-to-end Data Science project analyzing movie preferences and delivering recommendation insights using the MovieLens 1M dataset. Built with Python and Tableau Public, this interactive dashboard simulates a streaming platform’s analytics tool, featuring advanced visualizations and machine learning-driven recommendations.

## Project Overview

This project transforms raw MovieLens 1M data into a dynamic Tableau dashboard, showcasing:
- Top-rated movies by a custom Popularity Score.
- Genre popularity trends over time.
- Rating distribution across users.
- Ratings by genre and age group.
- ML-powered movie recommendations.

## Features

- **Data Preprocessing**: Merged `ratings`, `movies`, and `users` into `movielens_merged.csv` and expanded genres into `movielens_merged_expanded.csv` using Python (Pandas).
- **Visualizations** (Tableau Public):
  - **Bar Chart**: Top movies by Popularity Score (rating count × average rating).
  - **Line Chart**: Genre trends (rating count) over years, filtered to top 5 genres.
  - **Pie Chart**: Distribution of ratings (1-5).
  - **Heatmap**: Average ratings by genre and age.
  - **Table**: Top-5 movie recommendations per title.
- **Machine Learning**: Collaborative filtering with cosine similarity for recommendations.
- **Interactivity**: Filters for gender, age, genres, and movie selection.

## Tech Stack

- **Python**: Pandas, scikit-learn (cosine similarity).
- **Tableau Public**: Visualization and dashboarding.
- **Dataset**: MovieLens 1M (1M+ ratings, ~6K users, ~4K movies).

## Repository Contents

- `preprocess.py`: Merges and expands the MovieLens dataset.
- `recommendations.py`: Generates movie recommendations via collaborative filtering.
- `MovieLens_Dashboard.twbx`: Tableau workbook with visuals and dashboard.
- `Case_Study.pdf`: Detailed write-up of methodology and insights.

## Setup Instructions

1. **Download MovieLens 1M**: Get raw `.dat` files from [MovieLens](https://grouplens.org/datasets/movielens/1m/).
2. **Run Preprocessing**: Execute `preprocess.py` (requires Python, Pandas) to generate `movielens_merged.csv` and `movielens_merged_expanded.csv`.
3. **Generate Recommendations**: Run `recommendations.py` to create `recommendations.csv`.
4. **Open in Tableau**: Load the `.twbx` file in Tableau Public, or rebuild using the CSVs.

## Live Demo

Explore the interactive dashboard: [Insert Tableau Public URL here].

## Key Insights

- Top movies blend high ratings with broad appeal (e.g., “The Shawshank Redemption”).
- Action and Comedy dominate genre trends; Drama peaks cyclically.
- Younger users favor Action, older prefer Drama (heatmap).
- Recommendations align with genre/themes (e.g., “Star Wars” → “Empire Strikes Back”).

## Purpose

A portfolio project showcasing data preprocessing, advanced visualization, and ML integration for actionable insights.

## Contact

- **Email**: [Your Email]
- **LinkedIn**: [Your LinkedIn URL]
- **Portfolio**: [Optional Site URL]
