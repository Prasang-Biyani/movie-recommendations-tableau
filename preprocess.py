import pandas as pd
import numpy as np

# movies - 
movies = pd.read_fwf('movies.dat', header=None, encoding='ISO-8859-1')
movies.columns = ["MovieID", "Title", "Genres"]
movies[["MovieID", "Title", "Genres"]] = movies["MovieID"].str.split("::", expand=True)

# ratings - 
ratings = pd.read_fwf('ratings.dat', header=None, encoding='ISO-8859-1')
ratings = ratings[0].str.split("::", expand=True)
ratings.columns = ["UserID", "MovieID", "Rating", "Timestamp"]
ratings['Timestamp'] = pd.to_numeric(ratings['Timestamp'])

# users - 
users = pd.read_fwf('users.dat', header=None, encoding='ISO-8859-1')
users = users[0].str.split("::", expand=True)
users.columns = ["UserID", "Gender", "Age", "Occupation", "Zip"]
users['Gender'] = users['Gender'].replace({"Fantasy": "F"})

df = ratings.merge(users, on=["UserID"]).merge(movies, on=["MovieID"])
df = df[~df['Zip'].isin(["20744-", "55337-", "48103-"])]

# Convert Timestamp to datetime
df['Timestamp'] = pd.to_datetime(ratings['Timestamp'], unit='s')
# Remove duplicates
df = df.drop_duplicates()

# Converting MovieID type to "int"
df['MovieID'] = df['MovieID'].astype(int)
df.to_csv("movies_data.csv", index=False)



# Split the 'Genres' column by '|' and explode the list into separate rows
df_expanded = df.assign(Genres=df['Genres'].str.split('|')).explode('Genres')

# Define a dictionary to replace incorrect or abbreviated genre names with correct ones
replace_map = {
    "Children's": "Children", "Sci-F": "Sci-Fi", 
    "Advent": "Adventure", "Th": "Thriller", "Thri": "Thriller",
    "Roman": "Romance", "Rom": "Romance", "Roma": "Romance", "Children'": "Children",
    "Horro": "Horror", "Sci-":"Sci-Fi", "S": "Sci-Fi", "Wa": "War", "Chil": "Children",
    "Adventu": "Adventure", "Doc": "Documentary", "F": "Fantasy", "Acti": "Action",
    "Childre": "Children", "Documenta": "Documentary", "Come": "Comedy", "Crim": "Crime",
    "Docu": "Documentary", "Dram": "Drama", "Fant": "Fantasy", "Chil": "Children", "We" : "War",
    "Chil": "Children", "Chi": "Children", "Fantas": "Fantasy", "D": "Drama", "Dra": "Drama", "Animati": "Animation",
    "Adv": "Adventure", "A": "Adenture", "Sci": "Sci-Fi", "Com": "Comedy", "Thrille": "Thriller",
    "Adventur": "Adventure", "Horr": "Horror", "Childr": "Children", "Comed": "Comedy", "Ro":"Romance",
    "Documen": "Documentary", "Documen": "Documentary", "R": "Romance", "Music" : "Musical",
    "Document": "Documentary"
}

# Replace incorrect or abbreviated genre names with correct ones using the replace_map
df_expanded = df_expanded.replace(replace_map)

# Remove rows with specific unwanted genre values
df_expanded = df_expanded[~df_expanded.isin(["Film-Noir", "Dr", '', None, "Wester"])]

# Drop any rows with NaN values
df_expanded = df_expanded.dropna()

# Strip any leading or trailing whitespace from the 'Genres' column
df_expanded['Genres'] = df_expanded['Genres'].str.strip()

# Replace incorrect 'Gender' values with correct ones
df_expanded['Gender'] = df_expanded['Gender'].replace({"Fantasy": "F"})

# Save the cleaned and expanded DataFrame to a CSV file
df_expanded.to_csv('movielens_merged_expanded.csv', index=False)

