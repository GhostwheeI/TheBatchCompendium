![Windows](https://img.shields.io/badge/platform-Windows-blue)
![Scripts](https://img.shields.io/badge/scripts-500%2B-green)
![License: MIT](https://img.shields.io/badge/license-MIT-brightgreen)

# 🧰 TheBatchCompendium

**TheBatchCompendium** is an ambitious, community-driven project aiming to be the **largest and most organized archive of Windows batch scripting resources** — combining **standalone `.bat` tools** with **full repo-based automation solutions**.

Whether you're a sysadmin, a power user, or a curious hacker, this compendium gives you instant access to decades of scripting logic, fixes, enhancements, and deployment tricks — all powered by pure `.bat` / `.cmd`.

---

## 🚀 Mission

Batch scripting remains essential for:

- 💻 Offline-safe and dependency-free automation
- ⚙️ Quick tooling in Windows-native environments
- 🔎 Transparent and editable workflows
- 🧪 Scriptable tweaks and system inspection

This repo unifies **hundreds of one-off scripts**, plus **entire toolkits from respected GitHub repos**, into a single location — for the first time.

---

## 🗂 Project Structure

Scripts and imported toolkits are organized by purpose with **3,000+ batch files** across these categories:

```
TheBatchCompendium/
├── All-In-One/ (55 .bat/.cmd files, 232 total)          # General-purpose & multipurpose scripts
│   ├── DannyDorito--ARMA-3-Startup-and-Restart-Script/  # Game server automation
│   ├── DannyDorito--DayZ-Startup-and-Restart-Script/    # DayZ server management
│   ├── Jisll--windows11/                                # Windows 11 tweaks collection
│   ├── Takaovi--BatchStealer/                          # System information gatherer
│   ├── diogo-fernan--ir-rescue/                        # Incident response toolkit
│   ├── frizb--Windows-Privilege-Escalation/            # Security testing scripts
│   ├── massgravel--Microsoft-Activation-Scripts/       # Windows/Office activation
│   └── [... 4 more projects]
│
├── Automation & Installers/ (5 .bat/.cmd files, 34 total)  # Deployment & setup routines
│   ├── Shicoder--Meshlab-MLXScriptBatchProcessing/     # 3D model batch processing
│   └── cgartlab--Software_Install_Script/              # Automated software installs
│
├── Cleanup & Maintenance/ (1,383 .bat/.cmd files, 3,922 total)  # Disk, cache & service cleanup
│   ├── AveYo--MediaCreationTool.bat/                   # Windows Media Creation Tool
│   ├── Chainski--WindowsCleanerUtility/                # Comprehensive system cleaner
│   ├── Kerbalnut--Batch-Tools-SysAdmin/                # System admin toolkit
│   ├── ManuelGil--Script-Reset-Windows-Update-Tool/    # Windows Update repair
│   ├── Scrut1ny--Windows-Debloating-Script/            # Windows debloating tools
│   ├── TarikSeyceri--Windows-10-Update-Disabler.bat/   # Update control scripts
│   ├── TheCraZyDuDee--Windows-Gaming-Optimization-Script/ # Gaming optimization
│   ├── ZephrFish--WindowsHardeningScript/               # Security hardening
│   ├── warengonzaga--wrn-cleaner/                      # System cleaner utility
│   └── [... 33+ more projects]
│
├── File & Media Utilities/ (1,240 .bat/.cmd files, 2,384 total)  # File ops & media processing
│   ├── AndrewHazelden--MultiMesh-Scripting/            # 3D mesh batch processing
│   ├── C0nw0nk--qBittorrent/                           # BitTorrent automation
│   ├── FoxP--PNG-to-ICO/                               # Image format conversion
│   ├── JaredCabot--OneDrive-Uninstaller/               # OneDrive removal tool
│   ├── K3V1991--ADBKit/                                # Android Debug Bridge tools
│   ├── KnightDanila--BAT_FFMPEG/                       # FFmpeg batch operations
│   ├── ManzDev--video-converter-scripts/               # Video conversion tools
│   ├── NabiKAZ--video2gif/                             # Video to GIF conversion
│   ├── Serede--mkvtoolnix-batch/                       # MKV video processing
│   ├── rossy--mpv-install/                             # MPV media player installer
│   ├── swagkarna--Defeat-Defender-V1.2.0/              # Windows Defender bypass
│   ├── warengonzaga--wifi-passview/                    # WiFi password viewer
│   └── [... 42+ more projects]
│
├── Hardware & Network Tweaks/ (51 .bat/.cmd files, 75 total)  # NIC, ping, IP configs, device fixes
│   ├── Deadshot0x7--Wifipassword/                      # WiFi password extraction
│   ├── Octanium91--NFS_Heat_CPU_Load_FIX/              # Game performance fix
│   └── ermannog--BatchScripts/                         # Various hardware scripts
│
├── Other & Uncategorized/ (259 .bat/.cmd files, 306 total)  # One-off tools that don't fit elsewhere
│   ├── Da2dalus--FunBatchCode-MalicousAndNonMalicous/  # Educational batch examples
│   ├── EbolaMan-YT--PsExec/                            # PsExec utilities
│   ├── corpnewt--Batch-Scripts/                        # Mixed utility scripts
│   ├── geekcomputers--Batch/                           # General batch collection
│   └── [... 3+ more projects]
│
├── Privacy & Debloating/ (0 .bat/.cmd files, 1 total)      # Debloaters, telemetry blockers, hardening
│   └── [Currently contains only README]
│
├── Scripting Libraries & Examples/ (56 .bat/.cmd files, 60 total)  # Reusable routines & educational snippets
│   └── logicopslab--BatchScripting/                    # Comprehensive batch examples
│
├── Security & Diagnostics/ (3 .bat/.cmd files, 11 total)   # AV checks, system status, forensic helpers
│   └── atlantsecurity--windows-hardening-scripts/      # Windows security hardening
│
├── System Optimization & Tweaks/ (1 .bat/.cmd file, 5 total)  # Performance and OS settings
│   └── UnLovedCookie--CoutX/                           # System optimization tools
│
├── Update & Activation Utilities/ (5 .bat/.cmd files, 17 total)  # Activation, licensing & Windows Update
│   ├── akhilnathe--winactivate/                        # Windows activation script
│   ├── danielj0nes--Activate-Windows10-Pro-Script/     # Windows 10 Pro activation
│   └── virusfreak7--Windows11-activator-script-/       # Windows 11 activation
│
└── z.repo_support/ (0 .bat/.cmd files, 2 total)           # Instructions, logs, metadata
    └── scripts/                                         # Repository maintenance scripts
```

### What's Inside Each Category:
- 🧾 **Single-purpose `.bat` scripts** - Ready-to-run utilities
- 📦 **Full repositories** - Complete projects flattened for easy browsing  
- 🔧 **Documentation** - READMEs and usage instructions where available
- ⚡ **3,057 total batch/cmd files** across all categories

---

## 🧪 Sample Tools

Here’s a peek at the kind of tools inside:

- `Cleanup & Maintenance/ClearTemp.bat` – Empty all temp folders safely
- `Privacy & Debloating/Win10Debloat.bat` – Strip bloat and silence telemetry
- `System Optimization & Tweaks/EnableTrim.bat` – Enable SSD TRIM on demand
- `Hardware & Network Tweaks/FixEthernet.bat` – Repair adapter states
- `File & Media Utilities/MassRename.bat` – Batch-rename files by pattern
- `Security & Diagnostics/LogDump.bat` – Dump recent event logs for analysis

---

## ⚙️ How to Use

> ⚠️ Most scripts require **elevated (admin) Command Prompt**  
> 💡 Always review scripts before running

### Example:

```bat
cd "Cleanup & Maintenance"
ClearTemp.bat
```

Most tools run as-is and output their steps directly in the terminal. No installs, no fluff.

---

## 🙋‍♂️ Who Is This For?

- 🛠 System administrators automating their workflows
- 🧪 Tinkerers, modders, and troubleshooters
- 🖥️ Air-gapped, legacy, or restricted environments
- 📚 Anyone learning how batch scripts actually *work*

---

## 💡 Tips

- Use Windows Search inside folders: `*.bat`
- Many full solutions include README or `.txt` helpers
- Fork or clone locally for faster script exploration
- Check commit history for recent additions or updates

---

## 🤝 Contributing

Pull requests are welcome!

You can:
- Submit original `.bat` files
- Add educational examples or snippets
- Flatten and contribute known GitHub script repos
- Improve categorization or documentation

Prefer clean, well-commented batch logic.

---

## 🔐 License

All content is covered under the [MIT License](LICENSE.md).  
Authors are credited where original repo info is preserved.

---

## 🙏 Credits

Thanks to:
- [@GhostwheeI](https://github.com/GhostwheeI)
- The open-source Windows scripting community
- Chainski, Tarik Seyceiri, and many repo authors featured here

---

🛠️ Made with love for the Windows command line
