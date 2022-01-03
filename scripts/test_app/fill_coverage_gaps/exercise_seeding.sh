#!/bin/sh

# This script exercises seeding the application

coverage run --append ./manage.py loaddata ./*/seeds.yaml

