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

- **Data Preprocessing**: Merged `ratings`, `movies`, and `users` into `movies_data.csv` and expanded genres into `movielens_merged_expanded.csv` using Python (Pandas).
- **Visualizations** (Tableau Public):
  - **Bar Chart**: Top movies by Popularity Score (rating count x average rating).
  - **Line Chart**: Genre trends (rating count) over years, filtered to top 5 genres.
  - **Pie Chart**: Distribution of ratings (1-5).
  - **Heatmap**: Average ratings by genre and age.
  - **Table**: Top-5 movie recommendations per title.
- **Machine Learning**: Collaborative filtering with cosine similarity for recommendations.
- **Interactivity**: Filters for gender, age, genres, and movie selection.

## Tech Stack 

- ![Python](https://img.shields.io/badge/-Python-blue?style=flat&logo=python&logoColor=white) **Python**: Pandas, scikit-learn (cosine similarity).
- ![Tableau](https://img.shields.io/badge/-Tableau-E97627?style=flat&logo=tableau&logoColor=white) **Tableau Public**: Visualization and dashboarding.
- ![Dataset](https://img.shields.io/badge/-Dataset-FF6F00?style=flat&logo=database&logoColor=white) **Dataset**: MovieLens 1M (1M+ ratings, ~6K users, ~4K movies).

## Repository Contents

- `preprocess.py`: Merges and expands the MovieLens dataset.
- `recommendations.py`: Generates movie recommendations via collaborative filtering.
- `MovieLens_Dashboard.twbx`: Tableau workbook with visuals and dashboard.
- `Case_Study.pdf`: Detailed write-up of methodology and insights.

## Setup Instructions

1. **Download MovieLens 1M**: Get raw `.dat` files from [MovieLens](https://grouplens.org/datasets/movielens/1m/).
2. **Run Preprocessing**: Execute `preprocess.py` (requires Python, Pandas) to generate `movies_data.csv` and `movielens_merged_expanded.csv`.
3. **Generate Recommendations**: Run `recommendations.py` to create `recommendations.csv`.
4. **Open in Tableau**: Load the `.twbx` file in Tableau Public, or rebuild using the CSVs.

## Live Demo

Explore the interactive dashboard: [![Tableau](https://img.icons8.com/?size=50&id=9Kvi1p1F0tUo&format=png&color=000000)](https://public.tableau.com/app/profile/prasang.biyani/viz/movies_recommendation/Dashboard1?publish=yes).

## Key Insights

- Top movies blend high ratings with broad appeal (e.g., “The Shawshank Redemption”).
- Action and Comedy dominate genre trends; Drama peaks cyclically.
- Younger users favor Action, older prefer Drama (heatmap).
- Recommendations align with genre/themes (e.g., “Star Wars” → “Empire Strikes Back”).

## Purpose

A portfolio project showcasing data preprocessing, advanced visualization, and ML integration for actionable insights.

## Contact

## Contact

- **Email**: [![Gmail](https://img.shields.io/badge/-Gmail-red?style=flat&logo=gmail&logoColor=white)](mailto:biyaniprasang@gmail.com)
- **LinkedIn**: [![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/prasangbiyani/)
- **Portfolio**: [![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@biyaniprasang)
