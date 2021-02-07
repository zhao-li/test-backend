""" Define URL/routes """

from django.conf.urls import include
from django.urls import re_path
from rest_framework import routers
from .views import GreetingsViewSet

ROUTER = routers.DefaultRouter()
ROUTER.register(r'', GreetingsViewSet)

urlpatterns = [
    re_path(r'', include(ROUTER.urls)),
]

