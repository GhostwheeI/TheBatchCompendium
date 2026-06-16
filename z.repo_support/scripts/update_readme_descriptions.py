#!/usr/bin/env python3
"""
Automatically parse repository subfolders and metadata, extract descriptions,
format them into 1-sentence summaries, and update the Folder Structure in README.md.
"""

import os
import re
import csv
import urllib.parse
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
README_PATH = BASE_DIR / "README.md"
SCRIPTS_DIR = BASE_DIR / "z.repo_support" / "scripts"

# CSV databases to check as fallbacks
CSV_FILES = [
    SCRIPTS_DIR / "repo_results.csv",
    BASE_DIR / "z.repo_support" / "batch_repos_found.csv",
    SCRIPTS_DIR / "discovered_repos_20260615.csv"
]

# Hardcoded descriptions for repositories with missing/empty READMEs and CSV metadata
HARDCODED_FALLBACKS = {
    "lintangwisesa--microsoft_office_2016_activator": "A command-line script to activate Microsoft Office 2016 standard and professional plus.",
    "massgravel--microsoft-activation-scripts": "Open-source Windows and Office activator featuring HWID, Ohook, KMS38, and Online KMS activation.",
    "anonymlol--encoding_automation_scripts": "Automation scripts for video and audio encoding using x264, x265, and FFmpeg.",
    "honguito98--enctool-batch": "A development tool for text protection and obfuscation within Windows batch files.",
    "ibrahimtonca--35-different-commands-to-make-it-professionals-work-easier-all-in-one-bat-file-": "An all-in-one utility script compiling 35 useful commands to simplify IT tasks.",
    "jonnybanana--batchman-e-robby": "A batch file compilation of system optimization and administration tools.",
    "jpalbert--webcam-settings-dialog-windows": "A utility script to open the native webcam settings dialog in Windows.",
    "paxanddos--forzahorizonfix": "A batch script to fix crash and connection issues in Forza Horizon.",
    "scottgriv--batch-useful_bat_files": "A collection of miscellaneous useful Windows batch files and scripts.",
    "takaovi--batchstealer": "A demonstration/utility script for copying files and gathering basic system information.",
    "mansourm--ez-dns-changer.bat": "A simple script to quickly change DNS settings on Windows.",
    "szybnev--ttl-changer": "A lightweight batch script to change the Time-To-Live (TTL) network settings.",
    "swagkarna--defeat-defender-v1.2.0": "A batch script to disable or manage Windows Defender settings.",
    "jisll--windows11": "A collection of scripts for Windows 11 installation, tweakers, and configurations.",
    "narcotic--windows-optimizer": "A script designed to optimize and speed up Windows system performance.",
    "terryhuanghd--windows10-versionswitcher": "A batch script to switch between different editions of Windows 10."
}

def load_csv_descriptions():
    """Load repo descriptions from all available CSV files into a dictionary."""
    descriptions = {}
    for csv_file in CSV_FILES:
        if not csv_file.exists():
            continue
        try:
            with open(csv_file, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    name = row.get("name", "")
                    desc = row.get("description", "")
                    if name and desc:
                        # Standardize name (owner/repo) to lower case
                        key = name.strip().lower()
                        if key not in descriptions:
                            descriptions[key] = desc.strip()
        except Exception as e:
            print(f"[WARN] Warning loading CSV {csv_file.name}: {e}")
    return descriptions

def clean_description(desc):
    """Format and clean a raw description to a single sentence or less."""
    if not desc:
        return ""
    
    # Strip whitespace, quotes, HTML tags
    desc = desc.strip()
    desc = re.sub(r'<[^>]+>', '', desc)  # strip HTML tags
    
    if (desc.startswith('"') and desc.endswith('"')) or (desc.startswith("'") and desc.endswith("'")):
        desc = desc[1:-1].strip()
        
    # Split into sentences using a lookbehind assertion to keep punctuation
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z0-9"\'(]|$)', desc)
    if not sentences:
        return desc
        
    first_sentence = sentences[0].strip()
    
    # If the sentence is extremely short (e.g. less than 10 characters) and we have more sentences, merge
    if len(first_sentence) < 10 and len(sentences) > 1:
        first_sentence = (first_sentence + " " + sentences[1]).strip()
        
    # Remove trailing junk (like stray hyphens or semicolons)
    first_sentence = re.sub(r'\s+-\s*$', '', first_sentence)  # remove trailing -
    first_sentence = first_sentence.strip()
    
    # Ensure it ends with proper punctuation
    if first_sentence and not first_sentence[-1] in ['.', '!', '?']:
        first_sentence += '.'
        
    return first_sentence

def extract_description_from_readme(readme_path):
    """Parse a sub-README to extract the description."""
    if not readme_path.exists():
        return ""
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Try to find ## Description / ## What it is? / ## About sections first
        for header in [r'Description', r'What it is\??', r'What is it\??', r'About']:
            desc_match = re.search(r'##\s+' + header + r'\s*\n+([^#\n][^\n]*?(?:\n+[^#\n][^\n]*?)*?)(?=\n+##|\n+#|$)', content, re.IGNORECASE)
            if desc_match:
                desc_text = desc_match.group(1).strip()
                # Filter out any metadata lines
                lines = [line.strip() for line in desc_text.split('\n') if line.strip() and not line.strip().startswith('**') and not line.strip().startswith('-')]
                if lines:
                    return " ".join(lines)
                
        # If no section found, look below the main title `# repo_name` or first header
        lines = content.split('\n')
        collecting = False
        desc_lines = []
        for line in lines:
            line_stripped = line.strip()
            if line_stripped.startswith('# '):
                collecting = True
                continue
            if collecting:
                if line_stripped.startswith('##'):
                    # Encountered next section, stop
                    break
                # Skip metadata lines, image badges and headers
                if line_stripped.startswith('**') or line_stripped.startswith('-') or line_stripped.startswith('>') or line_stripped.startswith('!['):
                    continue
                if line_stripped:
                    desc_lines.append(line_stripped)
        if desc_lines:
            return " ".join(desc_lines)
            
    except Exception as e:
        print(f"[WARN] Error parsing README at {readme_path}: {e}")
        
    return ""

def process_readme(dry_run=True):
    """Parse README.md, find links under Folder Structure, and append descriptions."""
    if not README_PATH.exists():
        print(f"[ERROR] Root README.md not found at {README_PATH}")
        return
        
    csv_descriptions = load_csv_descriptions()
    print(f"[INFO] Loaded {len(csv_descriptions)} descriptions from CSV database.")
    
    with open(README_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    in_folder_structure = False
    in_details_block = False
    updated_lines = []
    
    # Statistics
    total_links = 0
    updated_links = 0
    fallback_links = 0
    hardcoded_links = 0
    missing_links = 0
    
    # Regex to detect links like:
    # - [akhilnathe--winactivate/](./Activation%2C%20Licensing%20%26%20Update%20Scripts/akhilnathe--winactivate)
    # or with existing descriptions to be updated:
    # - [akhilnathe--winactivate/](./path) - description
    link_regex = re.compile(r'^(\s*-\s*\[)(?![Rr][Ee][Aa][Dd][Mm][Ee]\.[Mm][Dd])([^\]/]+)(/?\]\()(\./[^)]+)(\))(.*)$')
    
    for line in lines:
        line_stripped = line.strip()
        
        # Detect Folder Structure section
        if line_stripped.startswith("## Folder Structure"):
            in_folder_structure = True
            updated_lines.append(line)
            continue
            
        # Stop flag when we reach next major section (e.g. ## Sample Tools or Each folder may contain)
        if in_folder_structure and line_stripped.startswith("## ") and not "Folder Structure" in line_stripped:
            in_folder_structure = False
            
        if in_folder_structure:
            if "<details>" in line:
                in_details_block = True
            elif "</details>" in line:
                in_details_block = False
                
            match = link_regex.match(line)
            if match and in_details_block:
                total_links += 1
                prefix = match.group(1)
                repo_dir = match.group(2)
                suffix_bracket = match.group(3)
                url_path = match.group(4)
                suffix_paren = match.group(5)
                
                # Decode url path
                decoded_path = urllib.parse.unquote(url_path)
                
                # Check target README.md path
                local_dir = BASE_DIR / decoded_path
                readme_file = local_dir / "README.md"
                
                raw_desc = extract_description_from_readme(readme_file)
                source = "sub-README"
                
                # Fallback to CSV if README is empty
                if not raw_desc:
                    # Convert repo folder name to owner/repo format
                    repo_key = repo_dir.replace('--', '/').lower()
                    raw_desc = csv_descriptions.get(repo_key, "")
                    source = "CSV database"
                    
                # Fallback to Hardcoded List if CSV is empty
                if not raw_desc:
                    raw_desc = HARDCODED_FALLBACKS.get(repo_dir.lower(), "")
                    source = "Hardcoded fallback"
                    
                clean_desc = clean_description(raw_desc)
                
                # Try to print safely in Windows terminal (ignore encoding errors for console print)
                try:
                    display_desc = clean_desc
                except Exception:
                    display_desc = clean_desc.encode('ascii', 'replace').decode('ascii')
                
                if clean_desc:
                    if source == "sub-README":
                        updated_links += 1
                    elif source == "CSV database":
                        fallback_links += 1
                    else:
                        hardcoded_links += 1
                        
                    # Format: - [repo/](./path) - Description.
                    new_line = f"{prefix}{repo_dir}{suffix_bracket}{url_path}{suffix_paren} - {clean_desc}\n"
                    updated_lines.append(new_line)
                    
                    # Print preview
                    if total_links <= 15 or not dry_run:
                        try:
                            print(f"[DESC] {repo_dir}: {display_desc} ({source})")
                        except UnicodeEncodeError:
                            safe_name = repo_dir.encode('ascii', 'ignore').decode('ascii')
                            safe_desc = display_desc.encode('ascii', 'ignore').decode('ascii')
                            print(f"[DESC] {safe_name}: {safe_desc} ({source})")
                else:
                    missing_links += 1
                    # Keep original line if no description found
                    updated_lines.append(line)
                    try:
                        print(f"[MISSING] No description found for {repo_dir}")
                    except UnicodeEncodeError:
                        safe_name = repo_dir.encode('ascii', 'ignore').decode('ascii')
                        print(f"[MISSING] No description found for {safe_name}")
            else:
                updated_lines.append(line)
        else:
            updated_lines.append(line)
            
    print(f"\n[STATS] Summary:")
    print(f"  Total folder links found: {total_links}")
    print(f"  Descriptions from sub-READMEs: {updated_links}")
    print(f"  Descriptions from CSV fallbacks: {fallback_links}")
    print(f"  Descriptions from Hardcoded fallbacks: {hardcoded_links}")
    print(f"  Missing descriptions: {missing_links}")
    
    if not dry_run:
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.writelines(updated_lines)
        print(f"\n[SUCCESS] Successfully updated {README_PATH}")
    else:
        print(f"\n[INFO] Dry run completed. No files modified. Run with --apply flag to modify README.md.")

if __name__ == "__main__":
    import sys
    dry_run_flag = True
    if len(sys.argv) > 1 and sys.argv[1].lower() == "--apply":
        dry_run_flag = False
        
    process_readme(dry_run=dry_run_flag)
