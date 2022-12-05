from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import MoviesHome, CategoriesList


urlpatterns = [
    path('', MoviesHome.as_view()),
    path('categories', CategoriesList.as_view())




]