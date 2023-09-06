"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from blog.views import PostNews, PostEntertainment, PostFashion, PostSports, PostPolitics, AuthorView, CategoryView, PostDetails, CommentView, RecentPosts
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register('authors', AuthorView, 'author')
router.register('categories', CategoryView, 'category')
router.register('posts', PostDetails, 'post')
router.register('comments', CommentView, 'comment')
router.register('recentposts', RecentPosts, 'recentpost')
router.register('postnews', PostNews, 'postnews')
router.register('postentertainment', PostEntertainment, 'postentertainment')
router.register('postfashion', PostFashion, 'postfashion')
router.register('postsports', PostSports, 'postsports')
router.register('postpolitics', PostPolitics, 'postpolitics')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)