#!/bin/sh

# This script exercises starting the application without the django library
# installed

pip uninstall --yes django
coverage run --append ./manage.py check
pip install --requirement requirements.txt

