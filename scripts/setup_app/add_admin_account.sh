#!/bin/sh

# This script add an admin user to the Django admin app

DJANGO_SUPERUSER_USERNAME=admin \
DJANGO_SUPERUSER_EMAIL=admin@admin.admin \
DJANGO_SUPERUSER_PASSWORD=admin \
python manage.py createsuperuser --noinput

