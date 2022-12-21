from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from django.contrib.auth.views import PasswordChangeView
from rest_framework.routers import SimpleRouter

from .views import MoviesHome, CategoriesList, MoviesByCategories, MovieDetailView, \
    AddCommentView, UserRegisterView, EditProfilePageView, ShowProfilePageView, UserEditView, \
    PasswordsChangeView, password_success, CreateProfilePageView, add_rating


urlpatterns = [
    path('', MoviesHome.as_view(), name='home'),
    path('categories', CategoriesList.as_view(), name='list_of_categories'),
    path('category/<slug:cat_slug>/', MoviesByCategories.as_view(), name='movies_by_category'),
    path('movies/<slug:movie_slug>', MovieDetailView.as_view(), name='detail_movie'),
    path('movies/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),  # Добавить к фильму комментарий

    path("rate/<int:movie_id>/<int:rating>/", add_rating, name='add-rating'),    # добавление к фильму рейтинга

    path('register/', UserRegisterView.as_view(), name='register_user'),  # регистрация пользователя
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),  # редактирование настроек профиля
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),  # изменение пароля
    path('password_success/', password_success, name='password_success'),  # для переадресации в случае успешного изменения пароля
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),  # показать профиль пользователя
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),  # создание страницы профиля
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),  # редактирование профиля

]

# urlpatterns += router.urls

# path('add_post/', AddPostView.as_view(), name='add_post'),
# path('add_category/', AddCategoryView.as_view(), name='add_category'),
# path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
# path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
# path('category/<str:cats>/', category_view, name='category'),
# path('category-list/', category_list_view, name='category-list'),
# path('like/<int:pk>', like_view, name='like_post'),
# path('article/<int:pk>/comment', AddCommentView.as_view(), name='add_comment')
#


