#!/usr/bin/env python3
"""
Update main collection documentation, statistics, and organization after adding new repositories.
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


class CollectionUpdater:
    """Update main collection documentation and statistics."""
    
    def __init__(self, base_path: str = "."):
        """
        Initialize the updater.
        
        Args:
            base_path: Base path of the repository collection
        """
        self.base_path = Path(base_path)
        self.scripts_path = self.base_path / "z.repo_support" / "scripts"
        self.main_csv = self.scripts_path / "repo_results.csv"
        self.main_readme = self.base_path / "README.md"
        
    def load_repositories(self) -> List[Dict]:
        """Load all repositories from the main CSV."""
        repos = []
        try:
            with open(self.main_csv, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Convert numeric fields
                    try:
                        row['stars'] = int(row['stars'])
                    except (ValueError, TypeError, KeyError):
                        row['stars'] = 0
                    repos.append(row)
        except FileNotFoundError:
            print(f"Warning: Main CSV not found: {self.main_csv}")
            return []
        except Exception as e:
            print(f"Error loading repositories: {e}")
            return []
        
        return repos
    
    def get_collection_statistics(self, repos: List[Dict]) -> Dict:
        """Generate comprehensive collection statistics."""
        if not repos:
            return {}
        
        total_repos = len(repos)
        total_stars = sum(r.get('stars', 0) for r in repos)
        avg_stars = total_stars / total_repos if total_repos > 0 else 0
        
        # Star distribution
        star_ranges = {
            'ultra_popular': len([r for r in repos if r.get('stars', 0) >= 10000]),
            'extremely_popular': len([r for r in repos if 5000 <= r.get('stars', 0) < 10000]),
            'very_popular': len([r for r in repos if 1000 <= r.get('stars', 0) < 5000]),
            'popular': len([r for r in repos if 500 <= r.get('stars', 0) < 1000]),
            'notable': len([r for r in repos if 100 <= r.get('stars', 0) < 500]),
            'recognized': len([r for r in repos if 50 <= r.get('stars', 0) < 100]),
            'emerging': len([r for r in repos if r.get('stars', 0) < 50])
        }
        
        # Category distribution
        categories = {}\n        for repo in repos:
            category = repo.get('category', 'Uncategorized')
            categories[category] = categories.get(category, 0) + 1
        
        # Top repositories
        top_repos = sorted(repos, key=lambda x: x.get('stars', 0), reverse=True)[:10]
        
        # Language distribution
        languages = {}
        for repo in repos:
            lang = repo.get('language', 'Unknown')
            languages[lang] = languages.get(lang, 0) + 1
        
        return {
            'total_repos': total_repos,
            'total_stars': total_stars,
            'avg_stars': avg_stars,
            'star_ranges': star_ranges,
            'categories': categories,
            'top_repos': top_repos,
            'languages': languages,
            'last_updated': datetime.now().isoformat()
        }
    
    def update_main_readme(self, stats: Dict) -> bool:
        """Update the main README.md with current statistics."""
        try:
            if not self.main_readme.exists():
                print(f"Warning: Main README not found: {self.main_readme}")
                return False
            
            # Read current README
            with open(self.main_readme, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Update statistics section
            stats_section = self._generate_stats_section(stats)
            
            # Find and replace statistics section
            # Look for a section marker like <!-- STATS_START --> ... <!-- STATS_END -->
            start_marker = "<!-- STATS_START -->"
            end_marker = "<!-- STATS_END -->"
            
            if start_marker in content and end_marker in content:
                start_idx = content.find(start_marker)
                end_idx = content.find(end_marker) + len(end_marker)
                
                new_content = (
                    content[:start_idx] + 
                    start_marker + "\\n" + stats_section + "\\n" + end_marker +
                    content[end_idx:]
                )
            else:
                # If markers don't exist, append stats at the end
                new_content = content + "\\n\\n" + start_marker + "\\n" + stats_section + "\\n" + end_marker
            
            # Write updated README
            with open(self.main_readme, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"Updated main README: {self.main_readme}")
            return True
            
        except Exception as e:
            print(f"Error updating main README: {e}")
            return False
    
    def _generate_stats_section(self, stats: Dict) -> str:
        """Generate the statistics section for README."""
        total_repos = stats.get('total_repos', 0)
        total_stars = stats.get('total_stars', 0)
        avg_stars = stats.get('avg_stars', 0)
        star_ranges = stats.get('star_ranges', {})
        categories = stats.get('categories', {})
        
        # Top categories
        top_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)[:5]
        
        section = f"""
## 📊 Collection Statistics

- **Total Repositories:** {total_repos:,}
- **Total Stars:** {total_stars:,}
- **Average Stars:** {avg_stars:.0f}
- **Last Updated:** {datetime.now().strftime('%B %d, %Y')}

### Repository Distribution by Stars
- 🌟 **Ultra-Popular (10,000+ stars):** {star_ranges.get('ultra_popular', 0)}
- ⭐ **Extremely Popular (5,000+ stars):** {star_ranges.get('extremely_popular', 0)}
- ✨ **Very Popular (1,000+ stars):** {star_ranges.get('very_popular', 0)}
- 🔥 **Popular (500+ stars):** {star_ranges.get('popular', 0)}
- 👍 **Notable (100+ stars):** {star_ranges.get('notable', 0)}
- 📈 **Recognized (50+ stars):** {star_ranges.get('recognized', 0)}

### Top Categories"""
        
        for category, count in top_categories:
            section += f"\\n- **{category}:** {count} repositories"
        
        return section
    
    def generate_category_index(self, repos: List[Dict]) -> str:
        """Generate a category index document."""
        categories = {}
        for repo in repos:
            category = repo.get('category', 'Uncategorized')
            if category not in categories:
                categories[category] = []
            categories[category].append(repo)
        
        # Sort categories by repository count
        sorted_categories = sorted(categories.items(), key=lambda x: len(x[1]), reverse=True)
        
        index = f"""# Repository Categories Index

This document provides an organized view of all repositories in The Batch Compendium by category.

**Last Updated:** {datetime.now().strftime('%B %d, %Y')}  
**Total Categories:** {len(categories)}  
**Total Repositories:** {sum(len(repos) for repos in categories.values())}

---

"""
        
        for category, category_repos in sorted_categories:
            # Sort repositories within category by stars
            category_repos.sort(key=lambda x: x.get('stars', 0), reverse=True)
            
            index += f"## {category} ({len(category_repos)} repositories)\\n\\n"
            
            for repo in category_repos:
                name = repo.get('name', 'Unknown')
                url = repo.get('url', '')
                stars = repo.get('stars', 0)
                description = repo.get('description', 'No description')[:100]
                
                index += f"- **[{name}]({url})** ({stars:,} ⭐)\\n"
                index += f"  {description}...\\n\\n"
        
        return index
    
    def update_category_documentation(self, repos: List[Dict]):
        """Update category-based documentation."""
        try:
            # Generate category index
            category_index = self.generate_category_index(repos)
            
            # Save category index
            category_file = self.scripts_path / "CATEGORY_INDEX.md"
            with open(category_file, 'w', encoding='utf-8') as f:
                f.write(category_index)
            
            print(f"Updated category index: {category_file}")
            
        except Exception as e:
            print(f"Error updating category documentation: {e}")
    
    def run_script_count_update(self) -> bool:
        """Run the script count update script."""
        try:
            update_script = self.scripts_path / "update_script_count.sh"
            if not update_script.exists():
                print(f"Warning: Script count updater not found: {update_script}")
                return False
            
            # Change to base directory and run the script
            original_cwd = os.getcwd()
            os.chdir(self.base_path)
            
            result = subprocess.run(['bash', str(update_script)], 
                                 capture_output=True, text=True, check=True)
            
            print("Script count updated successfully")
            if result.stdout:
                print(result.stdout.strip())
            
            os.chdir(original_cwd)
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"Error running script count update: {e}")
            if e.stderr:
                print(f"Error output: {e.stderr}")
            return False
        except Exception as e:
            print(f"Error updating script count: {e}")
            return False
        finally:
            if 'original_cwd' in locals():
                os.chdir(original_cwd)
    
    def save_statistics_json(self, stats: Dict):
        """Save detailed statistics to JSON file."""
        try:
            stats_file = self.scripts_path / "collection_stats.json"
            with open(stats_file, 'w', encoding='utf-8') as f:
                json.dump(stats, f, indent=2, default=str)
            
            print(f"Statistics saved to: {stats_file}")
            
        except Exception as e:
            print(f"Error saving statistics JSON: {e}")
    
    def generate_update_report(self, stats: Dict, new_repos_count: int = 0) -> str:
        """Generate an update report."""
        report = f"""
Collection Update Report
{'=' * 50}

Update Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}
New Repositories Added: {new_repos_count}

Current Collection Status:
-------------------------
Total Repositories: {stats.get('total_repos', 0):,}
Total Stars: {stats.get('total_stars', 0):,}
Average Stars: {stats.get('avg_stars', 0):.1f}

Star Distribution:
-----------------"""
        
        star_ranges = stats.get('star_ranges', {})
        for range_name, count in star_ranges.items():
            display_name = range_name.replace('_', ' ').title()
            report += f"\\n{display_name}: {count}"
        
        report += f"""

Top Categories:
--------------"""
        
        categories = stats.get('categories', {})
        top_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)[:10]
        
        for category, count in top_categories:
            report += f"\\n{category}: {count} repositories"
        
        report += f"""

Files Updated:
-------------
- Main repository CSV ({self.main_csv})
- Main README.md statistics
- Category index documentation
- Collection statistics JSON
- Script count badges

Next Steps:
----------
1. Review new repository integrations
2. Verify categorization accuracy
3. Check for any manual curation needed
4. Update any category-specific documentation
5. Consider featuring top new repositories

---
Collection update completed successfully!
"""
        
        return report
    
    def update_collection(self, new_repos_count: int = 0) -> Dict:
        """Main collection update process."""
        print("Starting collection update process...")
        
        # Load current repositories
        repos = self.load_repositories()
        if not repos:
            return {"success": False, "message": "No repositories loaded"}
        
        print(f"Loaded {len(repos)} repositories from collection")
        
        # Generate statistics
        stats = self.get_collection_statistics(repos)
        
        # Update main README
        readme_updated = self.update_main_readme(stats)
        
        # Update category documentation
        self.update_category_documentation(repos)
        
        # Run script count update
        script_count_updated = self.run_script_count_update()
        
        # Save detailed statistics
        self.save_statistics_json(stats)
        
        # Generate update report
        report = self.generate_update_report(stats, new_repos_count)
        
        # Save report
        report_file = self.scripts_path / f"update_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(report)
        print(f"Update report saved to: {report_file}")
        
        return {
            "success": True,
            "repositories_processed": len(repos),
            "readme_updated": readme_updated,
            "script_count_updated": script_count_updated,
            "statistics": stats,
            "report_file": str(report_file)
        }


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Update main collection documentation and statistics"
    )
    parser.add_argument(
        "--base-path",
        default="../../..",
        help="Base path of the repository collection (default: ../../..)"
    )
    parser.add_argument(
        "--new-repos-count",
        type=int,
        default=0,
        help="Number of new repositories added (for reporting)"
    )
    parser.add_argument(
        "--generate-report-only",
        action="store_true",
        help="Only generate statistics report without updating files"
    )
    
    args = parser.parse_args()
    
    updater = CollectionUpdater(base_path=args.base_path)
    
    if args.generate_report_only:
        # Just generate and display statistics
        repos = updater.load_repositories()
        if repos:
            stats = updater.get_collection_statistics(repos)
            report = updater.generate_update_report(stats, args.new_repos_count)
            print(report)
        else:
            print("No repositories found for reporting")
    else:
        # Perform full update
        result = updater.update_collection(args.new_repos_count)
        
        if result["success"]:
            print(f"\\n✅ Collection update completed successfully!")
            print(f"   Processed: {result['repositories_processed']} repositories")
        else:
            print(f"\\n❌ Collection update failed: {result.get('message', 'Unknown error')}")
            sys.exit(1)


if __name__ == "__main__":
    main()