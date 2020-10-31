"""Define Greeting serializers"""
from rest_framework import serializers
from .models import Greeting


class GreetingSerializer(serializers.HyperlinkedModelSerializer):
    """Define Greeting serializer"""

    class Meta:
        model = Greeting
        fields = '__all__'
