from django.contrib import admin
from blogapp.models import Post, Comment
from . import models
# Register your models here.

class PostModel(admin.ModelAdmin):
    search_fields = ['title', 'author']

    list_filter = ['create_date']

    list_display = ['title', 'author', 'create_date']

admin.site.register(models.Post, PostModel)
admin.site.register(Comment)