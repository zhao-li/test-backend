"""Define models"""
from django.db import models


class Transaction(models.Model):
    """Define Transaction model"""
    raw = models.JSONField(null=True, blank=True)

