from django.contrib import admin
from .models import Category, Movies, Comment, Profile, UserMovieRelations, RatingMovie


admin.site.register(Category)
admin.site.register(Movies)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(UserMovieRelations)
admin.site.register(RatingMovie)

