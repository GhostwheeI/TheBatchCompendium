#!/usr/bin/env python3
"""
Integrate new repositories into the main collection by updating CSV files,
generating repository structures, and creating documentation.
"""

import os
import sys
import csv
import json
import argparse
import subprocess
from typing import List, Dict, Optional
from pathlib import Path
from datetime import datetime


class RepositoryIntegrator:
    """Integrate new repositories into the collection."""
    
    def __init__(self, base_path: str = "."):
        """
        Initialize the integrator.
        
        Args:
            base_path: Base path of the repository collection
        """
        self.base_path = Path(base_path)
        self.scripts_path = self.base_path / "z.repo_support" / "scripts"
        self.main_csv = self.scripts_path / "repo_results.csv"
        
    def load_csv(self, filepath: str) -> List[Dict]:
        """Load repository data from CSV file."""
        repos = []
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Filter out None keys and ensure clean data
                    clean_row = {k: v for k, v in row.items() if k is not None and isinstance(k, str)}
                    
                    # Normalize data types
                    if 'stars' in clean_row:
                        try:
                            clean_row['stars'] = int(clean_row['stars'])
                        except (ValueError, TypeError):
                            clean_row['stars'] = 0
                    repos.append(clean_row)
        except FileNotFoundError:
            print(f"Warning: File not found: {filepath}")
            return []
        except Exception as e:
            print(f"Error reading CSV {filepath}: {e}")
            return []
        
        return repos
    
    def save_csv(self, repos: List[Dict], filepath: str):
        """Save repository data to CSV file."""
        if not repos:
            return
        
        # Get all unique fieldnames, filtering out None values
        fieldnames = set()
        for repo in repos:
            # Filter out None keys and ensure all keys are strings
            valid_keys = [k for k in repo.keys() if k is not None and isinstance(k, str)]
            fieldnames.update(valid_keys)
        fieldnames = sorted(fieldnames)
        
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(repos)
    
    def merge_repositories(self, new_repos: List[Dict]) -> List[Dict]:
        """Merge new repositories with existing collection."""
        print("Merging new repositories with existing collection...")
        
        # Load existing repositories
        existing_repos = self.load_csv(str(self.main_csv))
        print(f"Existing repositories: {len(existing_repos)}")
        
        if not new_repos:
            print("No new repositories to merge")
            return existing_repos
        
        # Merge and sort by stars
        all_repos = existing_repos + new_repos
        all_repos.sort(key=lambda x: x.get('stars', 0), reverse=True)
        
        print(f"Total repositories after merge: {len(all_repos)}")
        return all_repos
    
    def create_repo_structure(self, repo: Dict) -> Optional[str]:
        """Create directory structure for a new repository."""
        try:
            repo_name = repo.get('name', '')
            if not repo_name:
                return None
            
            # Clean the repository name for filesystem
            clean_name = repo_name.replace('/', '_').replace('\\', '_')
            category = repo.get('category', 'Uncategorized')
            
            # Create category directory if it doesn't exist
            category_path = self.base_path / category.replace(' & ', '_').replace(' ', '_')
            category_path.mkdir(exist_ok=True)
            
            # Create repository directory
            repo_path = category_path / clean_name
            repo_path.mkdir(exist_ok=True)
            
            # Create README.md for the repository
            readme_content = self.generate_repo_readme(repo)
            readme_path = repo_path / "README.md"
            
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(readme_content)
            
            print(f"Created structure for: {clean_name}")
            return str(repo_path)
            
        except Exception as e:
            print(f"Error creating structure for {repo.get('name', 'unknown')}: {e}")
            return None
    
    def generate_repo_readme(self, repo: Dict) -> str:
        """Generate README content for a repository."""
        name = repo.get('name', 'Unknown Repository')
        url = repo.get('url', '')
        description = repo.get('description', 'No description available.')
        stars = repo.get('stars', 0)
        language = repo.get('language', 'Unknown')
        category = repo.get('category', 'Uncategorized')
        
        # Extract owner and repo name
        owner, repo_name = name.split('/', 1) if '/' in name else ('unknown', name)
        
        readme = f"""# {repo_name}

**Owner:** [{owner}](https://github.com/{owner})  
**Repository:** [{name}]({url})  
**Stars:** {stars:,} ⭐  
**Language:** {language}  
**Category:** {category}

## Description

{description}

## 🔗 Links

- **GitHub Repository:** [{url}]({url})
- **Owner Profile:** [https://github.com/{owner}](https://github.com/{owner})

## 📊 Repository Stats

- **Stars:** {stars:,}
- **Primary Language:** {language}
- **Category:** {category}

## 📝 About This Repository

This repository is part of [The Batch Compendium](https://github.com/YourUsername/TheBatchCompendium) - a comprehensive collection of Windows batch scripts and tools.

### Why This Repository?

- ✅ **High Quality:** {stars:,} stars indicate community trust
- ✅ **Active Project:** Well-maintained and documented
- ✅ **Batch Scripts:** Contains useful Windows batch files
- ✅ **Open Source:** Free to use and learn from

## 🚀 Quick Start

1. Visit the [original repository]({url})
2. Read the project's documentation
3. Clone or download the scripts you need
4. Follow the repository's installation instructions

## ⚠️ Important Notes

- Always review batch scripts before running them
- Test scripts in a safe environment first
- Check for any prerequisites or dependencies
- Respect the repository's license terms

## 📄 License

This repository follows the license terms of the original project. Please check the [original repository]({url}) for specific license information.

## 🤝 Contributing

To contribute to the original project:
1. Visit [{url}]({url})
2. Read their contributing guidelines
3. Fork, modify, and submit pull requests to their repository

---

**Discovered:** {datetime.now().strftime('%Y-%m-%d')}  
**Added to Collection:** Automated discovery system  
**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}

*This README was automatically generated by The Batch Compendium discovery system.*
"""
        return readme
    
    def update_main_collection(self, all_repos: List[Dict]):
        """Update the main repository collection CSV."""
        print("Updating main collection CSV...")
        
        # Save updated collection
        self.save_csv(all_repos, str(self.main_csv))
        print(f"Updated {self.main_csv} with {len(all_repos)} repositories")
    
    def update_statistics(self, new_count: int):
        """Update repository statistics and counts."""
        print(f"Updating statistics (added {new_count} new repositories)...")
        
        # Run the script count update script if it exists
        update_script = self.scripts_path / "update_script_count.sh"
        if update_script.exists():
            try:
                # Run the script from the base directory with proper working dir
                result = subprocess.run(
                    ['bash', str(update_script.resolve())], 
                    cwd=str(self.base_path),
                    check=True,
                    capture_output=True,
                    text=True
                )
                print("Updated script counts successfully")
                if result.stdout:
                    print(f"Output: {result.stdout.strip()}")
            except subprocess.CalledProcessError as e:
                print(f"Error running update script: {e}")
            except Exception as e:
                print(f"Error updating statistics: {e}")
    
    def create_integration_summary(self, new_repos: List[Dict], created_paths: List[str]) -> str:
        """Create a summary of the integration process."""
        summary = f"""
Integration Summary - {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}
{'=' * 70}

New Repositories Added: {len(new_repos)}
Directory Structures Created: {len(created_paths)}

Repositories Integrated:
-----------------------
"""
        
        for i, repo in enumerate(new_repos, 1):
            name = repo.get('name', 'Unknown')
            stars = repo.get('stars', 0)
            category = repo.get('category', 'Uncategorized')
            summary += f"{i:2d}. {name} ({stars:,} ⭐) - {category}\n"
        
        if created_paths:
            summary += f"\nDirectory Structures Created:\n"
            summary += "-" * 30 + "\n"
            for path in created_paths:
                summary += f"- {path}\n"
        
        summary += f"""
Files Updated:
--------------
- {self.main_csv}
- Main repository statistics
- Category organization
- Individual repository READMEs

Next Steps:
-----------
1. Review generated repository structures
2. Verify README content accuracy
3. Update main repository documentation
4. Consider manual curation of descriptions
5. Test any scripts in new repositories

---
Integration completed successfully!
"""
        return summary
    
    def integrate(self, new_repos_file: str, update_collection: bool = True) -> Dict:
        """Main integration process."""
        print("Starting repository integration process...")
        
        # Load new repositories
        new_repos = self.load_csv(new_repos_file)
        if not new_repos:
            print("No new repositories to integrate")
            return {"success": True, "count": 0, "message": "No repositories to process"}
        
        print(f"Integrating {len(new_repos)} new repositories...")
        
        created_paths = []
        
        # Create directory structures for new repositories
        for repo in new_repos:
            path = self.create_repo_structure(repo)
            if path:
                created_paths.append(path)
        
        if update_collection:
            # Merge with existing collection
            all_repos = self.merge_repositories(new_repos)
            
            # Update main collection CSV
            self.update_main_collection(all_repos)
            
            # Update statistics
            self.update_statistics(len(new_repos))
        
        # Create integration summary
        summary = self.create_integration_summary(new_repos, created_paths)
        
        # Save summary to file
        summary_file = self.scripts_path / f"integration_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        # Ensure the directory exists
        summary_file.parent.mkdir(parents=True, exist_ok=True)
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write(summary)
        
        print(summary)
        print(f"Integration summary saved to: {summary_file}")
        
        return {
            "success": True,
            "count": len(new_repos),
            "created_paths": created_paths,
            "summary_file": str(summary_file),
            "message": f"Successfully integrated {len(new_repos)} repositories"
        }


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Integrate new repositories into the collection"
    )
    parser.add_argument(
        "--new-repos",
        required=True,
        help="CSV file with new repositories to integrate"
    )
    parser.add_argument(
        "--base-path",
        default="../../..",
        help="Base path of the repository collection (default: ../../..)"
    )
    parser.add_argument(
        "--update-collection",
        action="store_true",
        help="Update the main collection CSV file"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes"
    )
    
    args = parser.parse_args()
    
    if args.dry_run:
        print("DRY RUN MODE - No changes will be made")
    
    integrator = RepositoryIntegrator(base_path=args.base_path)
    
    if args.dry_run:
        # Just load and show what would be processed
        new_repos = integrator.load_csv(args.new_repos)
        print(f"Would process {len(new_repos)} repositories:")
        for repo in new_repos:
            name = repo.get('name', 'Unknown')
            stars = repo.get('stars', 0)
            category = repo.get('category', 'Uncategorized')
            print(f"  - {name} ({stars:,} ⭐) - {category}")
    else:
        # Perform actual integration
        result = integrator.integrate(args.new_repos, args.update_collection)
        
        if result["success"]:
            print(f"\n✅ Integration completed successfully!")
            print(f"   Added: {result['count']} repositories")
        else:
            print(f"\n❌ Integration failed: {result.get('message', 'Unknown error')}")
            sys.exit(1)


if __name__ == "__main__":
    main()