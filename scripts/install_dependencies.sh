#!/bin/sh

# This script installs the application dependencies

# set_defaults
#
# sets up the defaults to be used later
#
# example usage: set_defaults
set_defaults() {
  environment=production
}

# gather_options
#
# gathers the options provided by the user
# based off of http://linuxcommand.org/lc3_wss0120.php
#
# example usage: gather_options "$@"
gather_options() {
  while [ "$1" != "" ]; do
    case $1 in
      -e)
        environment=$2
        shift
      ;;
    esac
    shift
  done
}

set_defaults
gather_options "$@"

#pip install --upgrade pip
case $environment in
  'production')
    pip install -r requirements.txt
  ;;
  'development')
    pip install -r requirements.development.txt
  ;;
esac

