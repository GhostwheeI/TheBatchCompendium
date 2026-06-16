#!/usr/bin/env python3
"""
Pre-filter discovered repositories to remove duplicates.
This script checks for existing repositories in both the database and directory structure.
"""

import csv
import os
import sys
from pathlib import Path

print('🔍 Pre-processing: Checking for existing repositories and scripts...')

# Load discovered repositories
# The DISCOVERY_FILE is set by the workflow step
discovery_file = os.environ.get('DISCOVERY_FILE')
if not discovery_file or not os.path.exists(discovery_file):
    print(f'Discovery file not found: {discovery_file}')
    sys.exit(1)

try:
    with open(discovery_file, 'r') as f:
        reader = csv.DictReader(f)
        discovered_repos = list(reader)
except (OSError, csv.Error) as e:
    print(f'Failed to read discovery file "{discovery_file}": {e}')
    sys.exit(1)

print(f'Discovered {len(discovered_repos)} repositories')

# Load existing repositories
existing_repos = []
if os.path.exists('repo_results.csv'):
    try:
        with open('repo_results.csv', 'r') as f:
            reader = csv.DictReader(f)
            existing_repos = list(reader)
        print(f'Found {len(existing_repos)} existing repositories')
    except (OSError, csv.Error) as e:
        print(f'Failed to read existing repository database "repo_results.csv": {e}')
        sys.exit(1)
else:
    print('No existing repository database found')

# Check for existing directories/scripts
base_path = Path('../../')
existing_dirs = set()

# Scan existing directory structure
if not base_path.exists() or not base_path.is_dir():
    print(f'Base path does not exist or is not a directory: {base_path}')
else:
    try:
        for category_dir in base_path.iterdir():
            if category_dir.is_dir() and not category_dir.name.startswith('.') and not category_dir.name.startswith('z.'):
                try:
                    for repo_dir in category_dir.iterdir():
                        if repo_dir.is_dir():
                            existing_dirs.add(repo_dir.name.lower())
                except OSError as e:
                    print(f'Warning: unable to access contents of {category_dir}: {e}')
    except OSError as e:
        print(f'Warning: unable to access base path {base_path}: {e}')

print(f'Found {len(existing_dirs)} existing repository directories')

# Filter out repositories that already exist
filtered_repos = []
for repo in discovered_repos:
    repo_name = repo.get('name', '').replace('/', '--').replace('\\', '--')
    repo_url = repo.get('url', '')

    # Check if repository already exists in CSV
    exists_in_csv = any(
        existing.get('name', '').lower() == repo.get('name', '').lower() or
        existing.get('url', '').lower() == repo_url.lower()
        for existing in existing_repos
    )

    # Check if directory already exists
    exists_as_dir = repo_name.lower() in existing_dirs

    if exists_in_csv:
        print(f'⏭️ Skipping {repo.get("name", "unknown")} - already in database')
    elif exists_as_dir:
        print(f'⏭️ Skipping {repo.get("name", "unknown")} - directory already exists')
    else:
        filtered_repos.append(repo)
        print(f'✅ New repository: {repo.get("name", "unknown")} ({repo.get("stars", 0)} stars)')

print(f'Pre-filtered to {len(filtered_repos)} truly new repositories')

# Save pre-filtered results
with open('pre_filtered_repos.csv', 'w', newline='') as f:
    if filtered_repos:
        fieldnames = filtered_repos[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filtered_repos)
    else:
        writer = csv.writer(f)
        writer.writerow(['name', 'url', 'description', 'stars', 'language'])

print('✅ Pre-filtering complete')
