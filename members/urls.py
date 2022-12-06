from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import RegisterUser


urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register_user'),
    path('login/', RegisterUser.as_view(), name='login'),

]