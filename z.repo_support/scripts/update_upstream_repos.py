#!/usr/bin/env python3
"""
Update and refresh batch scripts from their upstream repositories.
This script fetches the latest versions of scripts from their original GitHub sources.
"""

import os
import sys
import csv
import json
import argparse
import subprocess
import tempfile
import shutil
from typing import List, Dict, Optional, Tuple
from pathlib import Path
from datetime import datetime

try:
    import requests
except ImportError:
    print("Error: requests library not found. Install with: pip install requests")
    sys.exit(1)


class UpstreamUpdater:
    """Update repositories and scripts from their upstream sources."""
    
    # Configuration constants
    GIT_CLONE_TIMEOUT_SECONDS = 300  # 5 minute timeout for git clone operations
    UPDATE_THRESHOLD_DAYS = 30  # Update repositories older than this many days
    
    def __init__(self, base_path: str = ".", github_token: Optional[str] = None):
        """
        Initialize the upstream updater.
        
        Args:
            base_path: Base path of the repository collection
            github_token: GitHub API token for authenticated requests
        """
        self.base_path = Path(base_path)
        self.scripts_path = self.base_path / "z.repo_support" / "scripts"
        self.main_csv = self.scripts_path / "repo_results.csv"
        self.github_token = github_token
        self.headers = {
            "Accept": "application/vnd.github.v3+json"
        }
        if github_token:
            self.headers["Authorization"] = f"token {github_token}"
        
        self.stats = {
            'checked': 0,
            'updated': 0,
            'unchanged': 0,
            'errors': 0,
            'skipped': 0
        }
    
    def load_repositories(self) -> List[Dict]:
        """Load repository list from CSV."""
        repos = []
        try:
            with open(self.main_csv, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row.get('name') and row.get('url'):
                        repos.append(row)
        except FileNotFoundError:
            print(f"Warning: Repository CSV not found: {self.main_csv}")
            return []
        except Exception as e:
            print(f"Error reading repository CSV: {e}")
            return []
        
        return repos
    
    def get_repo_info(self, repo_name: str) -> Optional[Dict]:
        """
        Get repository information from GitHub API.
        
        Args:
            repo_name: Full repository name (owner/repo)
            
        Returns:
            Repository information dictionary or None on error
        """
        url = f"https://api.github.com/repos/{repo_name}"
        
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching repo info for {repo_name}: {e}")
            return None
    
    def get_repo_last_commit(self, repo_name: str) -> Optional[Dict]:
        """
        Get the last commit information for a repository.
        
        Args:
            repo_name: Full repository name (owner/repo)
            
        Returns:
            Commit information dictionary or None on error
        """
        url = f"https://api.github.com/repos/{repo_name}/commits/HEAD"
        
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching commit info for {repo_name}: {e}")
            return None
    
    def clone_or_update_repo(self, repo: Dict, target_dir: Path) -> Tuple[bool, str]:
        """
        Clone or update a repository to the target directory.
        
        Args:
            repo: Repository information dictionary
            target_dir: Target directory path
            
        Returns:
            Tuple of (success, message)
        """
        repo_url = repo.get('url', '')
        repo_name = repo.get('name', '')
        
        if not repo_url or not repo_name:
            return False, "Missing repository URL or name"
        
        # Create a temporary directory for cloning
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            clone_path = temp_path / "repo"
            
            try:
                # Clone the repository with shallow depth
                print(f"  Cloning {repo_name}...")
                result = subprocess.run(
                    ['git', 'clone', '--depth', '1', repo_url, str(clone_path)],
                    capture_output=True,
                    text=True,
                    timeout=self.GIT_CLONE_TIMEOUT_SECONDS
                )
                
                if result.returncode != 0:
                    return False, f"Git clone failed: {result.stderr}"
                
                # Remove existing target directory if it exists
                if target_dir.exists():
                    shutil.rmtree(target_dir)
                
                # Create target directory
                target_dir.mkdir(parents=True, exist_ok=True)
                
                # Copy files (excluding .git directory)
                for item in clone_path.iterdir():
                    if item.name != '.git':
                        if item.is_dir():
                            shutil.copytree(item, target_dir / item.name)
                        else:
                            shutil.copy2(item, target_dir / item.name)
                
                # Create or update metadata file
                metadata = {
                    'repository': repo_name,
                    'url': repo_url,
                    'last_updated': datetime.now().isoformat(),
                    'stars': repo.get('stars', 0),
                    'description': repo.get('description', '')
                }
                
                metadata_file = target_dir / '.upstream_metadata.json'
                with open(metadata_file, 'w', encoding='utf-8') as f:
                    json.dump(metadata, f, indent=2)
                
                return True, "Successfully updated"
                
            except subprocess.TimeoutExpired:
                return False, "Clone operation timed out"
            except Exception as e:
                return False, f"Error during update: {str(e)}"
    
    def get_repo_directory(self, repo: Dict) -> Optional[Path]:
        """
        Get the directory path for a repository in the collection.
        
        Args:
            repo: Repository information dictionary
            
        Returns:
            Path to repository directory or None if not found
        """
        repo_name = repo.get('name', '').replace('/', '_').replace('\\', '_')
        category = repo.get('category', 'Uncategorized')
        
        if not repo_name:
            return None
        
        # Try to find the repository directory
        category_dir = self.base_path / category.replace(' & ', '_').replace(' ', '_')
        repo_dir = category_dir / repo_name
        
        if repo_dir.exists():
            return repo_dir
        
        # Search in all category directories if not found
        for cat_dir in self.base_path.iterdir():
            if cat_dir.is_dir() and not cat_dir.name.startswith('.'):
                potential_repo_dir = cat_dir / repo_name
                if potential_repo_dir.exists():
                    return potential_repo_dir
        
        return None
    
    def should_update_repo(self, repo: Dict, repo_dir: Path) -> Tuple[bool, str]:
        """
        Determine if a repository should be updated.
        
        Args:
            repo: Repository information dictionary
            repo_dir: Repository directory path
            
        Returns:
            Tuple of (should_update, reason)
        """
        metadata_file = repo_dir / '.upstream_metadata.json'
        
        # Update if no metadata exists
        if not metadata_file.exists():
            return True, "No metadata found - initial update"
        
        try:
            with open(metadata_file, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
            
            # Check last update time (update if older than UPDATE_THRESHOLD_DAYS)
            last_updated = datetime.fromisoformat(metadata.get('last_updated', '2000-01-01'))
            days_since_update = (datetime.now() - last_updated).days
            
            if days_since_update > self.UPDATE_THRESHOLD_DAYS:
                return True, f"Last updated {days_since_update} days ago"
            
            # Check if repository information has changed
            repo_name = repo.get('name', '')
            if repo_name:
                repo_info = self.get_repo_info(repo_name)
                if repo_info:
                    # Check if there are new commits
                    last_commit = self.get_repo_last_commit(repo_name)
                    if last_commit:
                        try:
                            commit_date_str = last_commit['commit']['committer']['date']
                            # Handle different date formats.
                            # Note: Replacing 'Z' with '+00:00' is required for Python 3.6–3.10,
                            # where datetime.fromisoformat() does not accept a 'Z' suffix.
                            if commit_date_str.endswith('Z'):
                                commit_date_str = commit_date_str[:-1] + '+00:00'
                            commit_date = datetime.fromisoformat(commit_date_str)
                            if commit_date > last_updated:
                                return True, f"New commits available since last update"
                        except (KeyError, ValueError, TypeError) as e:
                            print(f"  Warning: Could not parse commit date: {e}")
                            return True, f"Could not verify commit date ({type(e).__name__}: {e}) - updating to be safe"
            
            return False, "Repository is up to date"
            
        except Exception as e:
            print(f"  Warning: Error checking update status: {e}")
            return True, "Error checking status - updating to be safe"
    
    def update_repositories(self, repos: Optional[List[Dict]] = None, 
                           force: bool = False, limit: Optional[int] = None) -> Dict:
        """
        Update repositories from their upstream sources.
        
        Args:
            repos: List of repositories to update (None = all)
            force: Force update even if not needed
            limit: Maximum number of repositories to update
            
        Returns:
            Statistics dictionary
        """
        if repos is None:
            repos = self.load_repositories()
        
        if not repos:
            print("No repositories to update")
            return self.stats
        
        if limit:
            repos = repos[:limit]
            print(f"Limiting update to first {limit} repositories")
        
        print(f"\n{'='*60}")
        print(f"Updating {len(repos)} repositories from upstream sources")
        print(f"{'='*60}\n")
        
        for i, repo in enumerate(repos, 1):
            repo_name = repo.get('name', 'unknown')
            print(f"\n[{i}/{len(repos)}] Processing: {repo_name}")
            
            self.stats['checked'] += 1
            
            # Get repository directory
            repo_dir = self.get_repo_directory(repo)
            
            if not repo_dir:
                print(f"  ⏭️  Skipped - repository directory not found")
                self.stats['skipped'] += 1
                continue
            
            # Check if update is needed
            if not force:
                should_update, reason = self.should_update_repo(repo, repo_dir)
                if not should_update:
                    print(f"  ✓ Up to date - {reason}")
                    self.stats['unchanged'] += 1
                    continue
                else:
                    print(f"  → Update needed: {reason}")
            else:
                print(f"  → Forced update")
            
            # Update the repository
            success, message = self.clone_or_update_repo(repo, repo_dir)
            
            if success:
                print(f"  ✅ {message}")
                self.stats['updated'] += 1
            else:
                print(f"  ❌ {message}")
                self.stats['errors'] += 1
        
        return self.stats
    
    def print_summary(self):
        """Print update summary."""
        print(f"\n{'='*60}")
        print(f"Update Summary")
        print(f"{'='*60}")
        print(f"  Repositories Checked: {self.stats['checked']}")
        print(f"  Successfully Updated: {self.stats['updated']}")
        print(f"  Already Up to Date:   {self.stats['unchanged']}")
        print(f"  Skipped:              {self.stats['skipped']}")
        print(f"  Errors:               {self.stats['errors']}")
        print(f"{'='*60}\n")


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Update batch repositories from their upstream sources"
    )
    parser.add_argument(
        '--base-path',
        default='../..',
        help='Base path of the repository collection (default: ../..)'
    )
    parser.add_argument(
        '--github-token',
        help='GitHub API token (or set GITHUB_TOKEN env var)',
        default=os.environ.get('GITHUB_TOKEN')
    )
    parser.add_argument(
        '--force',
        action='store_true',
        help='Force update all repositories even if they appear up to date'
    )
    parser.add_argument(
        '--limit',
        type=int,
        help='Limit number of repositories to update (for testing)'
    )
    parser.add_argument(
        '--repos',
        nargs='+',
        help='Specific repositories to update (owner/repo format)'
    )
    
    args = parser.parse_args()
    
    if not args.github_token:
        print("Warning: No GitHub token provided. API rate limits will be lower.")
        print("Set GITHUB_TOKEN environment variable or use --github-token option.\n")
    
    updater = UpstreamUpdater(
        base_path=args.base_path,
        github_token=args.github_token
    )
    
    # Load repositories
    all_repos = updater.load_repositories()
    
    # Filter to specific repositories if requested
    if args.repos:
        repos_to_update = [
            repo for repo in all_repos
            if repo.get('name') in args.repos
        ]
        if not repos_to_update:
            print(f"Error: None of the specified repositories found")
            sys.exit(1)
        print(f"Updating {len(repos_to_update)} specified repositories")
    else:
        repos_to_update = all_repos
    
    # Update repositories
    stats = updater.update_repositories(
        repos=repos_to_update,
        force=args.force,
        limit=args.limit
    )
    
    # Print summary
    updater.print_summary()
    
    # Exit with error code if there were errors
    if stats['errors'] > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
