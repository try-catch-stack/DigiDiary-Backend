from django.db import models
from django.contrib.auth.models import AbstractUser
from posts.models import Post


class User(AbstractUser):
    email = models.EmailField(unique=True)


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    photo_url = models.URLField(null=True, blank=True, editable=False)
    bookmarked_posts = models.ManyToManyField(Post, null=True, blank=True)

    def __str__(self):
        return self.user.username
