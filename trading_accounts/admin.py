"""Register models to Django admin console"""

from django.contrib import admin

from .models import TradingAccount

admin.site.register(TradingAccount)

