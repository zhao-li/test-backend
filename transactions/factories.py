"""Define factories"""
import factory
from trading_accounts.factories import TradingAccountFactory
from .models import Transaction


class TransactionFactory(factory.django.DjangoModelFactory):
    """Define Transaction factory"""
    class Meta:
        model = Transaction

    account = factory.SubFactory(TradingAccountFactory)

