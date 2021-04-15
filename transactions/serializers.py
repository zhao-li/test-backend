"""Define serializers"""
from rest_framework_json_api import serializers
from .models import Transaction


# pylint:disable=too-many-ancestors
class TransactionSerializer(serializers.ModelSerializer):
    """Define Transaction serializer"""

    class Meta:
        model = Transaction
        fields = '__all__'

