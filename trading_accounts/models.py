"""Define models"""
from django.db import models


class TradingAccount(models.Model):
    """Define TradingAccount model"""
    name = models.CharField(max_length=200)
    owner = models.ForeignKey('users.user', on_delete=models.CASCADE)

