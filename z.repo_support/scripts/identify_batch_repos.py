#!/usr/bin/env python3
"""
Script to identify highly rated GitHub repositories hosting Windows batch-based solutions.

This script searches GitHub for repositories containing batch scripts (.bat, .cmd files)
and filters them by star count to identify popular and well-maintained projects.
"""

import os
import sys
import csv
import time
import argparse
from typing import List, Dict, Optional
from datetime import datetime

try:
    import requests
except ImportError:
    print("Error: requests library not found. Install with: pip install requests")
    sys.exit(1)


class BatchRepoFinder:
    """Find and analyze GitHub repositories containing batch scripts."""
    
    def __init__(self, token: Optional[str] = None, min_stars: int = 10):
        """
        Initialize the finder.
        
        Args:
            token: GitHub API token (optional but recommended for higher rate limits)
            min_stars: Minimum star count to consider a repo
        """
        self.token = token
        self.min_stars = min_stars
        self.base_url = "https://api.github.com"
        self.headers = {
            "Accept": "application/vnd.github.v3+json"
        }
        if token:
            self.headers["Authorization"] = f"token {token}"
    
    def search_repos(self, query: str, max_results: int = 100) -> List[Dict]:
        """
        Search GitHub for repositories matching the query.
        
        Args:
            query: GitHub search query
            max_results: Maximum number of results to return
            
        Returns:
            List of repository dictionaries
        """
        repos = []
        page = 1
        per_page = 100  # GitHub API max per page
        
        while len(repos) < max_results:
            url = f"{self.base_url}/search/repositories"
            params = {
                "q": query,
                "sort": "stars",
                "order": "desc",
                "per_page": per_page,
                "page": page
            }
            
            try:
                response = requests.get(url, headers=self.headers, params=params)
                response.raise_for_status()
                data = response.json()
                
                if not data.get("items"):
                    break
                
                repos.extend(data["items"])
                
                # Check rate limit
                remaining = int(response.headers.get("X-RateLimit-Remaining", 0))
                if remaining < 5:
                    reset_time = int(response.headers.get("X-RateLimit-Reset", 0))
                    wait_time = reset_time - time.time()
                    if wait_time > 0:
                        print(f"Rate limit approaching. Waiting {int(wait_time)} seconds...")
                        time.sleep(wait_time + 1)
                
                if len(data["items"]) < per_page:
                    break
                
                page += 1
                time.sleep(1)  # Be nice to the API
                
            except requests.exceptions.RequestException as e:
                print(f"Error searching repositories: {e}")
                break
        
        return repos[:max_results]
    
    def get_repo_languages(self, repo_full_name: str) -> Dict:
        """
        Get language statistics for a repository.
        
        Args:
            repo_full_name: Full repository name (owner/repo)
            
        Returns:
            Dictionary of language statistics
        """
        url = f"{self.base_url}/repos/{repo_full_name}/languages"
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return {}
    
    def find_batch_repos(self, max_results: int = 100) -> List[Dict]:
        """
        Find repositories with batch scripts.
        
        Args:
            max_results: Maximum number of results
            
        Returns:
            List of filtered repository information
        """
        # Search queries to find batch script repositories
        queries = [
            f"batch script stars:>={self.min_stars} language:Batchfile",
            f"windows batch stars:>={self.min_stars}",
            f".bat OR .cmd stars:>={self.min_stars} language:Batchfile",
        ]
        
        all_repos = []
        seen_names = set()
        
        for query in queries:
            print(f"Searching with query: {query}")
            repos = self.search_repos(query, max_results=max_results)
            
            for repo in repos:
                full_name = repo.get("full_name", "")
                
                # Skip duplicates
                if full_name in seen_names:
                    continue
                
                seen_names.add(full_name)
                
                # Filter by star count
                stars = repo.get("stargazers_count", 0)
                if stars < self.min_stars:
                    continue
                
                # Extract relevant information
                repo_info = {
                    "name": full_name,
                    "url": repo.get("html_url", ""),
                    "description": (repo.get("description") or "").strip(),
                    "stars": stars,
                    "forks": repo.get("forks_count", 0),
                    "language": repo.get("language", ""),
                    "created_at": repo.get("created_at", ""),
                    "updated_at": repo.get("updated_at", ""),
                }
                
                all_repos.append(repo_info)
                print(f"Found: {full_name} ({stars} stars)")
            
            time.sleep(2)  # Rate limit consideration
        
        # Sort by stars (descending)
        all_repos.sort(key=lambda x: x["stars"], reverse=True)
        
        return all_repos
    
    def save_to_csv(self, repos: List[Dict], output_file: str):
        """
        Save repository information to CSV file.
        
        Args:
            repos: List of repository dictionaries
            output_file: Output CSV file path
        """
        if not repos:
            print("No repositories to save.")
            return
        
        fieldnames = ["name", "url", "description", "stars", "forks", "language", "created_at", "updated_at"]
        
        with open(output_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(repos)
        
        print(f"\nSaved {len(repos)} repositories to {output_file}")


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Identify highly rated GitHub repositories with Windows batch scripts"
    )
    parser.add_argument(
        "--token",
        help="GitHub API token (optional but recommended for higher rate limits)",
        default=os.environ.get("GITHUB_TOKEN")
    )
    parser.add_argument(
        "--min-stars",
        type=int,
        default=10,
        help="Minimum star count (default: 10)"
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=100,
        help="Maximum number of results (default: 100)"
    )
    parser.add_argument(
        "--output",
        default="batch_repos_found.csv",
        help="Output CSV file (default: batch_repos_found.csv)"
    )
    
    args = parser.parse_args()
    
    if not args.token:
        print("Warning: No GitHub token provided. API rate limits will be lower.")
        print("Set GITHUB_TOKEN environment variable or use --token option.")
        print()
    
    finder = BatchRepoFinder(token=args.token, min_stars=args.min_stars)
    
    print(f"Searching for batch script repositories with at least {args.min_stars} stars...")
    print()
    
    repos = finder.find_batch_repos(max_results=args.max_results)
    
    if repos:
        finder.save_to_csv(repos, args.output)
        print(f"\nFound {len(repos)} highly-rated batch script repositories!")
        print(f"\nTop 5 repositories by stars:")
        for i, repo in enumerate(repos[:5], 1):
            print(f"{i}. {repo['name']} - {repo['stars']} stars")
    else:
        print("No repositories found matching the criteria.")


if __name__ == "__main__":
    main()
