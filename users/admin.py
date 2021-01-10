"""
Register models to Django admin interface
"""
from django.contrib import admin
from .models import User

admin.site.register(User)

