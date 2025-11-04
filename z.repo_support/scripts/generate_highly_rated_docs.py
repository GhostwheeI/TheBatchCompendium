#!/usr/bin/env python3
"""
Generate and update the HIGHLY_RATED_REPOS.md documentation based on current collection.
"""

import os
import csv
import argparse
from typing import List, Dict
from datetime import datetime


class HighlyRatedDocsGenerator:
    """Generate documentation for highly rated repositories."""
    
    def __init__(self):
        """Initialize the generator."""
        self.star_tiers = [
            (100000, "Ultra-Popular (100,000+ stars)"),
            (50000, "Mega-Popular (50,000+ stars)"),
            (10000, "Extremely Popular (10,000+ stars)"),
            (5000, "Very Popular (5,000+ stars)"),
            (3000, "Very Popular (3,000+ stars)"),
            (1000, "Popular (1,000+ stars)"),
            (500, "Notable (500+ stars)"),
            (100, "Recognized (100+ stars)")
        ]
    
    def load_repositories(self, csv_file: str) -> List[Dict]:
        """Load repository data from CSV."""
        repos = []
        try:
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Convert stars to integer
                    try:
                        row['stars'] = int(row['stars'])
                    except (ValueError, TypeError):
                        row['stars'] = 0
                    repos.append(row)
        except FileNotFoundError:
            print(f"Error: File not found: {csv_file}")
            return []
        except Exception as e:
            print(f"Error reading CSV: {e}")
            return []
        
        return repos
    
    def categorize_by_stars(self, repos: List[Dict]) -> Dict[str, List[Dict]]:
        """Categorize repositories by star count."""
        categories = {}
        
        # Initialize categories
        for _, category_name in self.star_tiers:
            categories[category_name] = []
        
        # Sort repos by stars (descending)
        sorted_repos = sorted(repos, key=lambda x: x.get('stars', 0), reverse=True)
        
        # Categorize repos
        for repo in sorted_repos:
            stars = repo.get('stars', 0)
            categorized = False
            
            for min_stars, category_name in self.star_tiers:
                if stars >= min_stars:
                    categories[category_name].append(repo)
                    categorized = True
                    break
            
            if not categorized and stars >= 50:  # Catch remaining repos with 50+ stars
                if "Other Notable (50+ stars)" not in categories:
                    categories["Other Notable (50+ stars)"] = []
                categories["Other Notable (50+ stars)"].append(repo)
        
        # Remove empty categories
        return {k: v for k, v in categories.items() if v}
    
    def get_statistics(self, repos: List[Dict]) -> Dict:
        """Get repository statistics."""
        if not repos:
            return {}
        
        total_repos = len(repos)
        total_stars = sum(r.get('stars', 0) for r in repos)
        avg_stars = total_stars / total_repos if total_repos > 0 else 0
        
        # Count by star ranges
        star_ranges = {
            'ultra_popular': len([r for r in repos if r.get('stars', 0) >= 10000]),
            'very_popular': len([r for r in repos if 1000 <= r.get('stars', 0) < 10000]),
            'popular': len([r for r in repos if 100 <= r.get('stars', 0) < 1000]),
            'notable': len([r for r in repos if 50 <= r.get('stars', 0) < 100])
        }
        
        # Most common categories
        categories = {}
        for repo in repos:
            category = repo.get('category', 'Uncategorized')
            categories[category] = categories.get(category, 0) + 1
        
        # Top categories
        top_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)[:5]
        
        return {
            'total_repos': total_repos,
            'total_stars': total_stars,
            'avg_stars': avg_stars,
            'star_ranges': star_ranges,
            'top_categories': top_categories
        }
    
    def format_repo_entry(self, repo: Dict, index: int) -> str:
        """Format a single repository entry."""
        name = repo.get('name', 'Unknown')
        url = repo.get('url', '')
        description = repo.get('description', 'No description available.')
        stars = repo.get('stars', 0)
        category = repo.get('category', '')
        
        # Clean up the description
        description = description.strip().replace('\n', ' ')
        if len(description) > 150:
            description = description[:147] + "..."
        
        entry = f"{index}. **[{name}]({url})** ⭐ {stars:,}\n"
        entry += f"   - {description}\n"
        
        if category and category != 'Uncategorized':
            entry += f"   - Category: {category}\n"
        
        return entry + "\n"
    
    def generate_markdown(self, repos: List[Dict]) -> str:
        """Generate the complete markdown documentation."""
        stats = self.get_statistics(repos)
        categories = self.categorize_by_stars(repos)
        
        # Filter to only show repos with 100+ stars for the main list
        high_star_repos = [r for r in repos if r.get('stars', 0) >= 100]
        
        markdown = f"""# Highly Rated Windows Batch Repositories on GitHub

This document lists highly-rated Windows batch script repositories discovered through GitHub search, sorted by star count.

> **Last Updated:** {datetime.now().strftime('%B %d, %Y')}  
> **Criteria:** Repositories with significant batch script content and 100+ stars  
> **Total Repositories:** {stats.get('total_repos', 0):,}

---

## 📊 Collection Statistics

- **Total Repositories:** {stats.get('total_repos', 0):,}
- **Total Stars:** {stats.get('total_stars', 0):,}
- **Average Stars:** {stats.get('avg_stars', 0):.0f}

### Star Distribution
- **Ultra-Popular (10,000+ stars):** {stats.get('star_ranges', {}).get('ultra_popular', 0)}
- **Very Popular (1,000-9,999 stars):** {stats.get('star_ranges', {}).get('very_popular', 0)} 
- **Popular (100-999 stars):** {stats.get('star_ranges', {}).get('popular', 0)}
- **Notable (50-99 stars):** {stats.get('star_ranges', {}).get('notable', 0)}

### Top Categories
"""
        
        for category, count in stats.get('top_categories', []):
            markdown += f"- **{category}:** {count} repositories\n"
        
        markdown += "\n---\n\n## 🌟 Top Batch Script Repositories\n\n"
        
        # Generate repository listings by category
        repo_index = 1
        for category_name, category_repos in categories.items():
            if not category_repos:
                continue
                
            markdown += f"### {category_name}\n\n"
            
            for repo in category_repos:
                markdown += self.format_repo_entry(repo, repo_index)
                repo_index += 1
        
        # Add additional sections
        markdown += self._generate_additional_sections(stats)
        
        return markdown
    
    def _generate_additional_sections(self, stats: Dict) -> str:
        """Generate additional documentation sections."""
        return f"""
---

## 🔍 Discovery & Methodology

These repositories were discovered using automated GitHub search with the following criteria:

### Search Strategy
1. **Primary Query:** `language:Batchfile stars:>100`
2. **Secondary Queries:**
   - `batch script windows stars:>50`
   - `windows automation batch stars:>50`
   - `.bat OR .cmd stars:>100`

### Quality Filters
- ✅ **Minimum Star Count:** 100+ stars (shows community trust)
- ✅ **Active Repositories:** Updated within last 2 years
- ✅ **Quality Content:** Actual batch scripts, not just examples
- ✅ **Clear Purpose:** Good documentation and descriptions
- ❌ **Excluded:** Test repositories, homework, deprecated projects

### Categorization
Repositories are automatically categorized based on their content:
- **System Tweaks & Performance** - Optimization and system enhancement
- **Development & Scripting Tools** - Build scripts and automation
- **Security & Privacy Tools** - System hardening and protection
- **File & Disk Utilities** - File operations and disk management
- **Network & Internet Tools** - Network automation and utilities

---

## 📈 Trends & Insights

Popular types of batch repositories include:

1. **System Activation & Licensing** - Windows/Office activation scripts
2. **Performance Optimization** - System tweaks and cleaners  
3. **Development Automation** - Build and deployment scripts
4. **Security & Privacy** - Hardening and debloating tools
5. **Media Processing** - FFmpeg and video conversion tools
6. **Gaming Utilities** - Game server and mod management

---

## 🎯 Quality Indicators

High-quality batch repositories typically have:

- ✅ **Clear Documentation** - Well-written README files
- ✅ **Active Maintenance** - Recent commits and updates
- ✅ **Community Engagement** - Issues are addressed promptly
- ✅ **Practical Utility** - Solves real-world problems
- ✅ **Clean Code** - Well-commented and organized scripts
- ✅ **Safety Considerations** - Warning about potentially dangerous operations

---

## 🔗 Related Resources

### Search Tools
- [GitHub Advanced Search](https://github.com/search/advanced)
- [Batch Scripts Search](https://github.com/search?q=language:Batchfile+stars:%3E100&type=repositories&s=stars&o=desc)

### Documentation
- [Windows Commands Reference](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/)
- [SS64 Command Line Reference](https://ss64.com/nt/)
- [Batch Scripting Tutorial](https://www.tutorialspoint.com/batch_script/)

### Tools for Discovery
- See [USAGE_GUIDE.md](USAGE_GUIDE.md) for automated discovery tools
- See [README.md](README.md) for script documentation

---

## ⚠️ Important Notes

### Security Considerations
- **Always review** batch scripts before running them
- **Test in safe environments** first (virtual machines recommended)
- **Understand the operations** each script performs
- **Check for malware** using antivirus software
- **Backup your system** before running system modification scripts

### Legal & Ethical Use
- Respect software licenses and terms of service
- Use activation scripts in accordance with software licensing
- Don't use tools for illegal or unauthorized activities
- Consider the ethical implications of system modifications

---

**Note:** Star counts and repository information are accurate as of the last update date. Repository popularity and availability may change over time.

*This documentation is automatically generated and updated by The Batch Compendium discovery system.*
"""
    
    def save_documentation(self, content: str, output_file: str):
        """Save the generated documentation to file."""
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Documentation saved to: {output_file}")
        except Exception as e:
            print(f"Error saving documentation: {e}")


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="Generate highly rated repositories documentation"
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Input CSV file with repository data"
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output markdown file"
    )
    parser.add_argument(
        "--min-stars",
        type=int,
        default=100,
        help="Minimum star count for inclusion (default: 100)"
    )
    
    args = parser.parse_args()
    
    generator = HighlyRatedDocsGenerator()
    
    # Load repositories
    print(f"Loading repositories from {args.input}...")
    repos = generator.load_repositories(args.input)
    
    if not repos:
        print("No repositories loaded.")
        return
    
    # Filter by minimum stars
    filtered_repos = [r for r in repos if r.get('stars', 0) >= args.min_stars]
    print(f"Found {len(filtered_repos)} repositories with {args.min_stars}+ stars")
    
    if not filtered_repos:
        print("No repositories meet the minimum star criteria.")
        return
    
    # Generate documentation
    print("Generating documentation...")
    markdown_content = generator.generate_markdown(filtered_repos)
    
    # Save to file
    generator.save_documentation(markdown_content, args.output)
    
    print(f"✅ Documentation generated successfully!")
    print(f"   - Repositories documented: {len(filtered_repos)}")
    print(f"   - Output file: {args.output}")


if __name__ == "__main__":
    main()