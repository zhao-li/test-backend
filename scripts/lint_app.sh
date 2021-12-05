#!/bin/sh

# This script lints the application

SRC_DIR=$(cd "$(dirname "$0")" || exit; pwd -P)

"$SRC_DIR"/lint_app/run_pycodestyle.sh
"$SRC_DIR"/lint_app/run_pylint.sh

