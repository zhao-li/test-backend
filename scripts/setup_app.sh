#!/bin/sh

# This script sets up the application

SRC_DIR=$(cd "$(dirname "$0")" || exit; pwd -P)

python manage.py migrate

