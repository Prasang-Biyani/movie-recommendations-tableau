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

Explore the interactive dashboard: 
<a href="https://public.tableau.com/app/profile/prasang.biyani/viz/movies_recommendation/Dashboard1?publish=yes">
  <svg xmlns="http://www.w3.org/2000/svg" class="ionicon" viewBox="0 0 512 512" width="24" height="24">
    <path d="M242.69 340.3h26.62v-72.6h67v-25.82h-67v-72.6h-26.62v72.6h-66.15v25.82h66.15zM119.26 445.18h22.59v-64.54h59.7v-20.17h-59.7v-65.34h-22.59v65.34h-59.7v20.17h59.7zM370.15 212h22.59v-64.5h60.5v-19.37h-60.5V62.79h-22.59v65.34h-59.7v19.37h59.7zM246.72 496h19.36v-46h41.15v-16.92h-41.15v-46h-19.36v46h-40.33V450h40.33zM120.07 212h21v-65.31h60.51v-18.56H141V62.79h-21v65.34H59.56v18.56h60.51zM435.72 308.84h19.36v-45.18H496v-17.74h-40.92v-45.18h-19.36v45.18h-40.33v17.74h40.33z"/>
    <path fill-rule="evenodd" d="M370.15 445.18h22.59v-64.54h60.5v-20.17h-60.5v-65.34h-22.59v65.34h-59.7v20.17h59.7z"/>
    <path d="M307 74.08V60.37h-40.34V16h-14.52v44.37h-40.33v13.71h40.33v44.37h14.52V74.08zM56.11 305.61h14.52v-44.37H111v-13.71H70.63V204H56.11v43.56H16v14.52l40.11-.08z"/>
  </svg>
</a>

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
