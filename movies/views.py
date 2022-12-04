from django.shortcuts import render
from django.views.generic import ListView
# from .utils import DataMixin
from .models import Category

def home(request):
    return render(request, 'movies/home.html')



def movies_category(request):
    return render(request, 'movies/home.html')



# class HomeView(DataMixin, ListView):
#     model = Category
#     # model = Post
#     template_name = 'home.html'


