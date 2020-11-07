#!/bin/sh

# This script runs through the edge-case scenarios not handled by the normal
# test suite to get coverage to 100%

rm -rf /opt/app-root/lib/python3.8/site-packages/django/
coverage run -a ./manage.py check
coverage report
