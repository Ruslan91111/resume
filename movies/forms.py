from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import Comment


# ДОБАВЛЕНИЕ КОММЕНТАРИЯ
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }



# РЕГИСТРАЦИЯ ПОЛЬЗОВАТЕЛЯ
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Имя пользователя')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторный ввод пароля', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


# РЕДАКТИРОВАНИЕ СТРАНИЦЫ ПОЛЬЗОВАТЕЛЯ
# class EditProfileForm(UserChangeForm):
#     pic_profile = forms.ImageField(widget=forms.FileInput, label='Фото профиля')
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
#     first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Имя')
#     last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Фамилия')
#     username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Имя пользователя')
#
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name',
#                 'email', 'password', 'last_login')


# ИЗМЕНЕНИЕ ПАРОЛЯ
class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}), label='Старый пароль')
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}), label='Новый пароль')
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}), label='Подтверждение нового пароля')

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

