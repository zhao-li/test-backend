#!/bin/sh

# This script runs shellcheck to lint shell scripts

shellcheck -- *.sh
for file in scripts/**/*.sh; do
  shellcheck "$file"
done

