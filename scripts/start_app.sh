#!/bin/sh

# This script starts the application

SRC_DIR=$(cd "$(dirname "$0")" || exit; pwd -P)
. "$SRC_DIR"/common/functions.sh

wait_for_service $DATABASE_HOST $DATABASE_PORT

python manage.py runserver 0.0.0.0:"$APP_PORT"
