#!/bin/sh

# This script runs the unit test suite

coverage run --append manage.py test --tag=unit

