from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MoviesSerializer, UserMoviesRelationsSerializer
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .forms import SignUpForm, PasswordChangingForm, CommentForm, EditProfileForm, ProfilePageForm, RatingForm
from .models import Category, Movies, Comment, Profile, Rating
from django.contrib.auth.views import PasswordChangeView


class AddStarRating(View):
    """
    Добавление рейтинга к фильму
    """
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            print(x_forwarded_for)
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                movie_id=int(request.POST.get("movie")),
                defaults={'star_id': int(request.POST.get('star'))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)










class AddCommentView(CreateView):
    """
    Добавить комментарий
    """
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


class CreateProfilePageView(CreateView):
    """
    Создать страницу профиля
    """
    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/create_user_profile_page.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ShowProfilePageView(DetailView):
    """
    Показать страницу профиля.
    """
    model = Profile
    template_name = 'registration/user_profile_page.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user

        return context


class MoviesHome(ListView):
    """
    Отобразить домашнюю страницу
    """
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


class CategoriesList(ListView):
    """Отображение списка категорий"""
    model = Category
    template_name = "movies/list_of_categories.html"
    context_object_name = 'all_categories'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories_list'] = Category.objects.all().order_by('title_cat')
        return context


class MoviesByCategories(ListView):
    """
    Отображение списка фильмов определенной категории.
    """
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


class MovieDetailView(DetailView):
    """
    Представление одного фильма.
    """
    model = Movies
    template_name = 'movies/detail_movie.html'
    slug_url_kwarg = 'movie_slug'
    context_object_name = 'detail_movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["star_form"] = RatingForm()
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




# class UserMoviesRelationsView(UpdateModelMixin, GenericViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = UserMovieRelations.objects.all()
#     serializer_class = UserMoviesRelationsSerializer
#     lookup_field = 'movie'


