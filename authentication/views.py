from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from .models import User, UserProfile
from .serializers import ProfileSerializer

# Create your views here.


class ProfileView(generics.RetrieveUpdateAPIView):

    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        queryset = self.get_queryset()
        UserProfile.objects.get_or_create(user=self.request.user)
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj
