"""Define factories"""
import factory
from .models import User


class UserFactory(factory.django.DjangoModelFactory):
    """Define User factory"""
    class Meta:
        model = User

