"""Define serializers"""
from rest_framework_json_api import serializers
from .models import TradingAccount


# pylint:disable=too-many-ancestors
class TradingAccountSerializer(serializers.ModelSerializer):
    """Define Trading Account serializer"""

    class Meta:
        model = TradingAccount
        fields = '__all__'

