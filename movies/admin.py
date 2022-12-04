from django.contrib import admin
from .models import Category



#
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title_cat')
#     list_display_links = ('id', 'title_cat')
#     search_fields = ('id', 'title_cat')
#     prepopulated_fields = {"slug": ("title_cat",)}

admin.site.register(Category)
# admin.site.register(Category, CategoryAdmin)