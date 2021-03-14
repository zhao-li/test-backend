"""Define factories"""
import factory
from users.factories import UserFactory
from .models import TradingAccount


class TradingAccountFactory(factory.django.DjangoModelFactory):
    """Define Trading Account factory"""
    class Meta:
        model = TradingAccount

    owner = factory.SubFactory(UserFactory)

