#!/bin/sh

# This script exercises environmental variable CORS_ALLOWED_ORIGINS having
# multiple origins

CORS_ALLOWED_ORIGINS=http://origin1,http://origin2 coverage run --append ./manage.py check

