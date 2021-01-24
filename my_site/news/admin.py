from django.contrib import admin
from .models import News


# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


# Внимание! Порядок регистрации важен! Спачала News, а потом уже все остальное.
admin.site.register(News, NewsAdmin)
