#!/bin/sh

# This script runs through the edge-case scenarios not handled by the normal
# test suite to get coverage to 100%

pip uninstall --yes django
coverage run --append ./manage.py check
pip install --requirement requirements.txt

