from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image_url = models.TextField(max_length=200, blank=True)
    location = models.CharField(max_length=30, blank=True)

class Order(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    size = models.CharField(max_length=60)
    def __str__(self):
        return self.name