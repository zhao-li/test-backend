#!/bin/sh

# This script exercises starting the application without the django library
# installed

CORS_ALLOWED_ORIGINS="" coverage run --append ./manage.py check

