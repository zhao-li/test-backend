"""Define models"""
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Define User model to customize Django's built-in User"""

