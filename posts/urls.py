from django.urls import path
from .views import PostDetailView, PostsView, PostBookmarkView, BookmarkedPostsView
urlpatterns = [path('posts/', PostsView.as_view(), name='posts'),
               path('posts/<int:pk>/', PostDetailView.as_view(), name='post'),
               path('posts/<int:pk>/bookmark',
                    PostBookmarkView.as_view(), name='post_bookmark'),
               path('posts/bookmarks', BookmarkedPostsView.as_view(),
                    name='bookmarked_posts'),
               ]
