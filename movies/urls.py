from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import MoviesHome, CategoriesList, MoviesByCategories, MovieDetailView, AddReview


urlpatterns = [
    path('', MoviesHome.as_view(), name='home'),
    path('categories', CategoriesList.as_view(), name='list_of_categories'),
    path('category/<slug:cat_slug>/', MoviesByCategories.as_view(), name='movies_by_category'),
    path('movies/<slug:movie_slug>', MovieDetailView.as_view(), name='detail_movie'),
    path('movies/<slug:movie_slug>/add_review', AddReview.as_view(), name='add_post'),

]

# path('add_post/', AddPostView.as_view(), name='add_post'),
# path('add_category/', AddCategoryView.as_view(), name='add_category'),
# path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
# path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
# path('category/<str:cats>/', category_view, name='category'),
# path('category-list/', category_list_view, name='category-list'),
# path('like/<int:pk>', like_view, name='like_post'),
# path('article/<int:pk>/comment', AddCommentView.as_view(), name='add_comment')
#


