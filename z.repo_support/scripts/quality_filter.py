#!/usr/bin/env python3
"""
Advanced quality filtering system for batch script repositories.
This module provides comprehensive quality assessment and filtering.
"""

import re
import os
import csv
import json
import argparse
from typing import List, Dict, Set, Tuple, Optional
from datetime import datetime, timedelta
from urllib.parse import urlparse


class RepositoryQualityFilter:
    """Comprehensive quality filtering for batch script repositories."""
    
    def __init__(self):
        """Initialize the quality filter with predefined criteria."""
        
        # Quality keywords for descriptions
        self.quality_keywords = {
            'excellent': [
                'automation', 'optimization', 'professional', 'enterprise',
                'production', 'robust', 'comprehensive', 'advanced'
            ],
            'good': [
                'utility', 'tool', 'script', 'batch', 'system', 'windows',
                'admin', 'maintenance', 'installer', 'manager', 'cleaner',
                'tweaks', 'enhancement', 'performance', 'security'
            ],
            'neutral': [
                'simple', 'basic', 'easy', 'quick', 'fast', 'small'
            ],
            'warning': [
                'test', 'example', 'demo', 'learning', 'tutorial',
                'homework', 'school', 'assignment', 'practice'
            ],
            'bad': [
                'broken', 'deprecated', 'abandoned', 'outdated',
                'experimental', 'unstable', 'beta', 'alpha'
            ]
        }
        
        # Suspicious patterns in repository names or descriptions
        self.suspicious_patterns = [
            r'crack', r'hack', r'illegal', r'pirate', r'warez',
            r'keygen', r'serial', r'patch', r'virus', r'malware',
            r'trojan', r'backdoor', r'payload'
        ]
        
        # High-quality indicators
        self.quality_indicators = {
            'has_license': 0.1,
            'has_readme': 0.1,
            'has_releases': 0.05,
            'recent_activity': 0.15,
            'good_description': 0.1,
            'high_stars': 0.2,
            'good_keywords': 0.1,
            'active_maintainer': 0.1,
            'clear_purpose': 0.1
        }
        
        # Minimum thresholds
        self.min_thresholds = {
            'stars': 10,
            'quality_score': 0.3,
            'description_length': 20
        }
    
    def calculate_quality_score(self, repo: Dict) -> float:
        """Calculate comprehensive quality score for a repository."""
        score = 0.0
        factors = {}
        
        # Star count factor (normalized)
        stars = repo.get('stars', 0)
        if stars >= 10000:
            star_factor = 1.0
        elif stars >= 1000:
            star_factor = 0.8
        elif stars >= 100:
            star_factor = 0.6
        elif stars >= 50:
            star_factor = 0.4
        elif stars >= 10:
            star_factor = 0.2
        else:
            star_factor = 0.0
        
        score += star_factor * self.quality_indicators['high_stars']
        factors['star_factor'] = star_factor
        
        # Description quality
        description = repo.get('description', '').lower()
        desc_factor = self._evaluate_description_quality(description)
        score += desc_factor * self.quality_indicators['good_description']
        factors['description_factor'] = desc_factor
        
        # Language bonus
        if repo.get('language', '').lower() == 'batchfile':
            score += 0.1
            factors['language_bonus'] = True
        
        # Activity recency
        activity_factor = self._evaluate_activity_recency(repo)
        score += activity_factor * self.quality_indicators['recent_activity']
        factors['activity_factor'] = activity_factor
        
        # Repository name quality
        name_factor = self._evaluate_name_quality(repo.get('name', ''))
        score += name_factor * 0.05
        factors['name_factor'] = name_factor
        
        # Fork ratio (original projects preferred)
        fork_factor = self._evaluate_fork_ratio(repo)
        score += fork_factor * 0.05
        factors['fork_factor'] = fork_factor
        
        # Suspicious content penalty
        suspicious_penalty = self._check_suspicious_content(repo)
        score -= suspicious_penalty
        factors['suspicious_penalty'] = suspicious_penalty
        
        # Normalize score to 0-1 range
        final_score = max(0.0, min(1.0, score))
        
        return final_score, factors
    
    def _evaluate_description_quality(self, description: str) -> float:
        """Evaluate the quality of repository description."""
        if not description:
            return 0.0
        
        score = 0.0
        
        # Length bonus (good descriptions are descriptive)
        if len(description) >= 50:
            score += 0.3
        elif len(description) >= 20:
            score += 0.1
        
        # Keyword analysis
        excellent_matches = sum(1 for word in self.quality_keywords['excellent'] 
                              if word in description)
        good_matches = sum(1 for word in self.quality_keywords['good'] 
                         if word in description)
        warning_matches = sum(1 for word in self.quality_keywords['warning'] 
                            if word in description)
        bad_matches = sum(1 for word in self.quality_keywords['bad'] 
                        if word in description)
        
        # Apply keyword scoring
        score += excellent_matches * 0.15
        score += good_matches * 0.1
        score -= warning_matches * 0.1
        score -= bad_matches * 0.2
        
        # Grammar and structure bonus
        if '.' in description and len(description.split()) >= 5:
            score += 0.1
        
        # Clear purpose indicators
        purpose_words = ['for', 'to', 'helps', 'provides', 'enables', 'allows']
        if any(word in description for word in purpose_words):
            score += 0.1
        
        return max(0.0, min(1.0, score))
    
    def _evaluate_activity_recency(self, repo: Dict) -> float:
        """Evaluate repository activity recency."""
        updated_at = repo.get('updated_at', '')
        if not updated_at:
            return 0.0
        
        try:
            # Simple year-based evaluation
            current_year = datetime.now().year
            
            if str(current_year) in updated_at:
                return 1.0  # This year
            elif str(current_year - 1) in updated_at:
                return 0.8  # Last year
            elif str(current_year - 2) in updated_at:
                return 0.5  # 2 years ago
            elif str(current_year - 3) in updated_at:
                return 0.3  # 3 years ago
            else:
                return 0.1  # Older
                
        except Exception:
            return 0.0
    
    def _evaluate_name_quality(self, name: str) -> float:
        """Evaluate repository name quality."""
        if not name:
            return 0.0
        
        score = 0.0
        name_lower = name.lower()
        
        # Meaningful name bonus
        if len(name.split('/')) == 2:  # owner/repo format
            repo_name = name.split('/')[1].lower()
            
            # Good naming patterns
            if any(word in repo_name for word in ['batch', 'script', 'tool', 'util']):
                score += 0.3
            
            # Avoid generic names
            generic_names = ['test', 'example', 'demo', 'temp', 'new', 'untitled']
            if any(generic in repo_name for generic in generic_names):
                score -= 0.2
            
            # Professional naming (hyphens, clear structure)
            if '-' in repo_name or '_' in repo_name:
                score += 0.1
        
        return max(0.0, min(1.0, score))
    
    def _evaluate_fork_ratio(self, repo: Dict) -> float:
        """Evaluate fork to star ratio (prefer original projects)."""
        stars = repo.get('stars', 0)
        forks = repo.get('forks', 0)
        
        if stars == 0:
            return 0.0
        
        fork_ratio = forks / stars
        
        # Optimal fork ratio is around 0.1-0.3 (active but not just forks)
        if 0.05 <= fork_ratio <= 0.4:
            return 1.0
        elif fork_ratio < 0.05:
            return 0.7  # Might be less collaborative
        else:
            return 0.5  # High fork ratio might indicate issues
    
    def _check_suspicious_content(self, repo: Dict) -> float:
        """Check for suspicious or problematic content."""
        penalty = 0.0
        
        name = repo.get('name', '').lower()
        description = repo.get('description', '').lower()
        combined_text = f"{name} {description}"
        
        # Check for suspicious patterns
        for pattern in self.suspicious_patterns:
            if re.search(pattern, combined_text, re.IGNORECASE):
                penalty += 0.3
        
        # Check for specific problematic indicators
        problematic_terms = [
            'activation', 'activator', 'crack', 'license bypass',
            'illegal', 'pirated', 'stolen', 'virus', 'malware'
        ]
        
        for term in problematic_terms:
            if term in combined_text:
                penalty += 0.2
        
        return min(penalty, 0.8)  # Cap penalty at 0.8
    
    def categorize_by_quality(self, repos: List[Dict]) -> Dict[str, List[Dict]]:
        """Categorize repositories by quality tiers."""
        categories = {
            'excellent': [],      # 0.8+
            'high_quality': [],   # 0.6-0.79
            'good': [],          # 0.4-0.59
            'acceptable': [],    # 0.3-0.39
            'questionable': [],  # 0.2-0.29
            'poor': []           # <0.2
        }
        
        for repo in repos:
            score, factors = self.calculate_quality_score(repo)
            repo['quality_score'] = round(score, 3)
            repo['quality_factors'] = factors
            
            if score >= 0.8:
                categories['excellent'].append(repo)
            elif score >= 0.6:
                categories['high_quality'].append(repo)
            elif score >= 0.4:
                categories['good'].append(repo)
            elif score >= 0.3:
                categories['acceptable'].append(repo)
            elif score >= 0.2:
                categories['questionable'].append(repo)
            else:
                categories['poor'].append(repo)
        
        return categories
    
    def filter_repositories(self, repos: List[Dict], 
                          min_quality: float = 0.3,
                          min_stars: int = 10,
                          exclude_suspicious: bool = True) -> List[Dict]:
        """Filter repositories based on quality criteria."""
        filtered = []
        
        for repo in repos:
            # Calculate quality score
            score, factors = self.calculate_quality_score(repo)
            repo['quality_score'] = round(score, 3)
            repo['quality_factors'] = factors
            
            # Apply filters
            if score < min_quality:
                continue
            
            if repo.get('stars', 0) < min_stars:
                continue
            
            if exclude_suspicious and factors.get('suspicious_penalty', 0) > 0.3:
                continue
            
            # Description length check
            description = repo.get('description', '')
            if len(description) < self.min_thresholds['description_length']:
                continue
            
            filtered.append(repo)
        
        return filtered
    
    def generate_quality_report(self, repos: List[Dict]) -> str:
        """Generate a detailed quality analysis report."""
        if not repos:
            return "No repositories to analyze."
        
        categories = self.categorize_by_quality(repos)
        total_repos = len(repos)
        
        # Calculate statistics
        scores = [r.get('quality_score', 0) for r in repos]
        avg_score = sum(scores) / len(scores) if scores else 0
        
        report = f"""
Repository Quality Analysis Report
{'=' * 60}

Total Repositories Analyzed: {total_repos}
Average Quality Score: {avg_score:.3f}

Quality Distribution:
--------------------
Excellent (0.8+):     {len(categories['excellent']):3d} ({len(categories['excellent'])/total_repos*100:.1f}%)
High Quality (0.6+):  {len(categories['high_quality']):3d} ({len(categories['high_quality'])/total_repos*100:.1f}%)
Good (0.4+):          {len(categories['good']):3d} ({len(categories['good'])/total_repos*100:.1f}%)
Acceptable (0.3+):    {len(categories['acceptable']):3d} ({len(categories['acceptable'])/total_repos*100:.1f}%)
Questionable (0.2+):  {len(categories['questionable']):3d} ({len(categories['questionable'])/total_repos*100:.1f}%)
Poor (<0.2):          {len(categories['poor']):3d} ({len(categories['poor'])/total_repos*100:.1f}%)

Recommended for Collection: {len(categories['excellent']) + len(categories['high_quality']) + len(categories['good'])}

Top Quality Repositories:
------------------------
"""
        
        # Show top 10 by quality score
        top_repos = sorted(repos, key=lambda x: x.get('quality_score', 0), reverse=True)[:10]
        
        for i, repo in enumerate(top_repos, 1):
            name = repo.get('name', 'Unknown')
            score = repo.get('quality_score', 0)
            stars = repo.get('stars', 0)
            description = repo.get('description', 'No description')[:60]
            
            report += f"{i:2d}. {name} (Score: {score:.3f}, Stars: {stars:,})\n"
            report += f"    {description}...\n\n"
        
        # Quality factors analysis
        report += self._generate_factors_analysis(repos)
        
        return report
    
    def _generate_factors_analysis(self, repos: List[Dict]) -> str:
        """Generate analysis of quality factors."""
        if not repos:
            return ""
        
        # Analyze common quality factors
        high_star_count = len([r for r in repos if r.get('stars', 0) >= 1000])
        good_descriptions = len([r for r in repos if len(r.get('description', '')) >= 50])
        recent_updates = len([r for r in repos if '2024' in r.get('updated_at', '') or '2025' in r.get('updated_at', '')])
        suspicious_repos = len([r for r in repos if r.get('quality_factors', {}).get('suspicious_penalty', 0) > 0])
        
        analysis = f"""
Quality Factors Analysis:
------------------------
High Star Count (1000+):     {high_star_count} repositories
Good Descriptions (50+ chars): {good_descriptions} repositories  
Recent Updates (2024-2025):   {recent_updates} repositories
Suspicious Content Detected:  {suspicious_repos} repositories

Recommendations:
---------------
- Focus on repositories with scores 0.4+ for quality collection
- Manual review recommended for scores 0.3-0.4 range
- Avoid repositories with suspicious content penalties
- Prefer repositories with recent activity (last 2 years)
- Prioritize repositories with clear, descriptive names

Quality Improvement Suggestions:
-------------------------------
- Filter minimum star count to 50+ for better quality
- Require descriptions of at least 30 characters
- Exclude repositories not updated in 3+ years
- Manual review of activation/licensing tools for legitimacy
"""
        
        return analysis
    
    def save_quality_analysis(self, repos: List[Dict], output_file: str):
        """Save detailed quality analysis to JSON file."""
        analysis = {
            'timestamp': datetime.now().isoformat(),
            'total_repositories': len(repos),
            'quality_categories': {},
            'statistics': {},
            'repositories': []
        }
        
        # Categorize repositories
        categories = self.categorize_by_quality(repos)
        for category, category_repos in categories.items():
            analysis['quality_categories'][category] = {
                'count': len(category_repos),
                'percentage': len(category_repos) / len(repos) * 100 if repos else 0
            }
        
        # Calculate statistics
        scores = [r.get('quality_score', 0) for r in repos]
        analysis['statistics'] = {
            'average_score': sum(scores) / len(scores) if scores else 0,
            'median_score': sorted(scores)[len(scores)//2] if scores else 0,
            'min_score': min(scores) if scores else 0,
            'max_score': max(scores) if scores else 0
        }
        
        # Add repository details
        for repo in repos:
            repo_analysis = {
                'name': repo.get('name'),
                'stars': repo.get('stars'),
                'quality_score': repo.get('quality_score'),
                'quality_factors': repo.get('quality_factors'),
                'category': repo.get('category'),
                'description_length': len(repo.get('description', ''))
            }
            analysis['repositories'].append(repo_analysis)
        
        # Save to file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(analysis, f, indent=2, default=str)


def main():
    """Main function for command-line usage."""
    parser = argparse.ArgumentParser(
        description="Quality filtering system for batch repositories"
    )
    parser.add_argument(
        "input_file",
        help="Input CSV file with repository data"
    )
    parser.add_argument(
        "--output",
        help="Output CSV file for filtered repositories"
    )
    parser.add_argument(
        "--min-quality",
        type=float,
        default=0.3,
        help="Minimum quality score (0-1, default: 0.3)"
    )
    parser.add_argument(
        "--min-stars",
        type=int,
        default=10,
        help="Minimum star count (default: 10)"
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Generate quality analysis report"
    )
    parser.add_argument(
        "--analysis-json",
        help="Save detailed analysis to JSON file"
    )
    parser.add_argument(
        "--exclude-suspicious",
        action="store_true",
        help="Exclude repositories with suspicious content"
    )
    
    args = parser.parse_args()
    
    # Load repositories
    repos = []
    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    row['stars'] = int(row['stars'])
                except (ValueError, TypeError):
                    row['stars'] = 0
                repos.append(row)
    except FileNotFoundError:
        print(f"Error: File not found: {args.input_file}")
        return
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return
    
    if not repos:
        print("No repositories loaded.")
        return
    
    print(f"Loaded {len(repos)} repositories for quality analysis")
    
    # Initialize quality filter
    quality_filter = RepositoryQualityFilter()
    
    # Generate report if requested
    if args.report:
        report = quality_filter.generate_quality_report(repos)
        print(report)
    
    # Save detailed analysis if requested
    if args.analysis_json:
        quality_filter.save_quality_analysis(repos, args.analysis_json)
        print(f"Detailed analysis saved to: {args.analysis_json}")
    
    # Filter repositories
    if args.output:
        filtered_repos = quality_filter.filter_repositories(
            repos,
            min_quality=args.min_quality,
            min_stars=args.min_stars,
            exclude_suspicious=args.exclude_suspicious
        )
        
        print(f"Filtered to {len(filtered_repos)} high-quality repositories")
        
        # Save filtered results
        if filtered_repos:
            fieldnames = list(filtered_repos[0].keys())
            with open(args.output, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(filtered_repos)
            
            print(f"Filtered repositories saved to: {args.output}")
        else:
            print("No repositories passed the quality filters")


if __name__ == "__main__":
    main()