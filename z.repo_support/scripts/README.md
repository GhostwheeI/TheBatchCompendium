# Repository Support Scripts

This directory contains scripts to help maintain and update the TheBatchCompendium repository.

## generate_project_structure.py

**Purpose**: Dynamically generates the Project Structure section for the main README.md file.

**Usage**:
```bash
# From anywhere in the repository
python z.repo_support/scripts/generate_project_structure.py

# Or specify a custom path
python z.repo_support/scripts/generate_project_structure.py /path/to/repo
```

**Features**:
- Scans all main category directories
- Counts projects and files in each category
- Identifies projects with README documentation (📋 indicator)
- Generates collapsible HTML structure using `<details>` and `<summary>` tags
- Cross-platform compatible (Python 3.6+)

## generate_project_structure.bat

**Purpose**: Windows batch file wrapper for the Python script.

**Usage**:
```cmd
cd z.repo_support\scripts
generate_project_structure.bat
```

**Features**:
- Checks for Python availability
- Runs the Python script automatically
- Opens generated structure in Notepad for easy copying
- Handles Windows-specific paths and commands

## How to Update README.md

1. Run either script to generate the new structure
2. Copy the output (the complete Project Structure section)
3. Replace the existing "## 🗂 Project Structure" section in README.md
4. Commit the changes

The generated structure will automatically reflect:
- New projects added to any category
- Changes in file counts
- Addition/removal of README files in projects
- New or removed categories

## Legend

- 📋 = Project includes README/documentation
- 📂 = Main category folder  
- Numbers in parentheses = File count in each project