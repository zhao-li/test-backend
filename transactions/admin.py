""" Register models to Django admin interface """
from django.contrib import admin
from .models import Transaction

admin.site.register(Transaction)

