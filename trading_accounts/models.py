"""Define models"""
from django.db import models


class TradingAccount(models.Model):
    """Define TradingAccount model"""
    name = models.CharField(max_length=200)

