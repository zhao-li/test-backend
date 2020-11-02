#!/bin/sh

# This script sets up the application

SRC_DIR=$(cd "$(dirname "$0")" || exit; pwd -P)
. "$SRC_DIR"/setup_app/functions.sh

wait_for_service "$DATABASE_HOST" "$DATABASE_PORT"

python manage.py migrate
"$SRC_DIR"/setup_app/add_admin_account.sh
"$SRC_DIR"/setup_app/add_seed_data.sh

