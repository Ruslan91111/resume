from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from django.contrib.auth.views import PasswordChangeView


from .views import UserRegisterView, UserEditView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register_user'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordChangeView.as_view(template_name='registration/change-password.html')),

]