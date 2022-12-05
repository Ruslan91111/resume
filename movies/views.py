from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, Movies


class MoviesHome(ListView):
    model = Movies
    template_name = "movies/home.html"

    context_object_name = 'all_movies'

class CategoriesList(ListView):
    model = Category
    template_name = "movies/list_of_categories.html"

    context_object_name = 'all_categories'



