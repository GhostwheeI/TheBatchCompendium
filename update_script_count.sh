#!/bin/bash
# Script to update the batch script count in README.md
# 
# This script automatically counts all .bat and .cmd files in the repository
# and updates both the dynamic counter at the top of README.md and the badge.
# 
# Usage: ./update_script_count.sh
#
# Run this script whenever new scripts are added to keep the count accurate.

# Count all .bat and .cmd files (excluding .git directory)
SCRIPT_COUNT=$(find . -type f \( -name "*.bat" -o -name "*.cmd" \) ! -path "./.git/*" | wc -l)

echo "Found ${SCRIPT_COUNT} batch scripts"

# Format the count with commas for better readability (works for any number length)
FORMATTED_COUNT=$(echo "${SCRIPT_COUNT}" | sed ':a;s/\B[0-9]\{3\}\>/,&/;ta')

# Update the badge in README.md (no commas in URL)
# First update any badge with %2B (plus sign URL encoded), then update plain number badges
# Using .bak extension for cross-platform compatibility (macOS requires an extension argument)
sed -i.bak "s/scripts-[0-9]*%2B-green/scripts-${SCRIPT_COUNT}-green/g" README.md
sed -i.bak "s/badge\/scripts-[0-9]*/badge\/scripts-${SCRIPT_COUNT}/g" README.md

# Update the big counter at the top of README.md (with commas for display)
sed -i.bak "s/## 📊 \*\*[0-9,]* BATCH SCRIPTS\*\* 📊/## 📊 **${FORMATTED_COUNT} BATCH SCRIPTS** 📊/g" README.md

# Remove backup files created by sed
rm -f README.md.bak

echo "README.md updated with script count: ${FORMATTED_COUNT}"
