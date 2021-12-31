from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.TextField()
    topic = models.CharField(max_length=100)
    author = models.ForeignKey(
        'authentication.UserProfile', on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    image_url = models.URLField()
    post_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Title,PostContent,Topic,Author,Likes,ImageUrl
