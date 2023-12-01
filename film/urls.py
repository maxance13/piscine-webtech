from django.urls import path
from .views import blog_detail, film_detail, film_accueil

urlpatterns = [
    path('', film_accueil, name='film_accueil'),
    path('blog/<int:pk>/', blog_detail, name='blog_detail'),
    path('film/<int:film_id>/', film_detail, name='film_detail'),
]
