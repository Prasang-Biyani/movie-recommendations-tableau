import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Specify data types for columns
dtype_spec = {
    'UserID': int,
    'MovieID': int,
    'Rating': float,
    'Timestamp': str,
    'Gender': str,
    'Age': "int64",
    'Occupation': "int64",
    'Zip': "int64",
    "Title": str,
    "Genres": str
}

# Load data
merged = pd.read_csv('movies_data.csv')
merged["MovieID"] = merged["MovieID"].astype(int)
ratings_matrix = merged.pivot(index='UserID', columns='MovieID', values='Rating').fillna(0)

# Cosine similarity between movies
movie_similarity = cosine_similarity(ratings_matrix.T)
movie_ids = ratings_matrix.columns

# Function for top similar movies
def get_similar_movies(movie_id, top_n=5):
    idx = movie_ids.get_loc(movie_id)
    sim_scores = list(enumerate(movie_similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    return [movie_ids[i[0]] for i in sim_scores]

# Generate recommendations for all movies
recs = []
# Keeping it only 25 IDs 
for movie_id in movie_ids[:10]:  # Limit for demo; expand as needed
    similar = get_similar_movies(movie_id)
    for sim_movie in similar:
        recs.append([movie_id, sim_movie])
recs_df = pd.DataFrame(recs, columns=['MovieID', 'RecommendedMovieID'])
recs_df = pd.merge(recs_df, df[['MovieID', 'Title']], on='MovieID', how='left')
recs_df = pd.merge(recs_df, df[['MovieID', 'Title']], left_on='RecommendedMovieID', 
                   right_on='MovieID', suffixes=('_Original', '_Recommended'))
recs_df = recs_df[['MovieID_Original', 'RecommendedMovieID', 'Title_Original', 'Title_Recommended']]
recs_df.to_csv('recommendations.csv', index=False)