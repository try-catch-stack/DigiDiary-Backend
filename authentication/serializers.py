from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from .models import UserProfile, User


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password',
                  'email', 'first_name']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer(read_only=True)

    class Meta:
        model = UserProfile
        # read_only_fields = ['bookmarked_posts']
        fields = ['user']


class SearchProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'email', 'username', ]
