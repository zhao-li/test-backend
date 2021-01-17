"""Defines views"""
from rest_framework import viewsets
from .models import TradingAccount
from .serializers import TradingAccountSerializer


class TradingAccountViewSet(viewsets.ModelViewSet):
    """API endpoints for Trading Account"""

    queryset = TradingAccount.objects.all()
    serializer_class = TradingAccountSerializer

