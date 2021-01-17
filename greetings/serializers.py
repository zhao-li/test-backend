"""Define serializers"""
from rest_framework_json_api import serializers
from .models import Greeting


# pylint:disable=too-many-ancestors
class GreetingSerializer(serializers.ModelSerializer):
    """Define Greeting serializer"""

    class Meta:
        model = Greeting
        fields = '__all__'

