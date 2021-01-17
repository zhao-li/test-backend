"""Define serializers"""
from rest_framework import serializers
from .models import TradingAccount


class TradingAccountSerializer(serializers.HyperlinkedModelSerializer):
    """Define Trading Account serializer"""

    class Meta:
        model = TradingAccount
        fields = '__all__'

