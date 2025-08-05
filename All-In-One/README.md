# All-In-One

**Multi-purpose tools and comprehensive automation solutions** that cover multiple areas of Windows administration, development workflows, security analysis, and system optimization. These repositories provide complete, standalone toolkits for complex tasks.

---

## 🎮 Server Management & Gaming

### **DannyDorito--ARMA-3-Startup-and-Restart-Script**
Complete ARMA 3 server automation solution with crash monitoring and restart capabilities.

**Key Features:**
- Automatic server startup with custom parameters
- Crash detection and restart monitoring
- Steam Workshop mod support
- Database backup integration
- Performance optimization options

**Usage:**
```cmd
cd "DannyDorito--ARMA-3-Startup-and-Restart-Script"
:: Edit ARMAServerStart.bat to configure paths and parameters
ARMAServerStart.bat
```

### **DannyDorito--DayZ-Startup-and-Restart-Script**
Automated DayZ server management with monitoring and restart functionality.

**Key Features:**
- DayZ server startup automation
- Automatic crash recovery
- Mod management support
- Server monitoring capabilities

**Usage:**
```cmd
cd "DannyDorito--DayZ-Startup-and-Restart-Script"
:: Configure server settings in the batch file
start_server.bat
```

### **tinboye--Steam_workshop_scripts**
Steam Workshop content management and bulk mod downloading for game servers.

**Key Features:**
- Bulk mod downloading from Steam Workshop
- ARMA 3 server mod management
- Single mod download capability

**Usage:**
```cmd
cd "tinboye--Steam_workshop_scripts"
:: Download single mod
download_singlemod.bat

:: Download multiple mods in bulk
download_bulk_mods.bat

:: Download ARMA 3 server files
download_arma3server.bat
```

---

## 🔐 Security & Forensics

### **diogo-fernan--ir-rescue**
Comprehensive incident response and forensic data collection toolkit for Windows and Unix systems.

**Key Features:**
- Live system data collection
- Historical data from Volume Shadow Copies
- Memory dumping capabilities
- Network and process analysis
- Malware detection tools

**Usage:**
```cmd
cd "diogo-fernan--ir-rescue\win"
:: Run with administrator privileges
ir-rescue-win-v1.4.4.bat
```

### **frizb--Windows-Privilege-Escalation**
Complete Windows privilege escalation methodology with enumeration scripts and tools.

**Key Features:**
- Automated enumeration scripts
- Privilege escalation techniques
- File upload methods
- PowerShell exploitation tools

**Usage:**
```cmd
cd "frizb--Windows-Privilege-Escalation"
:: Basic system enumeration
windows_recon.bat

:: Copy-paste enumeration (no file upload required)
CopyAndPasteEnum.bat
```

### **Takaovi--BatchStealer**
Information gathering and system analysis script (educational/proof-of-concept).

**Key Features:**
- System information collection
- Browser data extraction
- Application data gathering
- Screenshot capabilities

**Usage:**
```cmd
cd "Takaovi--BatchStealer"
:: Configure webhook in file.bat before running
file.bat
```

---

## 💻 Development & Productivity Tools

### **aliounebfam--vscode_projects_launcher**
Multi-project VSCode workspace launcher for complex development environments.

**Key Features:**
- Launches multiple VSCode instances for different projects
- Git repository detection
- Cross-platform support (Windows/macOS/Linux)
- Customizable project detection

**Usage:**
```cmd
cd "aliounebfam--vscode_projects_launcher\scripts\windows"
:: Launch projects in current directory
mcode.bat

:: Launch projects in specific directory
mcode.bat "C:\path\to\projects"
```

### **jonstephens85--instantngp-batch**
Automated batch processing for NVIDIA's Instant-NGP neural radiance fields (NeRF) training.

**Key Features:**
- One-click NeRF training automation
- Image and video preprocessing
- Python environment setup
- CUDA integration support

**Usage:**
```cmd
cd "jonstephens85--instantngp-batch"
:: Install Python requirements first
install_requirements.bat

:: Process photos for NeRF training
nerf_photos.bat

:: Process video for NeRF training
nerf_video.bat
```

### **repnz--shellcode2exe**
Convert raw shellcode into executable files for testing and development.

**Key Features:**
- Shellcode to executable conversion
- Cross-platform assembly support
- Simple command-line interface

**Usage:**
```cmd
cd "repnz--shellcode2exe"
:: Place your shellcode in the appropriate format
shellcode2exe.bat
```

---

## ⚙️ System Optimization & Administration

### **Jisll--windows11**
Comprehensive Windows 11 optimization, customization, and tweaking toolkit.

**Key Features:**
- Performance optimizations
- Privacy enhancements
- System debloating
- Visual customizations
- Policy configurations

**Usage:**
```cmd
cd "Jisll--windows11"
:: Run the main optimization script
"Start Optimize Windows.bat"
```

### **massgravel--Microsoft-Activation-Scripts (MAS)**
Windows and Office activation toolkit with multiple activation methods.

**Key Features:**
- HWID activation for Windows
- Ohook activation for Office
- KMS38 and Online KMS methods
- Troubleshooting tools

**Usage:**
```cmd
cd "massgravel--Microsoft-Activation-Scripts\MAS\All-In-One-Version"
:: Run the main activation script
MAS_AIO.cmd
```

---

## 🚀 Getting Started

Most scripts require **administrator privileges** to function properly. Before running any script:

1. **Extract/Clone** the desired repository
2. **Navigate** to the specific tool directory
3. **Configure** any required parameters in the batch files
4. **Run** the main script with administrator rights

---

## 📁 Repository Organization

Each repository maintains its original structure and documentation. Check individual README files within each repository for specific configuration options and advanced usage instructions.
