from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DetailView, UpdateView
from .forms import SignUpForm, PasswordChangingForm, CommentForm
from .models import Category, Movies, Comment, Profile
from django.contrib.auth.views import PasswordChangeView


# отображение домашней страницы
class MoviesHome(ListView):
    model = Movies
    template_name = "movies/home.html"
    context_object_name = 'all_movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies_list'] = Movies.objects.all().order_by('title')
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Movies.objects.filter(is_published=True)


# отображение списка категорий
class CategoriesList(ListView):
    model = Category
    template_name = "movies/list_of_categories.html"
    context_object_name = 'all_categories'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories_list'] = Category.objects.all().order_by('title_cat')
        return context


# отображение фильмов определнной категории
class MoviesByCategories(ListView):
    model = Movies
    template_name = "movies/movies_by_category.html"
    context_object_name = 'movies_by_category'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['movies_by_category'][0].cat)
        context['cat_selected'] = context['movies_by_category'][0].cat_id
        return context

    def get_queryset(self):
        return Movies.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


# класс  представления одного фильма
class MovieDetailView(DetailView):
    model = Movies
    template_name = 'movies/detail_movie.html'
    slug_url_kwarg = 'movie_slug'
    context_object_name = 'detail_movie'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# добавление комментария
class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'movies/add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('home')


# регистрация пользователей
class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


# Редактирование страницы профиля
class EditProfilePageView(UpdateView):
    model = Profile
    # form_class = EditProfileForm
    template_name = 'registration/edit_profile_page.html'
    fields = ['profile_pic', 'first_name', 'last_name', 'bio']
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        users = Profile.objects.all()
        context = super(EditProfilePageView, self).get_context_data(**kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


# Изменение пароля юзера
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')


# Показать страницу профиля
class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context['page_user'] = page_user
        return context



