import django.contrib.auth.models
from django.db import models


# Create your models here.
class Vacancy(models.Model):
    description = models.CharField(max_length=1024)
    author= models.ForeignKey(django.contrib.auth.models.User, on_delete=models.CASCADE)
