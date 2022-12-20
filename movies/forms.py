from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import Comment, Profile, RatingStar, Rating


class ProfilePageForm(forms.ModelForm):
    """
    Создание страницы профиля.
    """
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'first_name', 'last_name')
        widgets = {

                'bio': forms.Textarea(attrs={'class': 'form-control'}),
                # 'profile_pic': forms.ImageField(allow_empty_file=True),
                'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    """
    Создание комментария.
    """
    class Meta:
        model = Comment
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class SignUpForm(UserCreationForm):
    """
    Форма регистрации пользователя на сайте.
    """
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Имя пользователя')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # убрал first_name и last_name, чтобы не требовало при регистрации
    # first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Имя')
    # last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Фамилия')
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


class EditProfileForm(UserChangeForm):
    """
    Форма редактирования страницы пользователя.
    """
    pic_profile = forms.ImageField(widget=forms.FileInput, required=False, label='Фото профиля')
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Имя')
    last_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Фамилия')
    bio = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}), label='О себе')
    # username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Имя пользователя')
    # last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}),  label='Последнее раз был')
    # is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}), label='Является ли суперпользователем')
    # is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}), label='Персонал сайта')
    # is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}), label='На сайте?')
    # date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Дата регистрации')

    class Meta:
        model = User
        fields = ('pic_profile', 'username', 'first_name', 'last_name', 'password')


class PasswordChangingForm(PasswordChangeForm):
    """
    Форма изменения пароля.
    """
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}), label='Старый пароль')
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}), label='Новый пароль')
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}), label='Подтверждение нового пароля')

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class RatingForm(forms.ModelForm):
    """
    Форма добавления рейтинга.
    """
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ('star',)





