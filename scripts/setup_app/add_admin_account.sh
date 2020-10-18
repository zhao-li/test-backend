#!/bin/sh

# This script add an admin user to the Django admin app

echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@ad.min', 'admin')" | python manage.py shell

