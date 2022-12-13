from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DetailView, UpdateView
from rest_framework.viewsets import ModelViewSet

from .forms import SignUpForm, PasswordChangingForm, CommentForm, EditProfileForm, ProfilePageForm
from .models import Category, Movies, Comment, Profile
from django.contrib.auth.views import PasswordChangeView

from .serializers import MoviesSerializer


class MoviesViewSet(ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer



class AddCommentView(CreateView):  # добавить комментарий
    model = Comment
    form_class = CommentForm
    template_name = 'movies/add_comment.html'

    def form_valid(self, form):
        form.instance.movies_id = self.kwargs['pk']
        form.instance.author = self.request.user       # передача автора комментария
        return super().form_valid(form)

    def get_success_url(self):
        # перевод queryset в словарь из одной пары ключ - значение: 'slug':''
        list_out_of_queryset = dict(current_page=Movies.objects.filter(pk=self.kwargs['pk']).values('slug'))
        needed_slug = list_out_of_queryset['current_page'][0]['slug']      # вытягиваем нужный slug

        return reverse_lazy('detail_movie', kwargs={'movie_slug': needed_slug})


class CreateProfilePageView(CreateView):  # создать страницу профиля
    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/create_user_profile_page.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ShowProfilePageView(DetailView):  # Показать страницу профиля
    model = Profile
    template_name = 'registration/user_profile_page.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user

        return context


class MoviesHome(ListView):  # отображение домашней страницы
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


class CategoriesList(ListView):  # отображение списка категорий
    model = Category
    template_name = "movies/list_of_categories.html"
    context_object_name = 'all_categories'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories_list'] = Category.objects.all().order_by('title_cat')
        return context


class MoviesByCategories(ListView):  # отображение фильмов определнной категории
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


class MovieDetailView(DetailView):  # класс представления одного фильма
    model = Movies
    template_name = 'movies/detail_movie.html'
    slug_url_kwarg = 'movie_slug'
    context_object_name = 'detail_movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserRegisterView(CreateView):  # регистрация пользователей
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(UpdateView):  # отредактировать страницу юзера - пользователя
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user



class EditProfilePageView(UpdateView):  # Редактирование страницы профиля
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


class PasswordsChangeView(PasswordChangeView):          # Изменение пароля юзера
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')


def password_success(request):                     # сообщение о том, что пароль успешно изменен
    return render(request, 'registration/password_success.html', {})






