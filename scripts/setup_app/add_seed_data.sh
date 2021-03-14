#!/bin/sh

# This script adds seed data

./manage.py loaddata greetings/seeds.yaml
./manage.py loaddata trading_accounts/seeds.yaml
./manage.py loaddata transactions/seeds.yaml

