from django.db import models
from django.conf import settings
# Create your models here.


class Write(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    url = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    cnt = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_posts")


class Comment(models.Model):
    comment = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    write = models.ForeignKey(Write, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    comment_like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="comment_like_posts")
