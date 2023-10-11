from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User, AbstractUser
# Create your models here.

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
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=150)
    

    def __str__(self):
        return self.title
    # def __str__(self):
    #     return self.description