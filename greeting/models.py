"""Define Greeting models"""
from django.db import models


class Greeting(models.Model):
    """Define Greeting model"""
    message = models.CharField(max_length=200)
