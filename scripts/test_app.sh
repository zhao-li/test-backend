#!/bin/sh

# This script tests the application

SRC_DIR=$(cd "$(dirname "$0")" || exit; pwd -P)

"$SRC_DIR"/test_app/run_unit_tests.sh
"$SRC_DIR"/test_app/run_integration_tests.sh
"$SRC_DIR"/test_app/fill_coverage_gaps.sh
coverage report

