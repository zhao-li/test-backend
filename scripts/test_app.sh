#!/bin/sh

# This script tests the application

coverage run manage.py test
coverage report

