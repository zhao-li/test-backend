"""
Register Greeting models Django admin
https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#modeladmin-objects
https://docs.djangoproject.com/en/2.1/intro/tutorial02/#make-the-poll-app-modifiable-in-the-admin
"""
from django.contrib import admin

from .models import Greeting

admin.site.register(Greeting)
