import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load movies data
def load_movies():
    file_path = 'recommend/data/movies.dat'
    movies = pd.read_csv(file_path, sep='::', header=None, engine='python',
                         names=['movie_id', 'title', 'genres'],encoding='latin1')
    return movies

# Train content-based recommendation model
def train_content_model():
    movies = load_movies()
    
    # TF-IDF Vectorization on genres
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies['genres'])
    
    # Compute cosine similarity between movies
    similarity_matrix = cosine_similarity(tfidf_matrix)
    return movies, similarity_matrix

# Function to recommend movies based on movie ID
def recommend_movies_content(movie_id, movies, similarity_matrix, num_recommendations=5):
    movie_index = movies[movies['movie_id'] == movie_id].index[0]
    similarity_scores = list(enumerate(similarity_matrix[movie_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    
    recommended_movie_indices = [i[0] for i in similarity_scores[1:num_recommendations+1]]
    return movies.iloc[recommended_movie_indices]
