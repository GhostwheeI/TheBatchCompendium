# Cleanup & Maintenance Scripts

A comprehensive collection of Windows batch scripts and tools designed to clean, maintain, optimize, and secure your Windows system. These scripts help automate routine maintenance tasks, remove unwanted files, optimize system performance, and enhance security.

## 📋 System Requirements

### **Supported Operating Systems**
- **Windows 7** (Service Pack 1 or later)
- **Windows 8/8.1**
- **Windows 10** (All versions)
- **Windows 11** (All versions)
- **Windows Server 2008 R2** and later

### **Prerequisites**
- **Administrative privileges** - Most scripts require "Run as Administrator"
- **PowerShell 3.0 or later** (for PowerShell-based scripts)
- **Internet connection** (for scripts that download updates or tools)
- **Minimum 4GB RAM** (recommended for optimization scripts)
- **At least 1GB free disk space** (for cleanup operations)

## 🚀 Features

### **System Cleanup & Maintenance**
- **Temporary File Removal**: Automatically clean Windows temp files, browser cache, and system logs
- **Registry Cleaning**: Remove invalid registry entries and optimize registry performance
- **Disk Cleanup**: Free up disk space by removing unnecessary files and old backups
- **System File Integrity**: Check and repair corrupted system files using SFC and DISM

### **Performance Optimization**
- **Service Management**: Disable unnecessary Windows services to improve performance
- **Startup Optimization**: Remove unwanted startup programs and optimize boot times
- **Memory Optimization**: Clear memory caches and optimize RAM usage
- **Gaming Optimization**: Dedicated scripts for gaming performance enhancement

### **Security & Hardening**
- **Windows Hardening**: Apply security configurations and policies
- **Privacy Settings**: Configure privacy settings and disable telemetry
- **Log Management**: Enable comprehensive Windows logging for security monitoring
- **Update Management**: Control Windows Update behavior and installation

### **Utility Tools**
- **Software Activation**: Tools for activating various software (use responsibly)
- **Media Processing**: Batch utilities for video/audio file processing
- **Network Tools**: WiFi password recovery and network optimization
- **Development Environment**: Setup scripts for development tools and environments

## 📖 Usage Instructions

### **Basic Script Execution**

1. **Download or clone** the repository to your local machine
2. **Navigate** to the desired script directory
3. **Right-click** on the batch file (.bat) or PowerShell script (.ps1)
4. Select **"Run as Administrator"** from the context menu

```batch
# Example: Running the Windows Cleaner script
cd "Cleanup & Maintenance\TarikSeyceri--Windows-Cleaner.bat"
# Right-click on "Windows Cleaner.bat" and select "Run as Administrator"
```

### **Command Line Execution**

```cmd
# Open Command Prompt as Administrator
# Navigate to script directory
cd "C:\Path\To\TheBatchCompendium\Cleanup & Maintenance\ScriptFolder"

# Execute the script
script-name.bat

# For PowerShell scripts
powershell -ExecutionPolicy Bypass -File script-name.ps1
```

### **Script Categories and Examples**

#### **🧹 Cleanup Scripts**
- **TarikSeyceri--Windows-Cleaner.bat**: Removes temporary files and system junk
  ```cmd
  # Cleans: Temp folders, Recycle Bin, Browser cache, Windows logs
  cd "TarikSeyceri--Windows-Cleaner.bat"
  # Run as administrator
  ```

- **warengonzaga--wrn-cleaner**: Advanced Windows cleanup utility
  ```cmd
  # Features: Deep system cleanup, registry cleaning, performance optimization
  cd "warengonzaga--wrn-cleaner"
  wrn-cleaner-4.5.0.bat
  ```

#### **🔧 Optimization Scripts**
- **shoober420--windows11-scripts**: Windows 11 performance optimization
  ```cmd
  # Optimizes: Gaming performance, latency reduction, system responsiveness
  cd "shoober420--windows11-scripts"
  # Follow individual script instructions
  ```

- **SeregaSPb--Windows-10-batch-optimizer**: Comprehensive Windows 10 optimization
  ```cmd
  # Features: Service optimization, startup management, performance tweaks
  cd "SeregaSPb--Windows-10-batch-optimizer"
  # Run main optimization script
  ```

#### **🔒 Security & Hardening**
- **ZephrFish--WindowsHardeningScript**: System security hardening
  ```cmd
  # Applies: Security policies, privacy settings, vulnerability mitigations
  cd "ZephrFish--WindowsHardeningScript"
  Harden.cmd
  ```

- **Yamato-Security--EnableWindowsLogSettings**: Enhanced logging configuration
  ```cmd
  # Enables: Advanced Windows logging for security monitoring
  cd "Yamato-Security--EnableWindowsLogSettings"
  # Run configuration script
  ```

## ⚠️ Important Warnings & Safety Notes

### **🚨 Critical Warnings**

**ALWAYS CREATE A SYSTEM RESTORE POINT BEFORE RUNNING ANY SCRIPTS**
```cmd
# Create restore point manually:
# Control Panel > System > System Protection > Create
```

**Specific Risk Categories:**

- **Registry Modifications**: Scripts that modify the Windows registry can cause system instability if not used correctly
- **Service Disabling**: Disabling critical Windows services may break system functionality
- **File Deletion**: Cleanup scripts may permanently delete files - ensure you have backups
- **Security Settings**: Hardening scripts may affect software compatibility
- **Update Management**: Disabling Windows Update may leave your system vulnerable

### **🛡️ Risk Mitigation**

1. **Test in Virtual Machine**: Always test scripts in a VM before running on production systems
2. **Read Documentation**: Review each script's README.md for specific warnings and requirements
3. **Backup Important Data**: Create full system backups before running optimization scripts
4. **Monitor System Behavior**: Watch for unusual behavior after running scripts
5. **Have Recovery Media Ready**: Keep Windows installation media available for system recovery

### **⚖️ Legal Considerations**

- **Software Activation Scripts**: Use only for software you legally own
- **Corporate Environments**: Verify compliance with company policies before use
- **License Agreements**: Respect software license terms and conditions

## 🔧 Troubleshooting

### **Common Issues and Solutions**

#### **Permission Denied Errors**
```
Problem: "Access is denied" or "Operation requires elevation"
Solution: 
1. Right-click Command Prompt and select "Run as Administrator"
2. Ensure your user account has administrator privileges
3. Disable UAC temporarily if necessary (not recommended for regular use)
```

#### **Script Won't Execute**
```
Problem: Script files won't run or appear to do nothing
Solutions:
1. Check file associations: .bat files should open with cmd.exe
2. Verify script integrity: Re-download if file appears corrupted
3. Check antivirus: Temporarily disable real-time protection
4. Path issues: Ensure no spaces in file paths, or use quotes
```

#### **PowerShell Execution Policy Errors**
```
Problem: "Execution of scripts is disabled on this system"
Solution:
1. Open PowerShell as Administrator
2. Run: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
3. Confirm with 'Y' when prompted
4. Alternative: powershell -ExecutionPolicy Bypass -File script.ps1
```

#### **System Instability After Running Scripts**
```
Problem: Windows becomes unstable or features stop working
Solutions:
1. Restore from System Restore Point:
   - Type "rstrui" in Run dialog
   - Select restore point created before running scripts
2. Use System File Checker:
   - Open cmd as admin
   - Run: sfc /scannow
3. Reset specific Windows features:
   - DISM /Online /Cleanup-Image /RestoreHealth
```

#### **Missing Dependencies**
```
Problem: Scripts fail due to missing tools or components
Solutions:
1. Install Microsoft Visual C++ Redistributables
2. Update PowerShell to latest version
3. Install .NET Framework (latest version)
4. Verify Windows Management Framework is installed
```

### **Performance Issues**

#### **Scripts Running Slowly**
- **Disable real-time antivirus scanning** temporarily
- **Close unnecessary applications** to free up system resources
- **Run scripts during low-usage periods** (off-hours)
- **Check available disk space** - ensure at least 15% free space

#### **System Freezing During Execution**
- **Increase virtual memory** (pagefile) size
- **Monitor CPU and RAM usage** during script execution
- **Run scripts one at a time** instead of multiple simultaneously
- **Restart in Safe Mode** if persistent issues occur

### **Getting Help**

1. **Check Individual Project Documentation**: Each script folder contains specific README files
2. **Review Script Source Code**: Most scripts are open-source and well-commented
3. **Search Issue Trackers**: Check GitHub issues for known problems and solutions
4. **Community Forums**: Windows admin communities often have solutions for common problems
5. **Create System Recovery Plan**: Document your system configuration before modifications

## 📁 Included Script Collections

### **🔧 System Maintenance Tools**
- **[AveYo--MediaCreationTool.bat](./AveYo--MediaCreationTool.bat)** - Universal Media Creation Tool wrapper with business edition support
- **[TarikSeyceri--Windows-Cleaner.bat](./TarikSeyceri--Windows-Cleaner.bat)** - Comprehensive temporary file cleanup utility
- **[warengonzaga--wrn-cleaner](./warengonzaga--wrn-cleaner)** - Advanced Windows Registry and system cleaner
- **[ManuelGil--Script-Reset-Windows-Update-Tool](./ManuelGil--Script-Reset-Windows-Update-Tool)** - Windows Update troubleshooting and reset tool

### **🚀 Performance Optimization**
- **[SeregaSPb--Windows-10-batch-optimizer](./SeregaSPb--Windows-10-batch-optimizer)** - Comprehensive Windows 10 performance optimization
- **[shoober420--windows11-scripts](./shoober420--windows11-scripts)** - Windows 11 gaming and latency optimization scripts
- **[TheCraZyDuDee--Windows-Gaming-Optimization-Script](./TheCraZyDuDee--Windows-Gaming-Optimization-Script)** - Gaming-focused system optimization
- **[Zusier--Zusiers-optimization-Batch](./Zusier--Zusiers-optimization-Batch)** - ⚠️ **UNSUPPORTED** - General optimization scripts

### **🔒 Security & Hardening**
- **[ZephrFish--WindowsHardeningScript](./ZephrFish--WindowsHardeningScript)** - Comprehensive Windows security hardening
- **[Yamato-Security--EnableWindowsLogSettings](./Yamato-Security--EnableWindowsLogSettings)** - Enhanced Windows logging configuration
- **[Scrut1ny--Windows-Debloating-Script](./Scrut1ny--Windows-Debloating-Script)** - ⚠️ **CAUTION REQUIRED** - Windows debloating and privacy enhancement

### **🔧 System Administration**
- **[happy05dz--Batch-Script-Collection](./happy05dz--Batch-Script-Collection)** - Comprehensive batch script examples for system administration
- **[Kerbalnut--Batch-Tools-SysAdmin](./Kerbalnut--Batch-Tools-SysAdmin)** - System administrator batch tools and utilities
- **[wizz13150--PDQ_Repo](./wizz13150--PDQ_Repo)** - PDQ Deploy and Inventory scripts (unofficial)
- **[kodybrown--dos](./kodybrown--dos)** - Collection of DOS utilities and tools

### **🛠️ Specialized Utilities**
- **[awesome-windows11--windows11](./awesome-windows11--windows11)** - Comprehensive Windows 11 enhancement and customization tools
- **[lstprjct--IDM-Activation-Script](./lstprjct--IDM-Activation-Script)** - Internet Download Manager activation and trial reset
- **[n00mkrad--ffmpeg-batch-utils](./n00mkrad--ffmpeg-batch-utils)** - FFmpeg batch processing utilities for video/audio
- **[ddashizzle--snapraid_made_simple](./ddashizzle--snapraid_made_simple)** - SnapRAID maintenance and notification scripts
- **[t4rra--hotspot-helper](./t4rra--hotspot-helper)** - Windows hotspot lag fix for VR streaming

### **🏗️ Development & Installation**
- **[ai-joe-git--ComfyUI-Intel-Arc-Clean-Install-Windows-venv-XPU-](./ai-joe-git--ComfyUI-Intel-Arc-Clean-Install-Windows-venv-XPU-)** - ComfyUI automated installation for Intel Arc GPUs
- **[dend--windows-dev-box](./dend--windows-dev-box)** - Development environment setup scripts
- **[vegardit--cygwin-portable-installer](./vegardit--cygwin-portable-installer)** - Portable Cygwin installation utility
- **[Laf111--CEMU-Batch-Framework](./Laf111--CEMU-Batch-Framework)** - Batch framework for CEMU WII-U emulator

### **🔍 Security & Diagnostics**
- **[acgbfull--IBM_Appscan_Batch_Scan_Script](./acgbfull--IBM_Appscan_Batch_Scan_Script)** - IBM AppScan batch scanning automation
- **[TarikSeyceri--Windows-10-Update-Disabler.bat](./TarikSeyceri--Windows-10-Update-Disabler.bat)** - Windows 10 Update complete disable utility
- **[wureset-tools--script-wureset](./wureset-tools--script-wureset)** - Windows Update reset and troubleshooting tool

### **📚 Educational & Examples**
- **[Archive-projects--Batch-File-examples](./Archive-projects--Batch-File-examples)** - Collection of batch file examples and tutorials
- **[jersonmartinez--ShellScriptBatch](./jersonmartinez--ShellScriptBatch)** - Shell scripting and batch programming examples
- **[buananetpbun--Run-Command-Window-Batch-Script](./buananetpbun--Run-Command-Window-Batch-Script)** - 133 Windows run commands for quick access

### **🎮 Gaming & Entertainment**
- **[yaldabaoth444--asphalt_legends_unite_windows_bot](./yaldabaoth444--asphalt_legends_unite_windows_bot)** - Asphalt Legends Unite automation bot
- **[eppic--ytBATCH](./eppic--ytBATCH)** - YouTube-related batch processing utilities

### **🔧 Utility Collections**
- **[bongochong--CWP-Utilities](./bongochong--CWP-Utilities)** - Command-line privacy and block list utilities
- **[cavo789--tools_winscp](./cavo789--tools_winscp)** - WinSCP automation and utility tools
- **[daboynb--windows_scripts](./daboynb--windows_scripts)** - General Windows administration scripts
- **[andry81--contools](./andry81--contools)** - Console tools and utilities
- **[Chainski--WindowsCleanerUtility](./Chainski--WindowsCleanerUtility)** - Windows system cleaner utility
- **[Ec-25--FixIt](./Ec-25--FixIt)** - System repair and troubleshooting tools
- **[HiiARA--SoPI](./HiiARA--SoPI)** - System optimization and privacy improvement
- **[kkkgo--KMS_VL_ALL](./kkkgo--KMS_VL_ALL)** - KMS activation tools and utilities

---

> **⚡ Quick Start Tip**: For first-time users, we recommend starting with **TarikSeyceri--Windows-Cleaner.bat** for basic cleanup, then progressing to more advanced scripts as you become comfortable with the tools.

> **🔄 Regular Maintenance**: Consider running cleanup scripts weekly and optimization scripts monthly for optimal system performance.