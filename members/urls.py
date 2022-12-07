from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import UserRegisterView, UserEditView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register_user'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),

]