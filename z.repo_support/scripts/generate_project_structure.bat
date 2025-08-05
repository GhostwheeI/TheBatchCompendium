@echo off
setlocal EnableDelayedExpansion

:: =================================================================
:: Generate Project Structure for README.md
:: =================================================================
:: This script dynamically generates a collapsible HTML structure
:: showing all projects in TheBatchCompendium repository
:: =================================================================

echo Generating dynamic project structure...

:: Get the repository root directory (two levels up from this script)
set "REPO_ROOT=%~dp0..\.."
pushd "%REPO_ROOT%"

:: Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is required but not found in PATH
    echo Please install Python or ensure it's in your PATH
    pause
    exit /b 1
)

:: Create temporary Python script
set "TEMP_SCRIPT=%TEMP%\generate_structure.py"

(
echo #!/usr/bin/env python3
echo """
echo Script to generate a dynamic collapsible project structure for README.md
echo """
echo import os
echo import sys
echo from pathlib import Path
echo.
echo def generate_collapsible_structure^(base_path^):
echo     """Generate collapsible HTML structure for the project directories."""
echo     base_path = Path^(base_path^)
echo     
echo     # Define directories to ignore
echo     ignore_dirs = {'.git', '__pycache__', '.vscode', 'node_modules', '.pytest_cache'}
echo     
echo     # Get all main directories ^(excluding files and ignored directories^)
echo     main_dirs = []
echo     for item in sorted^(base_path.iterdir^(^)^):
echo         if item.is_dir^(^) and item.name not in ignore_dirs and not item.name.startswith^('.'^):
echo             main_dirs.append^(item^)
echo     
echo     # Build the collapsible structure
echo     structure_lines = []
echo     structure_lines.append^('^<details^>'^)
echo     structure_lines.append^('^<summary^>^<strong^>📁 Project Structure ^(Click to expand^)^</strong^>^</summary^>'^)
echo     structure_lines.append^(''^)
echo     
echo     for main_dir in main_dirs:
echo         # Add the main directory as a collapsible section
echo         subdir_count = len^([d for d in main_dir.iterdir^(^) if d.is_dir^(^) and not d.name.startswith^('.'^)]^)
echo         readme_exists = ^(main_dir / 'README.md'^).exists^(^)
echo         readme_indicator = ' 📋' if readme_exists else ''
echo         
echo         structure_lines.append^(f'^<details^>'^)
echo         structure_lines.append^(f'^<summary^>^<strong^>📂 {main_dir.name}/^</strong^> ^({subdir_count} projects{readme_indicator}^)^</summary^>'^)
echo         structure_lines.append^(''^)
echo         
echo         # List subdirectories
echo         subdirs = []
echo         for item in sorted^(main_dir.iterdir^(^)^):
echo             if item.is_dir^(^) and not item.name.startswith^('.'^):
echo                 subdirs.append^(item^)
echo         
echo         if subdirs:
echo             for subdir in subdirs:
echo                 # Check if subdir has a README
echo                 subdir_readme = ^(subdir / 'README.md'^).exists^(^)
echo                 readme_badge = ' 📋' if subdir_readme else ''
echo                 
echo                 # Count files in subdirectory
echo                 file_count = len^([f for f in subdir.iterdir^(^) if f.is_file^(^) and not f.name.startswith^('.'^)]^)
echo                 
echo                 structure_lines.append^(f'- **{subdir.name}**{readme_badge} ^({file_count} files^)'^)
echo         else:
echo             structure_lines.append^('- *No projects yet*'^)
echo         
echo         structure_lines.append^(''^)
echo         structure_lines.append^('^</details^>'^)
echo         structure_lines.append^(''^)
echo     
echo     structure_lines.append^('^</details^>'^)
echo     
echo     return '\n'.join^(structure_lines^)
echo.
echo if __name__ == "__main__":
echo     if len^(sys.argv^) != 2:
echo         print^("Usage: python generate_structure.py ^<repo_path^>'^)
echo         sys.exit^(1^)
echo     
echo     repo_path = sys.argv[1]
echo     structure = generate_collapsible_structure^(repo_path^)
echo     print^(structure^)
) > "%TEMP_SCRIPT%"

:: Run the Python script to generate structure
echo Running structure generation...
python "%TEMP_SCRIPT%" "%REPO_ROOT%" > "%TEMP%\new_structure.txt"

if errorlevel 1 (
    echo Error: Failed to generate project structure
    pause
    exit /b 1
)

echo.
echo Generated structure saved to: %TEMP%\new_structure.txt
echo.
echo You can now copy this structure and replace the Project Structure section in README.md
echo.

:: Clean up
del "%TEMP_SCRIPT%"

:: Open the generated file in notepad for easy copying
start notepad "%TEMP%\new_structure.txt"

popd
echo.
echo Done! Structure generation complete.
pause