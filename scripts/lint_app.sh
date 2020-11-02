#!/bin/bash

# This script lints the application

SRC_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

. "$SRC_DIR"/lint_app/run_shellcheck.sh
pycodestyle .
pylint -- *

