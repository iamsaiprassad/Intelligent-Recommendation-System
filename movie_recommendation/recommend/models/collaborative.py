import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import cross_validate
import os

# Load data function
def load_ratings():
    file_path = os.path.join('recommend/data/ratings.dat')
    ratings = pd.read_csv(file_path, sep='::', header=None, engine='python',
                          names=['user_id', 'movie_id', 'rating', 'timestamp'])
    return ratings

# Train collaborative filtering model using SVD
def train_collaborative_model():
    ratings = load_ratings()
    reader = Reader(line_format='user item rating timestamp', sep='::')
    data = Dataset.load_from_df(ratings[['user_id', 'movie_id', 'rating']], reader)
    
    # Using SVD (Singular Value Decomposition)
    model = SVD()
    cross_validate(model, data, cv=5, verbose=True)
    
    trainset = data.build_full_trainset()
    model.fit(trainset)
    return model

# Function to recommend movies based on user ID
def recommend_movies_collaborative(user_id, model, num_recommendations=5):
    ratings = load_ratings()
    unique_movies = ratings['movie_id'].unique()
    watched_movies = ratings[ratings['user_id'] == user_id]['movie_id'].tolist()
    
    recommendations = []
    for movie_id in unique_movies:
        if movie_id not in watched_movies:
            est_rating = model.predict(user_id, movie_id).est
            recommendations.append((movie_id, est_rating))
    
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations[:num_recommendations]
