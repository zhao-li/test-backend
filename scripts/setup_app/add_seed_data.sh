#!/bin/sh

# This script adds seed data

./manage.py loaddata \
  greetings/seeds.yaml \
  trading_accounts/seeds.yaml \
  transactions/seeds.yaml

