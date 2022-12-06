from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import MoviesHome, CategoriesList, MoviesByCategories, MovieDetailView


urlpatterns = [
    path('', MoviesHome.as_view(), name='home'),
    path('categories', CategoriesList.as_view(), name='list_of_categories'),
    path('category/<slug:cat_slug>/', MoviesByCategories.as_view(), name='movies_by_category'),
    path('movies/<slug:movie_slug>', MovieDetailView.as_view(), name='detail_movie'),



]