from django.shortcuts import render
from rest_framework.views import APIView, View
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from authentication.models import UserProfile
from .models import Post
from .serializers import PostSerializer, PostBookmarkSerializer

# Create your views here.


class PostsView(generics.ListCreateAPIView):
    queryset = Post.objects.all().prefetch_related('author',)
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return [AllowAny()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostBookmarkView(generics.UpdateAPIView):

    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostBookmarkSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if request.user in instance.bookmarks.all():
            instance.bookmarks.remove(request.user)
        else:
            instance.bookmarks.add(request.user)
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class BookmarkedPostsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(bookmarks=self.request.user)
