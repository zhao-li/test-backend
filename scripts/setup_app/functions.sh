#!/bin/sh

# some functions are defined with parenthesis instead of curly braces
# to support shellcheck linting and local variables
# https://github.com/thoughtbot/laptop/issues/481
# https://stackoverflow.com/questions/18597697/posix-compliant-way-to-scope-variables-to-a-function-in-a-shell-script#answer-18600920

# wait_for_service
#
# waits for service to be ready for connection
#
# example usage: wait_for_service http://localhost 27017
wait_for_service() {
  local host=$1
  local port=$2

  local service_up=1 #assume service is not up yet
  until [ "$service_up" -eq 0 ]; do
    sleep 5
    nc -z "$host" "$port"
    service_up=$?
  done
}

