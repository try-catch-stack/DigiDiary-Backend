from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from authentication.models import UserProfile
from .models import Post
from .serializers import PostSerializer

# Create your views here.


class PostsView(generics.ListCreateAPIView):
    queryset = Post.objects.all().prefetch_related('author')
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=UserProfile.objects.get(user=self.request.user))


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
