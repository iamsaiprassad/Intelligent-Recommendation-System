import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse.linalg import svds


MOVIE_DATA_PATH = 'recommend/data/movies.dat'
RATINGS_DATA_PATH = 'recommend/data/ratings.dat'
USERS_DATA_PATH = 'recommend/data/users.dat'

# Load MovieLens 1M data
def load_data():
    # Load ratings
    ratings = pd.read_csv(RATINGS_DATA_PATH, sep='::', engine='python', names=['user_id', 'movie_id', 'rating', 'timestamp'])

    # Load movies
    movies = pd.read_csv(MOVIE_DATA_PATH, sep='::', engine='python', names=['movie_id', 'title', 'genres'],encoding='latin1')

    users = pd.read_csv(USERS_DATA_PATH, sep='::', header=None, engine='python', 
                        names=['user_id', 'gender', 'age', 'occupation', 'zip_code'])

    return movies , ratings , users
def preprocess_data():
    movies, ratings, users = load_data()

    # Merge datasets
    df = ratings.merge(movies, on='movie_id').merge(users, on='user_id')

    # Drop unnecessary columns
    df.drop(columns=['timestamp', 'zip_code'], inplace=True)
    
    return df