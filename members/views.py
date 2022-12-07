from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView

# регистрация пользователей
class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


# Редактирование страницы профиля
class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


# Изменение пароля юзера
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')