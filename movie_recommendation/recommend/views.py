
from django.http import JsonResponse
from .models.hybrid import recommend_hybrid
from django.shortcuts import render

def hybrid_recommendations(request):
    try:
        user_id = int(request.GET.get('user_id', None))
        movie_id = int(request.GET.get('movie_id', None))
        recommendations = recommend_hybrid(user_id, movie_id, num_recommendations=5)
        
        # Ensure column names are correct for JSON serialization
        response_data = recommendations[['movie_id', 'title']].to_dict(orient='records')
        return JsonResponse({'recommendations': response_data})

        

        # recommendations = recommend_hybrid_with_explanation(user_id, movie_id, num_recommendations=5)
        # response_data = recommendations[['movie_id', 'title', 'reason']].to_dict(orient='records')
        # return JsonResponse({'recommendations': response_data})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
        
def index(request):
    return render(request, 'index.html')


