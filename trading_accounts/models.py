"""Define models"""
from django.db import models
from .managers import TradingAccountManager


class TradingAccount(models.Model):
    """Define TradingAccount model"""
    objects = TradingAccountManager()

    name = models.CharField(max_length=200)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)

