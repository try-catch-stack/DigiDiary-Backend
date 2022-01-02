from django.urls import path
from .views import ProfileView

urlpatterns = [
    path('auth/profile/me', ProfileView.as_view(), name='profile'),
]
