#!/usr/bin/env python3
"""
Generate dynamic project structure for TheBatchCompendium README.md

This script scans the repository structure and generates a collapsible 
HTML structure showing all projects organized by category.

Usage:
    python generate_project_structure.py [repo_path]
    
If no repo_path is provided, uses current directory.
"""

import os
import sys
from pathlib import Path

def generate_collapsible_structure(base_path):
    """Generate collapsible HTML structure for the project directories."""
    base_path = Path(base_path)
    
    # Define directories to ignore
    ignore_dirs = {'.git', '__pycache__', '.vscode', 'node_modules', '.pytest_cache'}
    
    # Get all main directories (excluding files and ignored directories)
    main_dirs = []
    for item in sorted(base_path.iterdir()):
        if item.is_dir() and item.name not in ignore_dirs and not item.name.startswith('.'):
            main_dirs.append(item)
    
    # Build the collapsible structure
    structure_lines = []
    structure_lines.append('<details>')
    structure_lines.append('<summary><strong>📁 Project Structure (Click to expand)</strong></summary>')
    structure_lines.append('')
    
    for main_dir in main_dirs:
        # Add the main directory as a collapsible section
        subdir_count = len([d for d in main_dir.iterdir() if d.is_dir() and not d.name.startswith('.')])
        readme_exists = (main_dir / 'README.md').exists()
        readme_indicator = ' 📋' if readme_exists else ''
        
        structure_lines.append(f'<details>')
        structure_lines.append(f'<summary><strong>📂 {main_dir.name}/</strong> ({subdir_count} projects{readme_indicator})</summary>')
        structure_lines.append('')
        
        # List subdirectories
        subdirs = []
        for item in sorted(main_dir.iterdir()):
            if item.is_dir() and not item.name.startswith('.'):
                subdirs.append(item)
        
        if subdirs:
            for subdir in subdirs:
                # Check if subdir has a README
                subdir_readme = (subdir / 'README.md').exists()
                readme_badge = ' 📋' if subdir_readme else ''
                
                # Count files in subdirectory
                try:
                    file_count = len([f for f in subdir.iterdir() if f.is_file() and not f.name.startswith('.')])
                except PermissionError:
                    file_count = 0
                
                structure_lines.append(f'- **{subdir.name}**{readme_badge} ({file_count} files)')
        else:
            structure_lines.append('- *No projects yet*')
        
        structure_lines.append('')
        structure_lines.append('</details>')
        structure_lines.append('')
    
    structure_lines.append('</details>')
    
    return '\n'.join(structure_lines)

def generate_full_section(base_path):
    """Generate the complete Project Structure section for README.md"""
    structure = generate_collapsible_structure(base_path)
    
    full_section = f"""## 🗂 Project Structure

Scripts and imported toolkits are organized by purpose. Click below to explore the complete collection:

{structure}

**Legend:**
- 📋 = Project includes README/documentation
- 📂 = Main category folder  
- Numbers in parentheses = File count in each project

Each folder may contain:
- 🧾 Single-purpose `.bat` scripts
- 📦 Full script-based repositories (flattened for GitHub browsing)
- 🔧 `.txt` files describing usage (where needed)"""
    
    return full_section

if __name__ == "__main__":
    # Default to current directory if no path provided
    repo_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    
    try:
        section = generate_full_section(repo_path)
        print(section)
    except Exception as e:
        print(f"Error generating project structure: {e}", file=sys.stderr)
        sys.exit(1)