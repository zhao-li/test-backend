#!/bin/sh

# This script runs the integration test suite

coverage run --append manage.py test --tag=integration

