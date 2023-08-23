from rest_framework import serializers

from .models import Post, Comment, Category, Author

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'excerpt', 'content', 'featuredImage', 'featuredPost', 'author', 'category')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'photo', 'bio')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('dateadded', 'name', 'email', 'comment', 'post')

