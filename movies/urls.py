from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import home, movies_category

urlpatterns = [
    path('', home, name='home'),
    path('category/<slug:cat_slug>/', movies_category, name='category'),


]