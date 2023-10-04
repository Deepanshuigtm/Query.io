from django.db import models
from django.core.validators import MinLengthValidator

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
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="query_posts", null=True)
    issue_name = models.CharField(max_length=150)
    description = models.TextField()
    more_details = models.TextField()

    def __str__(self):
        return self.title