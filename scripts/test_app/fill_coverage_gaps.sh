#!/bin/sh

# This script runs through the edge-case scenarios not handled by the normal
# test suite to get coverage to 100%

SRC_DIR=$(cd "$(dirname "$0")" || exit; pwd -P)

"$SRC_DIR"/fill_coverage_gaps/exercise_cors_environment_variable.sh
"$SRC_DIR"/fill_coverage_gaps/exercise_django_not_installed.sh
"$SRC_DIR"/fill_coverage_gaps/exercise_multiple_cors_allowed_origins.sh
"$SRC_DIR"/fill_coverage_gaps/exercise_seeding.sh

