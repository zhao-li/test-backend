# Template

Prerequisites
-------------
1. install docker
1. install docker-compose
1. install git
1. clone repository: `git clone --recursive TBD`

Getting Started
---------------
1. run bootstrap.sh: `./bootstrap.sh`
1. start service: `docker-compose up`

Testing
-------
To test the application:

    app$ scripts/test_app.sh

To run a single test:

    app$ python manage.py test greeting.tests.GreetingTests.test_fetching_greeters

Linting
-------
To lint the application:

    app$ scripts/lint_app.sh

Documenting
-----------
To document the application:

    app$ scripts/document_app.sh

Migratiing Database
-------------------
To create database migrations:

    app$ python manage.py makemigrations

For more information: https://docs.djangoproject.com/en/3.1/topics/migrations/

Notes
-----
TBD
