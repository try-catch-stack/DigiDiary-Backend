from django.db import models
from django.contrib.auth.models import AbstractUser
from posts.models import Post
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo_url = models.URLField(null=True, blank=True, editable=False)

    def __str__(self):
        return self.user.username
