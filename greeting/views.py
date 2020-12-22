"""Defines the Greeting views"""
from rest_framework import viewsets
from .models import Greeting
from .serializers import GreetingSerializer


class GreetingViewSet(viewsets.ModelViewSet):
    """API endpoints for Greeting"""

    queryset= Greeting.objects.all()
    serializer_class = GreetingSerializer
