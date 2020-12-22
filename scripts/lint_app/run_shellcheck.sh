#!/bin/bash

# This script runs shellcheck to lint shell scripts

findings_found=0
trap '(( findings_found |= $? ))' ERR

shellcheck -- *.sh
for file in scripts/**/*.sh; do
  shellcheck "$file"
done

exit $findings_found

