from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User, AbstractUser
# Create your models here.
# import uuid


class student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Roll_number = models.CharField(max_length=100)
    Password = models.CharField(max_length=50)
    Email_address = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class QueryPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_post", default=None, null=True)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=150)
    votes = models.ManyToManyField(User, related_name="votes_posts", blank=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    def total_likes(self):
        return self.likes.count()

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_likes")
    post = models.ForeignKey(QueryPost, on_delete=models.CASCADE, related_name="post_likes")
