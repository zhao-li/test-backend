""" Define URL/routes """

from django.urls import re_path
from .views import ImportTransactions


urlpatterns = [
    re_path(r'transactions/', ImportTransactions.as_view()),
]

