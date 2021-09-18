from django.db import models
from django.db.models.base import Model

# Create your models here.
class Todo(models.Model):
    time = models.CharField(max_length=50)
    title = models.CharField(max_length=128)
    priority = models.CharField(max_length=3)
    category = models.CharField(max_length=20)

class Inprogress(models.Model):
    time = models.CharField(max_length=50)
    title = models.CharField(max_length=128)
    priority = models.CharField(max_length=3)
    category = models.CharField(max_length=20)

class Done(models.Model):
    time = models.CharField(max_length=50)
    title = models.CharField(max_length=128)
    priority = models.CharField(max_length=3)
    category = models.CharField(max_length=20)