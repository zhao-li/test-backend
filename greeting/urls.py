""" Greeting url configuration """

from django.conf.urls import include
from django.urls import re_path
from rest_framework import routers
from .views import GreetingViewSet

ROUTER = routers.DefaultRouter()
ROUTER.register(r'', GreetingViewSet)

urlpatterns = [
    re_path(r'', include(ROUTER.urls)),
]
