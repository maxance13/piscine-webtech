import requests
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from .models import BlogPost, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

def film_accueil(request):
    query = request.GET.get('query')
    if query:
        print("Recherche effectuée:", query)
        movies = search_movies(query)
        context = {'movies': movies, 'query': query}
    else:
        popular_movies = get_popular_movies()
        grouped_movies = [popular_movies[i:i + 3] for i in range(0, len(popular_movies), 3)]
        latest_blog_posts = BlogPost.objects.all().order_by('-published_date')[:3]
        context = {
            'grouped_movies': grouped_movies,
            'latest_blog_posts': latest_blog_posts,
        }
    return render(request, 'film_accueil.html', context)


def get_popular_movies():
    api_key = settings.TMDB_API_KEY
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=fr-FR"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['results']
    else:
        return []

def search_movies(query):
    api_key = settings.TMDB_API_KEY
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=fr-FR&query={query}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Réponse de l'API TMDB:", response.json())
        return response.json().get('results', [])
    else:
        print("Erreur avec l'API TMDB:", response.status_code)
        return []

@login_required
def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user  
            comment.post = post
            comment.save()
            return redirect('blog_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'blog_detail.html', {'post': post, 'form': form})

def film_detail(request, film_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{film_id}?api_key={settings.TMDB_API_KEY}&language=fr-FR")
    movie = response.json()
    return render(request, 'film_detail.html', {'movie': movie})

@login_required
def approve_comments(self, request, queryset):
    queryset.update(approved_comment=True)
approve_comments.short_description = "Approve selected comments"

