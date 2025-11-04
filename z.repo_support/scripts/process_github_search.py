#!/usr/bin/env python3
"""
Process GitHub search results to identify highly rated batch repositories.
This script can be used with data from GitHub search API.
"""

import json
import csv
import sys
import argparse
from typing import List, Dict


def process_github_search_results(data: Dict) -> List[Dict]:
    """
    Process GitHub search API response and extract relevant repository information.
    
    Args:
        data: GitHub search API response JSON
        
    Returns:
        List of processed repository dictionaries
    """
    repos = []
    
    if 'items' not in data:
        print("Warning: No 'items' key in data", file=sys.stderr)
        return repos
    
    for item in data['items']:
        repo = {
            'name': item.get('full_name', ''),
            'url': item.get('html_url', ''),
            'description': (item.get('description') or '').strip().replace('\n', ' '),
            'stars': item.get('stargazers_count', 0),
            'forks': item.get('forks_count', 0),
            'language': item.get('language', ''),
            'created_at': item.get('created_at', ''),
            'updated_at': item.get('updated_at', ''),
            'topics': ','.join(item.get('topics', [])),
            'archived': item.get('archived', False)
        }
        repos.append(repo)
    
    return repos


def filter_repos(repos: List[Dict], min_stars: int = 100, exclude_archived: bool = True) -> List[Dict]:
    """
    Filter repositories based on criteria.
    
    Args:
        repos: List of repository dictionaries
        min_stars: Minimum star count
        exclude_archived: Whether to exclude archived repos
        
    Returns:
        Filtered list of repositories
    """
    filtered = []
    
    for repo in repos:
        # Skip if below minimum stars
        if repo.get('stars', 0) < min_stars:
            continue
        
        # Skip if archived and we're excluding them
        if exclude_archived and repo.get('archived', False):
            continue
        
        filtered.append(repo)
    
    return filtered


def save_to_csv(repos: List[Dict], output_file: str):
    """
    Save repository list to CSV file.
    
    Args:
        repos: List of repository dictionaries
        output_file: Output CSV file path
    """
    if not repos:
        print("No repositories to save.")
        return
    
    fieldnames = ['name', 'url', 'description', 'stars', 'forks', 'language', 
                  'created_at', 'updated_at', 'topics', 'archived']
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(repos)
    
    print(f"Saved {len(repos)} repositories to {output_file}")


def generate_report(repos: List[Dict]) -> str:
    """
    Generate a text report of the repositories.
    
    Args:
        repos: List of repository dictionaries
        
    Returns:
        Report text
    """
    if not repos:
        return "No repositories found."
    
    total = len(repos)
    total_stars = sum(r.get('stars', 0) for r in repos)
    avg_stars = total_stars / total if total > 0 else 0
    
    # Categorize by stars
    highly_popular = [r for r in repos if r.get('stars', 0) >= 1000]
    popular = [r for r in repos if 100 <= r.get('stars', 0) < 1000]
    notable = [r for r in repos if 50 <= r.get('stars', 0) < 100]
    
    report = f"""
GitHub Batch Repository Search Results
{'=' * 60}

Total Repositories Found: {total}
Total Stars: {total_stars:,}
Average Stars: {avg_stars:.1f}

Star Distribution:
------------------
Highly Popular (1000+ stars): {len(highly_popular)}
Popular (100-999 stars): {len(popular)}
Notable (50-99 stars): {len(notable)}

Top 20 Repositories by Stars:
------------------------------
"""
    
    # Sort by stars
    sorted_repos = sorted(repos, key=lambda x: x.get('stars', 0), reverse=True)
    
    for i, repo in enumerate(sorted_repos[:20], 1):
        name = repo.get('name', 'Unknown')
        stars = repo.get('stars', 0)
        desc = repo.get('description', 'No description')[:70]
        url = repo.get('url', '')
        report += f"{i:2d}. {name} ({stars:,} ⭐)\n"
        report += f"    {desc}...\n"
        report += f"    {url}\n\n"
    
    return report


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Process GitHub search results for batch repositories"
    )
    parser.add_argument(
        "input_file",
        help="Input JSON file from GitHub search API"
    )
    parser.add_argument(
        "--min-stars",
        type=int,
        default=100,
        help="Minimum star count (default: 100)"
    )
    parser.add_argument(
        "--output",
        help="Output CSV file"
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Generate and print analysis report"
    )
    parser.add_argument(
        "--include-archived",
        action="store_true",
        help="Include archived repositories"
    )
    
    args = parser.parse_args()
    
    # Read JSON input
    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found: {args.input_file}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        sys.exit(1)
    
    # Process the data
    repos = process_github_search_results(data)
    print(f"Processed {len(repos)} repositories from search results")
    
    # Filter repos
    filtered_repos = filter_repos(
        repos, 
        min_stars=args.min_stars,
        exclude_archived=not args.include_archived
    )
    print(f"After filtering (>= {args.min_stars} stars): {len(filtered_repos)} repositories")
    
    # Generate report if requested
    if args.report:
        report = generate_report(filtered_repos)
        print(report)
    
    # Save to CSV if output file specified
    if args.output:
        save_to_csv(filtered_repos, args.output)


if __name__ == "__main__":
    main()
