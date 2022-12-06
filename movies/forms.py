from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Review


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class PostReview(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
                }






        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
        #     'author': forms.TextInput(attrs={'class': 'form-control',
        #                                      'value': '', 'id':'пользователь', 'type': 'hidden'}),
        #     'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
        #     'body': forms.Textarea(attrs={'class': 'form-control'}),
        #     'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        #
        # }