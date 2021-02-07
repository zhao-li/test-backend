""" Define URL/routes """

from django.conf.urls import include
from django.urls import re_path
from rest_framework import routers
from .views import TradingAccountViewSet

ROUTER = routers.DefaultRouter()
ROUTER.register(r'', TradingAccountViewSet)

urlpatterns = [
    re_path(r'', include(ROUTER.urls)),
]

