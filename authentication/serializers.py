from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer
from django.db import IntegrityError
from .models import UserProfile, User


class UserCreateSerializer(BaseUserCreateSerializer):

    def create(self, validated_data):
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            self.fail("cannot_create_user")

        profile = UserProfile.objects.create(user=user)

        return user

    name = serializers.CharField(source='first_name')

    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password',
                  'email', 'name']


class UserSerializer(BaseUserSerializer):
    name = serializers.CharField(source='first_name')

    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'name', ]


class ProfileSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer(read_only=True)

    class Meta:
        model = UserProfile
        # read_only_fields = ['bookmarked_posts']
        fields = ['user', ]
