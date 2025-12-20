#!/usr/bin/env python3
"""
Organize repositories and create READMEs.
This script ensures all discovered repositories have proper directory structure and documentation.
"""

import csv
import os
import sys
from pathlib import Path

print('🔧 Post-integration organization and README verification...')

# Load the filtered repositories
base_path = Path('../../../')
filtered_file = 'filtered_new_repos.csv'

if not os.path.exists(filtered_file):
    print('No new repositories to process')
    sys.exit(0)

with open(filtered_file, 'r') as f:
    reader = csv.DictReader(f)
    new_repos = list(reader)

if not new_repos:
    print('No repositories in filtered file')
    sys.exit(0)

print(f'Processing {len(new_repos)} repositories for organization...')

for repo in new_repos:
    repo_name = repo.get('name', '').replace('/', '_').replace('\\\\', '_')
    category = repo.get('category', 'Uncategorized')

    if not repo_name:
        continue

    # Create category directory
    category_dir = base_path / category.replace(' & ', '_').replace(' ', '_')
    category_dir.mkdir(exist_ok=True)

    # Create repository directory
    repo_dir = category_dir / repo_name
    repo_dir.mkdir(exist_ok=True)

    # Check if README exists, if not create it
    readme_path = repo_dir / 'README.md'
    if not readme_path.exists():
        print(f'Creating README for {repo_name}...')

        # Create comprehensive README
        readme_content = f'''# {repo.get('name', 'Unknown Repository')}

**Repository:** [{repo.get('name', 'Unknown')}]({repo.get('url', '')})
**Stars:** {repo.get('stars', 0):,} ⭐
**Category:** {category}
**Quality Score:** {repo.get('quality_score', 'N/A')}

## Description

{repo.get('description', 'No description available.')}

## 🔗 Links

- **Original Repository:** [{repo.get('url', '')}]({repo.get('url', '')})
- **Owner Profile:** [https://github.com/{repo.get('name', '').split('/')[0] if '/' in repo.get('name', '') else 'unknown'}](https://github.com/{repo.get('name', '').split('/')[0] if '/' in repo.get('name', '') else 'unknown'})

## 📊 Repository Statistics

- **Stars:** {repo.get('stars', 0):,}
- **Forks:** {repo.get('forks', 0):,}
- **Language:** {repo.get('language', 'Unknown')}
- **Last Updated:** {repo.get('updated_at', 'Unknown')}

## 🚀 Quick Start

1. Visit the [original repository]({repo.get('url', '')})
2. Read the project documentation
3. Clone or download the batch scripts
4. Review scripts before execution
5. Follow repository-specific installation instructions

## ⚠️ Safety Guidelines

- **Always review** batch scripts before running them
- **Test in a safe environment** first (VM recommended)
- **Understand the operations** each script performs
- **Backup your system** before running system modification scripts
- **Check antivirus** scan results for downloaded files

## 📄 License

This repository follows the license terms of the original project. Check the [original repository]({repo.get('url', '')}) for specific license information.

## 🤝 Contributing

To contribute to the original project:
1. Visit the [original repository]({repo.get('url', '')})
2. Read their contributing guidelines
3. Fork and submit pull requests to their repository

---

**Added to Collection:** {repo.get('discovery_date', 'Automated discovery')}
**Quality Score:** {repo.get('quality_score', 'N/A')}
**Auto-Generated:** This README was created by The Batch Compendium discovery system.

*Part of [The Batch Compendium](https://github.com/GhostwheeI/TheBatchCompendium) - A comprehensive collection of Windows batch scripts.*
'''

        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)

        print(f'✅ Created README for {repo_name}')
    else:
        print(f'ℹ️ README already exists for {repo_name}')

print('✅ Organization and README verification complete!')
