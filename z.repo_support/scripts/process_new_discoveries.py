#!/usr/bin/env python3
"""
Process new repository discoveries by filtering out duplicates and applying quality checks.

This script takes newly discovered repositories and compares them against the existing
collection to identify truly new repositories worth adding.
"""

import os
import sys
import csv
import argparse
from typing import List, Dict, Set, Optional
from datetime import datetime


class RepositoryProcessor:
    """Process and filter new repository discoveries."""
    
    def __init__(self, min_stars: int = 50):
        """
        Initialize the processor.
        
        Args:
            min_stars: Minimum star count for quality filtering
        """
        self.min_stars = min_stars
        self.quality_keywords = {
            'good': [
                'automation', 'optimization', 'performance', 'utility', 'tool',
                'script', 'batch', 'system', 'windows', 'admin', 'maintenance',
                'installer', 'manager', 'cleaner', 'tweaks', 'enhancement'
            ],
            'bad': [
                'test', 'example', 'demo', 'learning', 'tutorial', 'homework',
                'school', 'assignment', 'practice', 'sample', 'template'
            ]
        }
    
    def load_csv(self, filepath: str) -> List[Dict]:
        """Load repository data from CSV file."""
        repos = []
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Normalize star count
                    if 'stars' in row:
                        try:
                            row['stars'] = int(row['stars'])
                        except (ValueError, TypeError):
                            row['stars'] = 0
                    repos.append(row)
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
            # Create empty file with headers
            with open(filepath, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['name', 'url', 'description', 'stars', 'language'])
            return
        
        # Get all unique fieldnames
        fieldnames = set()
        for repo in repos:
            fieldnames.update(repo.keys())
        fieldnames = sorted(fieldnames)
        
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(repos)
    
    def get_repo_identifier(self, repo: Dict) -> str:
        """Get unique identifier for a repository."""
        name = repo.get('name', '').strip()
        url = repo.get('url', '').strip()
        
        # Use name if available, otherwise extract from URL
        if name:
            return name.lower()
        elif url:
            # Extract owner/repo from URL
            parts = url.rstrip('/').split('/')
            if len(parts) >= 2:
                return f"{parts[-2]}/{parts[-1]}".lower()
        
        return ''
    
    def find_duplicates(self, new_repos: List[Dict], existing_repos: List[Dict]) -> Set[str]:
        """Find repositories that already exist in the collection."""
        existing_ids = set()
        
        for repo in existing_repos:
            repo_id = self.get_repo_identifier(repo)
            if repo_id:
                existing_ids.add(repo_id)
        
        duplicates = set()
        for repo in new_repos:
            repo_id = self.get_repo_identifier(repo)
            if repo_id in existing_ids:
                duplicates.add(repo_id)
        
        return duplicates
    
    def quality_score(self, repo: Dict) -> float:
        """Calculate quality score for a repository."""
        score = 0.0
        
        # Star count (normalized to 0-1 scale, with 1000+ stars = 1.0)
        stars = repo.get('stars', 0)
        star_score = min(stars / 1000.0, 1.0)
        score += star_score * 0.4
        
        # Description quality
        description = repo.get('description', '').lower()
        if description:
            # Bonus for good keywords
            good_matches = sum(1 for keyword in self.quality_keywords['good'] 
                             if keyword in description)
            score += (good_matches / len(self.quality_keywords['good'])) * 0.3
            
            # Penalty for bad keywords  
            bad_matches = sum(1 for keyword in self.quality_keywords['bad']
                            if keyword in description)
            score -= (bad_matches / len(self.quality_keywords['bad'])) * 0.2
            
            # Bonus for having a description
            score += 0.1
        
        # Language bonus (if it's Batchfile)
        if repo.get('language', '').lower() == 'batchfile':
            score += 0.2
        
        # Recency bonus (if updated recently)
        updated_at = repo.get('updated_at', '')
        if updated_at:
            try:
                # Simple check if updated in last 2 years
                if '2023' in updated_at or '2024' in updated_at or '2025' in updated_at:
                    score += 0.1
            except:
                pass
        
        return max(0.0, min(1.0, score))
    
    def filter_by_quality(self, repos: List[Dict], min_quality: float = 0.3) -> List[Dict]:
        """Filter repositories by quality score."""
        filtered = []
        
        for repo in repos:
            quality = self.quality_score(repo)
            if quality >= min_quality:
                repo['quality_score'] = round(quality, 3)
                filtered.append(repo)
        
        return filtered
    
    def categorize_repository(self, repo: Dict) -> str:
        """Categorize a repository based on its description and properties."""
        description = repo.get('description', '').lower()
        name = repo.get('name', '').lower()
        
        # System & Performance
        if any(keyword in description + ' ' + name for keyword in 
               ['optimization', 'optimizer', 'performance', 'tweaks', 'debloat', 'cleaner', 'cleanup']):
            return 'System Tweaks & Performance Enhancements'
        
        # Security & Privacy
        if any(keyword in description + ' ' + name for keyword in
               ['security', 'privacy', 'hardening', 'defender', 'firewall', 'protection']):
            return 'Security & Privacy Tools'
        
        # Development & Scripting
        if any(keyword in description + ' ' + name for keyword in
               ['script', 'automation', 'build', 'deploy', 'development', 'dev', 'programming']):
            return 'Development & Scripting Tools'
        
        # File & Disk Operations
        if any(keyword in description + ' ' + name for keyword in
               ['file', 'disk', 'backup', 'sync', 'transfer', 'copy', 'move', 'archive']):
            return 'File & Disk Utilities'
        
        # System Information
        if any(keyword in description + ' ' + name for keyword in
               ['info', 'information', 'diagnostic', 'monitor', 'check', 'detect']):
            return 'System Information & Diagnostics'
        
        # Network & Internet
        if any(keyword in description + ' ' + name for keyword in
               ['network', 'internet', 'wifi', 'connection', 'dns', 'ip', 'web']):
            return 'Network & Internet Tools'
        
        # Audio/Video
        if any(keyword in description + ' ' + name for keyword in
               ['video', 'audio', 'media', 'ffmpeg', 'convert', 'encode', 'decode']):
            return 'Audio & Video Capture, Conversion & Playback'
        
        # Gaming
        if any(keyword in description + ' ' + name for keyword in
               ['game', 'gaming', 'steam', 'launcher', 'mod', 'server']):
            return 'Gaming & Entertainment Tools'
        
        # Process Management
        if any(keyword in description + ' ' + name for keyword in
               ['process', 'service', 'startup', 'task', 'schedule', 'daemon']):
            return 'Process, Service & Startup Management'
        
        return 'Uncategorized'
    
    def process_repositories(self, new_repos: List[Dict], existing_repos: List[Dict]) -> Dict:
        """Process new repositories and return analysis results."""
        print(f"Processing {len(new_repos)} new repositories against {len(existing_repos)} existing ones...")
        
        # Find duplicates
        duplicates = self.find_duplicates(new_repos, existing_repos)
        print(f"Found {len(duplicates)} duplicates")
        
        # Filter out duplicates
        unique_repos = []
        for repo in new_repos:
            repo_id = self.get_repo_identifier(repo)
            if repo_id not in duplicates:
                unique_repos.append(repo)
        
        print(f"After removing duplicates: {len(unique_repos)} repositories")
        
        # Apply quality filtering
        quality_repos = self.filter_by_quality(unique_repos)
        print(f"After quality filtering: {len(quality_repos)} repositories")
        
        # Add categories
        for repo in quality_repos:
            repo['category'] = self.categorize_repository(repo)
        
        # Sort by stars (descending)
        quality_repos.sort(key=lambda x: x.get('stars', 0), reverse=True)
        
        return {
            'total_discovered': len(new_repos),
            'duplicates_removed': len(duplicates),
            'unique_repos': len(unique_repos),
            'quality_filtered': len(quality_repos),
            'final_repos': quality_repos,
            'categories': self._get_category_stats(quality_repos)
        }
    
    def _get_category_stats(self, repos: List[Dict]) -> Dict[str, int]:
        """Get statistics about categories."""
        categories = {}
        for repo in repos:
            category = repo.get('category', 'Uncategorized')
            categories[category] = categories.get(category, 0) + 1
        return categories
    
    def generate_report(self, results: Dict) -> str:
        """Generate a text report of processing results."""
        report = f"""
Repository Discovery Processing Report
{'=' * 60}

Discovery Summary:
-----------------
Total Repositories Discovered: {results['total_discovered']}
Duplicates Removed: {results['duplicates_removed']}
Unique Repositories: {results['unique_repos']}
Quality Filtered (Final): {results['quality_filtered']}

Category Distribution:
---------------------
"""
        
        for category, count in sorted(results['categories'].items()):
            report += f"{category}: {count}\n"
        
        if results['final_repos']:
            report += f"\nTop New Repositories:\n"
            report += "-" * 30 + "\n"
            
            for i, repo in enumerate(results['final_repos'][:10], 1):
                name = repo.get('name', 'Unknown')
                stars = repo.get('stars', 0)
                category = repo.get('category', 'Uncategorized')
                quality = repo.get('quality_score', 0)
                description = repo.get('description', 'No description')[:60]
                
                report += f"{i:2d}. {name} ({stars:,} ⭐, Quality: {quality:.2f})\n"
                report += f"    Category: {category}\n"
                report += f"    {description}...\n\n"
        
        return report


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Process new repository discoveries"
    )
    parser.add_argument(
        "--new-repos",
        required=True,
        help="CSV file with newly discovered repositories"
    )
    parser.add_argument(
        "--existing-repos",
        required=True,
        help="CSV file with existing repository collection"
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output CSV file for filtered new repositories"
    )
    parser.add_argument(
        "--min-stars",
        type=int,
        default=50,
        help="Minimum star count (default: 50)"
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Generate and print processing report"
    )
    
    args = parser.parse_args()
    
    processor = RepositoryProcessor(min_stars=args.min_stars)
    
    # Load data
    new_repos = processor.load_csv(args.new_repos)
    existing_repos = processor.load_csv(args.existing_repos)
    
    if not new_repos:
        print("No new repositories to process.")
        # Create empty output file
        processor.save_csv([], args.output)
        return
    
    # Process repositories
    results = processor.process_repositories(new_repos, existing_repos)
    
    # Save filtered results
    processor.save_csv(results['final_repos'], args.output)
    print(f"\nSaved {len(results['final_repos'])} filtered repositories to {args.output}")
    
    # Generate report if requested
    if args.report:
        report = processor.generate_report(results)
        print(report)
        
        # Also save report to file
        report_file = args.output.replace('.csv', '_report.txt')
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"Report saved to {report_file}")


if __name__ == "__main__":
    main()