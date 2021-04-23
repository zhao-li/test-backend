#!/bin/sh

# This script runs shellcheck to lint shell scripts

findings_found=0
update_findings_count() {
  findings_found=$(findings_found + 1)
}

shellcheck --external -- *.sh || update_findings_count
for file in scripts/**/*.sh; do
  shellcheck --external "$file" || update_findings_count
done

exit "$findings_found"

