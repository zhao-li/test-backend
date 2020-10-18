#!/bin/sh

# This script sets up the application

SRC_DIR=$(cd "$(dirname "$0")" || exit; pwd -P)

python manage.py migrate
"$SRC_DIR"/setup_app/add_admin_account.sh

