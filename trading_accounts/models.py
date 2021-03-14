"""Define models"""
from django.db import models
from users.models import User


class TradingAccountManager(models.Manager):
    def get_by_natural_key(self, name, owner_username):
        owner = User.objects.get(username=owner_username)
        return self.get(name=name, owner=owner)

class TradingAccount(models.Model):
    """Define TradingAccount model"""
    objects = TradingAccountManager()

    name = models.CharField(max_length=200)
    owner = models.ForeignKey('users.user', on_delete=models.CASCADE)

