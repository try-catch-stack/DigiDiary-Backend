from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from .models import UserProfile, User


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password',
                  'email', 'first_name', 'last_name']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile()
        read_only_fields = ['id', 'bookmarked_posts']
        fields = ['id', 'bookmarked_posts']


class SearchProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User()
        read_only_fields = ['id']
        fields = ['id', 'name', 'email', 'username', ]
