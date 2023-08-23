from django.contrib import admin

from .models import Author, Category, Comment, Post

admin.site.register({Author, Category, Comment, Post })
