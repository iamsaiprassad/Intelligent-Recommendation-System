from . import views
from .views import hybrid_recommendations , index  # Import your views here
from django.urls import path

urlpatterns = [ 
    path('', views.index, name='index'),  # Render the index.html when visiting the root
    path('hybrid/',hybrid_recommendations, name='hybrid_recommendations'),
]


