#!/bin/sh

# This script lints the application

shellcheck -- \
  *.sh \
  scripts/*.sh \
  scripts/bootstrap/*.sh \
  scripts/setup_app/*.sh
pycodestyle .
pylint -- *
