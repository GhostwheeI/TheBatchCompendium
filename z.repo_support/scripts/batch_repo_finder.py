#!/usr/bin/env python3
"""
Script to identify highly rated GitHub repositories hosting Windows batch-based solutions.

This is a standalone script that can be integrated with GitHub search APIs or
used to analyze and filter existing repository lists.
"""

import csv
import argparse
import sys
from typing import List, Dict, Set


class BatchRepoAnalyzer:
    """Analyze and filter batch script repositories."""
    
    def __init__(self, min_stars: int = 10):
        """
        Initialize the analyzer.
        
        Args:
            min_stars: Minimum star count to consider a repo
        """
        self.min_stars = min_stars
    
    def load_csv(self, filepath: str) -> List[Dict]:
        """
        Load repository data from CSV file.
        
        Args:
            filepath: Path to CSV file
            
        Returns:
            List of repository dictionaries
        """
        repos = []
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Convert stars to integer if present
                    if 'stars' in row:
                        try:
                            row['stars'] = int(row['stars'])
                        except (ValueError, TypeError):
                            row['stars'] = 0
                    repos.append(row)
        except FileNotFoundError:
            print(f"Error: File not found: {filepath}")
            return []
        except Exception as e:
            print(f"Error reading CSV: {e}")
            return []
        
        return repos
    
    def filter_by_stars(self, repos: List[Dict]) -> List[Dict]:
        """
        Filter repositories by minimum star count.
        
        Args:
            repos: List of repository dictionaries
            
        Returns:
            Filtered list of repositories
        """
        return [r for r in repos if r.get('stars', 0) >= self.min_stars]
    
    def remove_duplicates(self, repos: List[Dict]) -> List[Dict]:
        """
        Remove duplicate repositories based on name or URL.
        
        Args:
            repos: List of repository dictionaries
            
        Returns:
            List with duplicates removed
        """
        seen: Set[str] = set()
        unique_repos = []
        
        for repo in repos:
            # Use name or url as unique identifier
            identifier = repo.get('name', repo.get('url', ''))
            if identifier and identifier not in seen:
                seen.add(identifier)
                unique_repos.append(repo)
        
        return unique_repos
    
    def sort_by_stars(self, repos: List[Dict], descending: bool = True) -> List[Dict]:
        """
        Sort repositories by star count.
        
        Args:
            repos: List of repository dictionaries
            descending: Sort in descending order (default: True)
            
        Returns:
            Sorted list of repositories
        """
        return sorted(repos, key=lambda x: x.get('stars', 0), reverse=descending)
    
    def categorize_by_stars(self, repos: List[Dict]) -> Dict[str, List[Dict]]:
        """
        Categorize repositories by star ranges.
        
        Args:
            repos: List of repository dictionaries
            
        Returns:
            Dictionary with categories as keys
        """
        categories = {
            'highly_popular': [],  # 1000+ stars
            'popular': [],         # 100-999 stars
            'notable': [],         # 50-99 stars
            'active': [],          # 10-49 stars
            'emerging': []         # < 10 stars
        }
        
        for repo in repos:
            stars = repo.get('stars', 0)
            if stars >= 1000:
                categories['highly_popular'].append(repo)
            elif stars >= 100:
                categories['popular'].append(repo)
            elif stars >= 50:
                categories['notable'].append(repo)
            elif stars >= 10:
                categories['active'].append(repo)
            else:
                categories['emerging'].append(repo)
        
        return categories
    
    def generate_report(self, repos: List[Dict]) -> str:
        """
        Generate a text report of repository statistics.
        
        Args:
            repos: List of repository dictionaries
            
        Returns:
            Report text
        """
        if not repos:
            return "No repositories to analyze."
        
        categories = self.categorize_by_stars(repos)
        total = len(repos)
        total_stars = sum(r.get('stars', 0) for r in repos)
        avg_stars = total_stars / total if total > 0 else 0
        
        report = f"""
Repository Analysis Report
{'=' * 50}

Total Repositories: {total}
Total Stars: {total_stars:,}
Average Stars: {avg_stars:.1f}

Star Distribution:
------------------
Highly Popular (1000+ stars): {len(categories['highly_popular'])}
Popular (100-999 stars): {len(categories['popular'])}
Notable (50-99 stars): {len(categories['notable'])}
Active (10-49 stars): {len(categories['active'])}
Emerging (< 10 stars): {len(categories['emerging'])}

Top 10 Repositories by Stars:
------------------------------
"""
        
        top_repos = self.sort_by_stars(repos)[:10]
        for i, repo in enumerate(top_repos, 1):
            name = repo.get('name', 'Unknown')
            stars = repo.get('stars', 0)
            desc = repo.get('description', 'No description')[:60]
            report += f"{i:2d}. {name} ({stars:,} stars)\n    {desc}...\n"
        
        return report
    
    def save_filtered_csv(self, repos: List[Dict], output_file: str):
        """
        Save filtered repository list to CSV.
        
        Args:
            repos: List of repository dictionaries
            output_file: Output CSV file path
        """
        if not repos:
            print("No repositories to save.")
            return
        
        # Get all unique fieldnames from repos
        fieldnames = set()
        for repo in repos:
            fieldnames.update(repo.keys())
        fieldnames = sorted(fieldnames)
        
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(repos)
        
        print(f"Saved {len(repos)} repositories to {output_file}")


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Analyze and filter batch script repositories"
    )
    parser.add_argument(
        "input_file",
        help="Input CSV file with repository data"
    )
    parser.add_argument(
        "--min-stars",
        type=int,
        default=10,
        help="Minimum star count (default: 10)"
    )
    parser.add_argument(
        "--output",
        help="Output CSV file for filtered results"
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Generate analysis report"
    )
    
    args = parser.parse_args()
    
    analyzer = BatchRepoAnalyzer(min_stars=args.min_stars)
    
    print(f"Loading repositories from {args.input_file}...")
    repos = analyzer.load_csv(args.input_file)
    
    if not repos:
        print("No repositories loaded.")
        sys.exit(1)
    
    print(f"Loaded {len(repos)} repositories")
    
    # Remove duplicates
    repos = analyzer.remove_duplicates(repos)
    print(f"After removing duplicates: {len(repos)} repositories")
    
    # Filter by stars
    filtered_repos = analyzer.filter_by_stars(repos)
    print(f"Repositories with >= {args.min_stars} stars: {len(filtered_repos)}")
    
    # Sort by stars
    filtered_repos = analyzer.sort_by_stars(filtered_repos)
    
    # Generate report if requested
    if args.report:
        report = analyzer.generate_report(filtered_repos)
        print(report)
    
    # Save filtered results if output file specified
    if args.output:
        analyzer.save_filtered_csv(filtered_repos, args.output)


if __name__ == "__main__":
    main()
