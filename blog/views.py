from django.shortcuts import render
from .models import Post, Author, Category, Comment
from rest_framework import viewsets
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import PostSerializer, AuthorSerializer, CategorySerializer, CommentSerializer

class PostView(views.APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_ok)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetails(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class RecentPosts(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('-id')[:3]
    serializer_class = PostSerializer

class PostNews(viewsets.ModelViewSet):
    queryset = Post.objects.filter(category='news')
    serializer_class = PostSerializer

class PostEntertainment(viewsets.ModelViewSet):
    queryset = Post.objects.filter(category='entertainment')
    serializer_class = PostSerializer

class PostFashion(viewsets.ModelViewSet):
    queryset = Post.objects.filter(category='fashion')
    serializer_class = PostSerializer

class PostSports(viewsets.ModelViewSet):
    queryset = Post.objects.filter(category='sports')
    serializer_class = PostSerializer

class PostPolitics(viewsets.ModelViewSet):
    queryset = Post.objects.filter(category='politics')
    serializer_class = PostSerializer

class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

