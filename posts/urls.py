from django.urls import path
from .views import PostDetailView, PostsView

urlpatterns = [path('posts/', PostsView.as_view(), name='posts'),
               path('posts/<int:pk>/', PostDetailView.as_view(), name='post')]
