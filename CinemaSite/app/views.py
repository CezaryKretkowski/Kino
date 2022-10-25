from itertools import product
from django.shortcuts import render
from .Models.Movie import Movie


def home(request):
    movies = Movie.objects.all()
    return render(request, 'Home.html', {'movies': movies})
