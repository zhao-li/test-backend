"""Defines views"""
from rest_framework import viewsets
from .models import Greeting
from .serializers import GreetingSerializer


# pylint:disable=too-many-ancestors
class GreetingsViewSet(viewsets.ModelViewSet):
    """API endpoints for Greeting"""

    queryset = Greeting.objects.all()
    serializer_class = GreetingSerializer

