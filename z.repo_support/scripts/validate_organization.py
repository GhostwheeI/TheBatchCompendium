#!/usr/bin/env python3
"""
Validate repository organization.
This script ensures all discovered repositories have proper structure and READMEs.
"""

import csv
import os
from pathlib import Path

print('🔍 Performing final validation...')

# Check if we have new repositories to validate
if not os.path.exists('filtered_new_repos.csv'):
    print('No new repositories to validate')
    exit(0)

try:
    with open('filtered_new_repos.csv', 'r') as f:
        reader = csv.DictReader(f)
        new_repos = list(reader)
except (OSError, csv.Error) as e:
    print(f"Error reading 'filtered_new_repos.csv': {e}")
    exit(1)

if not new_repos:
    print('No repositories in filtered file')
    exit(0)

base_path = Path('../../')
validation_errors = []
validation_success = []

for repo in new_repos:
    repo_name = repo.get('name', '').replace('/', '_').replace('\\', '_')
    category = repo.get('category', 'Uncategorized')

    if not repo_name:
        continue

    # Check directory structure
    category_dir = base_path / category.replace(' & ', '_').replace(' ', '_')
    repo_dir = category_dir / repo_name
    readme_path = repo_dir / 'README.md'

    # Validate structure
    if not category_dir.exists():
        validation_errors.append(f'❌ Category directory missing: {category_dir}')
    elif not repo_dir.exists():
        validation_errors.append(f'❌ Repository directory missing: {repo_dir}')
    elif not readme_path.exists():
        validation_errors.append(f'❌ README missing: {readme_path}')
    else:
        validation_success.append(f'✅ {repo_name} properly organized')

print(f'\n📊 Validation Results:')
print(f'✅ Successfully organized: {len(validation_success)}')
print(f'❌ Validation errors: {len(validation_errors)}')

if validation_success:
    print('\n✅ Successfully organized repositories:')
    for success in validation_success[:10]:  # Show first 10
        print(f'  {success}')
    if len(validation_success) > 10:
        print(f'  ... and {len(validation_success) - 10} more')

if validation_errors:
    print('\n❌ Validation errors found:')
    for error in validation_errors:
        print(f'  {error}')
    exit(1)

print('\n🎉 All repositories properly organized with READMEs!')
