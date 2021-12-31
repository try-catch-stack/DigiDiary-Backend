from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import UserProfile
from .serializers import ProfileSerializer

# Create your views here.


class ProfileView(generics.RetrieveUpdateAPIView):

    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)
