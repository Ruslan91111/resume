from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import UserRegisterView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register_user'),

]