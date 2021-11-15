#!/bin/sh

# This script documents the application

rm --force --recursive artifacts/docs/* # force is used to suppress warnings when directory is empty
sphinx-apidoc --force --output-dir docs/source .
sphinx-build docs/source/ artifacts/docs/
#sphinx-build -b coverage docs/source/ docs/build/ # not sure how to get sphinx coverage to work with autodoc
# https://stackoverflow.com/questions/33436025/sphinx-autodoc-vs-coverage-am-i-missing-something-here

