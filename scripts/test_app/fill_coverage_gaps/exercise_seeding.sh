#!/bin/sh

# This script exercises seeding the application

./manage.py flush --no-input
coverage run --append ./manage.py loaddata ./*/seeds.yaml

