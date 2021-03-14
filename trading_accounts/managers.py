"""Define model managerss"""
from django.db import models
from users.models import User


# pylint:disable=too-few-public-methods
class TradingAccountManager(models.Manager):
    """Define TradingAccount model manager"""
    def get_by_natural_key(self, name, owner_username):
        """Allow seeds to use natural keys instead of primary keys"""
        owner = User.objects.get(username=owner_username)
        return self.get(name=name, owner=owner)

