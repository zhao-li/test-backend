"""Defines views"""
from rest_framework import viewsets
from .models import Transaction
from .serializers import TransactionSerializer


# pylint:disable=too-many-ancestors
class TransactionViewSet(viewsets.ModelViewSet):
    """API endpoints for Transaction"""

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

