# Porter:Backend
The API backend for the Porter application.

[![pipeline status](https://gitlab.com/porter4/backend/badges/master/pipeline.svg)](https://gitlab.com/porter4/backend/-/commits/master)
[![coverage report](https://gitlab.com/porter4/backend/badges/master/coverage.svg?job=integration-test)](https://gitlab.com/porter4/backend/-/commits/master)

Prerequisites
-------------
1. install docker
1. install docker-compose
1. install git
1. clone repository: `git clone --recursive https://gitlab.com/porter4/backend.git`

Getting Started
---------------
1. run bootstrap.sh: `./bootstrap.sh`
1. start service: `docker-compose up`

Testing
-------
To test the application:

    backend$ scripts/test_app.sh

To run a single test:

    backend$ ./manage.py test greetings.tests.GreetingsTests.test_fetching_greeters

Linting
-------
To lint the application:

    backend$ scripts/lint_app.sh

Documenting
-----------
To document the application:

    backend$ scripts/document_app.sh

Migratiing Database
-------------------
To create database migrations:

    backend$ python manage.py makemigrations

For more information: https://docs.djangoproject.com/en/3.1/topics/migrations/

Notes
-----
TBD

