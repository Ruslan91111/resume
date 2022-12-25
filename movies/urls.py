from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from django.contrib.auth.views import PasswordChangeView
from rest_framework.routers import SimpleRouter

from .views import MoviesHome, CategoriesList, MoviesByCategories, MovieDetailView, \
    AddCommentView, UserRegisterView, EditProfilePageView, ShowProfilePageView, UserEditView, \
    PasswordsChangeView, password_success, CreateProfilePageView, add_rating, show_shot_detail, ActorDetailView, \
    AllActors



urlpatterns = [
    path('', MoviesHome.as_view(), name='home'),
    path('categories', CategoriesList.as_view(), name='list_of_categories'),   # отображение списка категорий
    path('category/<slug:cat_slug>/', MoviesByCategories.as_view(), name='movies_by_category'),   # отображение фильмов одной категории
    path('movies/<slug:movie_slug>', MovieDetailView.as_view(), name='detail_movie'), # Отображение информации об одном фильме
    path('movies/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),  # Добавить к фильму комментарий
    path("rate/<int:movie_id>/<int:rating>/", add_rating, name='add-rating'),    # добавление к фильму рейтинга
    path('<slug:actor_slug>', ActorDetailView.as_view(), name='actor_detail'),  # Отображение информации об актере
    path('shot/<int:shot_pk>', show_shot_detail, name='show-shot-detail'),    # Отображение одного кадра
    path('all_actors/', AllActors.as_view(), name='all-actors'),   # отображение списка всех актеров

    path('register/', UserRegisterView.as_view(), name='register_user'),  # регистрация пользователя
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),  # редактирование настроек профиля
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),  # изменение пароля
    path('password_success/', password_success, name='password_success'),  # для переадресации в случае успешного изменения пароля
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),  # показать профиль пользователя
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),  # создание страницы профиля
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),  # редактирование профиля

]




