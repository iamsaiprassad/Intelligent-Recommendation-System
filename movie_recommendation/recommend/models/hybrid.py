from .collaborative import train_collaborative_model, recommend_movies_collaborative
from .content_based import train_content_model, recommend_movies_content

# Hybrid recommendation function
def recommend_hybrid(user_id, movie_id, num_recommendations=5):
    # Train models
    collab_model = train_collaborative_model()
    movies, content_similarity = train_content_model()
    
    # Get collaborative recommendations
    collab_recs = recommend_movies_collaborative(user_id, collab_model, num_recommendations)
    collab_movie_ids = [movie[0] for movie in collab_recs]
    
    # Get content-based recommendations
    content_recs = recommend_movies_content(movie_id, movies, content_similarity, num_recommendations)
    content_movie_ids = content_recs['movie_id'].tolist()
    
    # Combine recommendations
    final_recommendations = list(set(collab_movie_ids + content_movie_ids))
    
    # Return top recommendations
    return movies[movies['movie_id'].isin(final_recommendations)]

# def recommend_hybrid_with_explanation(user_id, movie_id, num_recommendations=5):
#     recommendations = recommend_hybrid(user_id, movie_id, num_recommendations)
    
#     # Example explanation generation
#     recommendations['reason'] = recommendations.apply(lambda row: f"Recommended because you watched movies in genre {row['genre']}", axis=1)
    
#     return recommendations[['movie_id', 'title', 'reason']]

