from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Movies


# отображение домашней страницы
class MoviesHome(ListView):
    model = Movies
    template_name = "movies/home.html"
    context_object_name = 'all_movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies_list'] = Movies.objects.all().order_by('title')
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Movies.objects.filter(is_published=True)


# отображение списка категорий
class CategoriesList(ListView):
    model = Category
    template_name = "movies/list_of_categories.html"
    context_object_name = 'all_categories'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories_list'] = Category.objects.all().order_by('title_cat')
        return context


# отображение фильмов определнной категории
class MoviesByCategories(ListView):
    model = Movies
    template_name = "movies/movies_by_category.html"
    context_object_name = 'movies_by_category'
    allow_empty = False


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['movies_by_category'][0].cat)
        context['cat_selected'] = context['movies_by_category'][0].cat_id
        return context


    def get_queryset(self):
        return Movies.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True )


# класс  пердставления одного фильма
class MovieDetailView(DetailView):
    model = Movies
    template_name = 'movies/detail_movie.html'
    slug_url_kwarg = 'movie_slug'
    context_object_name = 'detail_movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        def get_queryset(self):
            return Movies.objects.filter(Movie__slug=self.kwargs['movie_slug'], is_published=True)


