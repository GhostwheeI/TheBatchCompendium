#!/usr/bin/env python3
"""
Automatically parse repository subfolders and metadata, extract descriptions,
format them into 1-sentence summaries, translate non-English descriptions to English,
and update the Folder Structure in README.md.
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

# Translation mapping to convert non-English descriptions to English
TRANSLATION_MAP = {
    "结合you-get、youtube-dl和ffmpeg，附带文件管理视频播放等命令.": 
        "Combines you-get, youtube-dl, and FFMPEG, with file management and video playback commands.",
    "script batch (.bat) interativo para otimizar suporte técnico no windows, automatizando reinício do sistema, limpeza de temporários, diagnóstico de rede, correção de erros comuns de impressão e ajustes de compartilhamento entre windows 10 e 11 via powershell, aumentando a eficiência e reduzindo erros humanos.": 
        "Interactive batch script (.bat) to optimize Windows support, automate system tasks, and adjust sharing settings via PowerShell.",
    "gpl-3.0 开源的 idm activation script 中文版：windows 批处理脚本，支持 idm 试用期冻结、普通激活、重置 and environment self-test.": 
        "GPL-3.0 open-source IDM Activation Script Chinese version: Windows batch script supporting IDM trial freeze, activation, reset, and self-check.",
    "gpl-3.0 开源的 idm activation script 中文版：windows 批处理脚本，支持 idm 试用期冻结、普通激活、重置和环境自检.": 
        "GPL-3.0 open-source IDM Activation Script Chinese version: Windows batch script supporting IDM trial freeze, activation, reset, and self-check.",
    "常用批处理.": 
        "Common batch scripts.",
    "one tool for windows folder icon batch modify. | 一个批量修改 windows 文件夹图标的小工具。.": 
        "One tool for Windows folder icon batch modification.",
    "在图片、压缩包 and 文件夹右键菜单加入mangameeya调用项。将bat放在mangameeya文件夹下运行。.":
        "Adds MangaMeeya context menu options to images, archives, and folders. Run the bat file from the MangaMeeya folder.",
    "在图片、压缩包和文件夹右键菜单加入mangameeya调用项。将bat放在mangameeya文件夹下运行。.": 
        "Adds MangaMeeya context menu options to images, archives, and folders. Run the bat file from the MangaMeeya folder.",
    "解锁 minecraft for windows （mcbe）的一键 bat 脚本.": 
        "One-click batch script to unlock Minecraft for Windows (MCBE).",
    "用于启动[udp2raw](https://github.com/wangyu-/udp2raw-tunnel)，[udpspeeder](https://github.com/wangyu-/udpspeeder)，[kcptun](https://github.com/xtaci/kcptun)/[tinyportmapper](https://github.com/wangyu-/tinyportmapper)的windows batch脚本，方便一键启动多个命令行工具。 [gplv3](license) [udpspeeder+udp2raw使用教程，并配合sstap加速优化网络游戏](https://www.moerats.com/archives/662/).": 
        "Windows batch script to launch udp2raw, udpspeeder, and kcptun/tinyportmapper to easily start multiple command-line tools.",
    "用于启动[udp2raw](https://github.com/wangyu-/udp2raw-tunnel)，[udpspeeder](https://github.com/wangyu-/udpspeeder)，[kcptun](https://github.com/xtaci/kcptun)/[tinyportmapper](https://github.com/wangyu-/tinyportmapper)的windows batch脚本，方便一键启动多个命令行工具。":
        "Windows batch script to launch udp2raw, udpspeeder, and kcptun/tinyportmapper to easily start multiple command-line tools.",
    "arquivo em lote (.bat) para otimização do windows.": 
        "Batch file (.bat) for Windows optimization.",
    "ativador office 365.": 
        "Office 365 Activator.",
    "windows repair tool pro هي أداة مجانية مخصصة لصيانة وإصلاح مشاكل ويندوز بسهولة من خلال واجهة cmd بسيطة وسريعة.": 
        "Windows Repair Tool Pro is a free tool dedicated to maintaining and repairing Windows problems easily through a simple and fast CMD interface.",
    "навык (skill) для ai-агентов: сборка/разборка обработок 1с в xml, выгрузка/загрузка конфигураций и расширений пакетными командами 1с: предприятие.": 
        "Skill for AI agents: assemble/disassemble 1C treatments to XML, upload/download configurations and extensions using batch commands."
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

def translate_to_english(desc):
    """Translate non-English descriptions using the translation mapping."""
    if not desc:
        return ""
    
    normalized = desc.strip().lower()
    
    # Precise comparison (strip punctuation/spaces) to avoid matching short words in long texts
    norm_clean = normalized.strip('.?! ')
    for non_eng, eng in TRANSLATION_MAP.items():
        non_eng_clean = non_eng.lower().strip('.?! ')
        if non_eng_clean == norm_clean or non_eng_clean in norm_clean:
            return eng
            
    # Handle specific partial match prefixes
    if "one click generation of product marketing and general content short videos" in normalized:
        return "One click generation of product marketing and general content short videos, AI batch automatic clipping, beautiful cross platform desktop tool."
        
    if "one tool for windows folder icon batch modify" in normalized:
        return "One tool for Windows folder icon batch modification."
        
    return desc

def clean_description(desc):
    """Format, clean, and translate a raw description to a single sentence or less."""
    if not desc:
        return ""
    
    # Translate to English if needed
    desc = translate_to_english(desc)
    
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
    
    # We must reset the root README.md to its original clean state (discarding previous run's changes)
    # to avoid double appending or matching dirty lines.
    # We can do this by running a git checkout on README.md before processing it.
    # if not dry_run:
    #     print("[INFO] Resetting README.md to main head to prevent dirty additions...")
    #     os.system("git checkout HEAD -- README.md")
        
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
        if line_stripped.startswith("## 🗂 Repository Index"):
            in_folder_structure = True
            updated_lines.append(line)
            continue
            
        # Stop flag when we reach next major section (e.g. ## Sample Tools or Each folder may contain)
        if in_folder_structure and line_stripped.startswith("## ") and not "Repository Index" in line_stripped:
            in_folder_structure = False
            
        if in_folder_structure:
            if "<details" in line:
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
