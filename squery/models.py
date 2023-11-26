from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User, AbstractUser
import uuid

class Profile(models.Model):
 email= models. EmailField()
 token = models.CharField(default='', max_length=1000)
 is_verified = models.BooleanField(default=False)
 
 created_at = models.DateTimeField(auto_now_add=True) 
 updated_at = models.DateTimeField(auto_now=True)

def str(self)-> str: 
    return self.email

def save(self, *args, **kwargs): 
    self.token =str(uuid.uuid4())
    super(Profile, self).save(*args, **kwargs)
    

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

class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_rewards",default=None)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=150)
    file = models.FileField(upload_to="rewards")

    def __str__(self):
        return self.title

class QueryPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_post", default=None, null=True)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="posts", null=True)
    certificates = models.ManyToManyField(Certificate, related_name="rewards")
    date = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=150)
    votes = models.ManyToManyField(User, related_name="votes_posts", blank=True)
    likes = models.IntegerField(default=0)
    is_resolved  = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    def total_likes(self):
        return self.likes.count()
    def get_resolved_status(self):  # Changed method name to 'get_resolved_status'
        return self.is_resolved

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_likes")
    post = models.ForeignKey(QueryPost, on_delete=models.CASCADE, related_name="post_likes")
