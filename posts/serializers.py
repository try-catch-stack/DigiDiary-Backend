import re
from rest_framework import serializers
from .models import Post
from authentication.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        read_only_fields = ['id', 'likes', 'author', 'created_at']
        fields = ['id', 'title', 'topic', 'author',
                  'image_url', 'likes', 'post_content', 'created_at']


class PostBookmarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        read_only_fields = ['title', 'topic',
                            'author', 'post_content', 'bookmarks']
        fields = ['title', 'topic', 'author', 'post_content', 'bookmarks']
