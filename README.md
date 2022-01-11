# Porter:Backend
The API backend for the Porter application.

[![pipeline status](https://gitlab.com/starting-spark/porter/backend/badges/master/pipeline.svg)](https://gitlab.com/starting-spark/porter/backend/-/commits/master)
[![coverage report](https://gitlab.com/starting-spark/porter/backend/badges/master/coverage.svg)](https://gitlab.com/starting-spark/porter/backend/-/commits/master)

Prerequisites
-------------
1. install docker
1. install docker-compose
1. install git
1. clone repository: `git clone --recursive https://gitlab.com/starting-spark/porter/backend.git`

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

To lint the shell scripts:

    $ docker-compose run shell-checker sh
    shell-checker$ scripts/lint_app/run_shellcheck.sh

    or

    $ docker-compose run shell-checker scripts/lint_app/run_shellcheck.sh

Documenting
-----------
To document the application:

    backend$ scripts/document_app.sh

Migrating Database
------------------
To create database migrations:

    backend$ python manage.py makemigrations

For more information: https://docs.djangoproject.com/en/3.1/topics/migrations/

Using Production Container
--------------------------
To run the production container

    $ docker compose \
        --profile production \
        up \
        backend-production

Notes
-----
TBD

