#!/bin/sh

# This script starts the application

python manage.py runserver 0.0.0.0:"$APP_PORT"
