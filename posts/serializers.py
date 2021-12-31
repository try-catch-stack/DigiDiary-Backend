from rest_framework import serializers
from .models import Post
from authentication.serializers import SearchProfileSerializer


class PostSerializer(serializers.ModelSerializer):
    author = SearchProfileSerializer(read_only=True)

    class Meta:
        model = Post
        read_only_fields = ['likes', 'author']
        fields = ['title', 'topic', 'author',
                  'image_url', 'likes', 'post_content']
