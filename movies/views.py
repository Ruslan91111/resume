from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Movies


class MoviesHome(ListView):
    model = Movies
    template_name = "movies/home.html"
    context_object_name = 'all_movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies_list'] = Movies.objects.all().order_by('title')
        return context


class CategoriesList(ListView):
    model = Category
    template_name = "movies/list_of_categories.html"
    context_object_name = 'all_categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories_list'] = Category.objects.all().order_by('title_cat')
        return context


class MovieDetailView(DetailView):
    model = Movies

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

