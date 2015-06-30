from django.shortcuts import render
from .models import Movie, Rate, Score

def movie_list(request):
	movies = Movie.objects.order_by('-release_date')
	return render(request, 'movies/movie_list.html', {'movies': movies})
	
