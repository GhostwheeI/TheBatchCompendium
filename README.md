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

Scripts and imported toolkits are organized by purpose:

```
TheBatchCompendium/
├── Activation, Licensing & Update Scripts/ # Activation tools and licensing scripts
├── Automation & Installers/               # Deployment helpers and setup routines
├── Cleanup & Maintenance/                 # Disk, cache, and service cleanup tools
├── File, Media & Conversion Tools/        # File operations, media conversion, and related tools
├── Game Server & Mod Utilities/           # Game server management and modding scripts
├── Hardware & Network Tweaks/             # NIC, ping, IP configs, device fixes
├── Privacy & Debloating/                  # Debloaters, telemetry blockers, hardening
├── Scripting Libraries & Examples/        # Reusable routines and educational snippets
├── Security, Hardening & Diagnostics/     # Security, hardening, and diagnostic tools
├── System Optimization & Performance/     # Performance tuning and system optimization
└── z.repo_support/                        # Instructions, logs, metadata
```

Each folder may contain:
- 🧾 Single-purpose `.bat` scripts
- 📦 Full script-based repositories (flattened for GitHub browsing)
- 🔧 `.txt` files describing usage (where needed)

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
