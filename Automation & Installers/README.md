# 🤖 Automation & Installers

Scripts and utilities for automating software installation, deployment, and batch processing tasks. This collection provides tools for streamlined software management and automated workflow processing.

## 📦 Included Script Collections

### **⚙️ Software Installation & Management**
- **[cgartlab--Software_Install_Script](./cgartlab--Software_Install_Script)** - Automated batch software installation using winget package manager

### **🎨 3D Processing & Automation**  
- **[Shicoder--Meshlab-MLXScriptBatchProcessing](./Shicoder--Meshlab-MLXScriptBatchProcessing)** - Batch processing tools for MeshLab 3D mesh operations

---

## 🚀 Quick Start Guide

### Software Installation Scripts

**Location:** `cgartlab--Software_Install_Script/Windows/`

#### Core Scripts:
- **`software_install.bat`** - Main installation script that reads from software list
- **`software_install_proxy.bat`** - Installation script with proxy support
- **`switch_winget_to_USTCsource.bat`** - Switch winget source to Chinese USTC mirror
- **`software_list.txt`** - Configurable list of software packages to install

#### Basic Usage:
```batch
cd "cgartlab--Software_Install_Script\Windows"
software_install.bat
```

#### Customizing Software List:
1. Edit `software_list.txt` with your desired packages
2. Use `winget search <software_name>` to find package IDs
3. Add package IDs one per line to the list file

#### Example Software List Entry:
```
Microsoft.VisualStudioCode
Git.Git
Google.Chrome
```

#### Using Alternative Source:
```batch
# Switch to USTC mirror (for better speeds in China)
switch_winget_to_USTCsource.bat

# Then run installation
software_install.bat
```

### MeshLab Batch Processing

**Location:** `Shicoder--Meshlab-MLXScriptBatchProcessing/scripts/windows/Scripts/`

#### Core Scripts:
- **`convertMeshes.bat`** - Batch convert mesh files between formats
- **`runMLXScript.bat`** - Apply MLX filter scripts to multiple mesh files

#### Setup Requirements:
1. Install MeshLab to: `C:\Program Files\VCG\MeshLab\`
2. Extract scripts to: `C:\multiMeshScripting\`
3. Place input mesh files in the `input\` folder

#### Converting Mesh Formats:
```batch
cd "C:\multiMeshScripting"
convertMeshes.bat
```

**Configuration Options:**
- **Input formats:** PLY, OBJ, or all formats (*)
- **Output formats:** PLY, OBJ, U3D
- **Input/Output folders:** Configurable via script variables

#### Applying MLX Filter Scripts:
```batch
cd "C:\multiMeshScripting"
runMLXScript.bat
```

**Script Variables (editable in .bat files):**
```batch
@set inputFolder=input
@set outputFolder=output
@set inputMeshFormat=ply
@set outputMeshFormat=obj
@set mlxScriptFile=simple_script.mlx
```

---

## 📋 Detailed Usage Instructions

### Software Installation Workflow

#### 1. Prepare Environment
- Ensure Windows Package Manager (winget) is installed
- Run Command Prompt as Administrator
- Navigate to the Windows scripts directory

#### 2. Configure Package List
Edit `software_list.txt` with desired software:
```
# Development Tools
Microsoft.VisualStudioCode
Git.Git
GitHub.GitHubDesktop

# Media & Graphics
Gyan.FFmpeg
FontForge.FontForge

# Utilities
Microsoft.WindowsTerminal
Python.Python
```

#### 3. Execute Installation
```batch
# Basic installation
software_install.bat

# With proxy support (if needed)
software_install_proxy.bat
```

#### 4. Source Management
```batch
# Switch to alternative source
switch_winget_to_USTCsource.bat

# Reset to default source
winget source reset --force
```

### MeshLab Processing Workflow

#### 1. Environment Setup
- Install MeshLab from [meshlab.sourceforge.net](http://meshlab.sourceforge.net/)
- Verify meshlabserver.exe is at: `C:\Program Files\VCG\MeshLab\meshlabserver.exe`
- Extract MultiMesh scripts to: `C:\multiMeshScripting\`

#### 2. Prepare Input Files
- Place mesh files in `C:\multiMeshScripting\input\`
- Supported formats: PLY, OBJ, STL, OFF, and others

#### 3. Format Conversion
```batch
# Convert all PLY files to OBJ format
convertMeshes.bat
```

**Customization Example:**
```batch
# Edit convertMeshes.bat to change formats
@set inputMeshFormat=ply
@set outputMeshFormat=obj
```

#### 4. Apply Processing Scripts
```batch
# Apply MLX filter script to all input meshes
runMLXScript.bat
```

**Available MLX Scripts:**
- `simple_script.mlx` - Basic mesh processing
- Custom MLX scripts can be created in MeshLab and saved to `scripts\` folder

#### 5. Output Collection
- Processed files are saved to `C:\multiMeshScripting\output\`
- Original files remain unchanged in the input folder

---

## 🔧 Configuration Examples

### Batch Software Installation Categories

**Development Environment:**
```
Microsoft.VisualStudioCode
Git.Git
OpenJS.NodeJS
Python.Python
Microsoft.PowerShell
```

**Media Production:**
```
Gyan.FFmpeg
FontForge.FontForge
Genymobile.Scrcpy
```

**System Utilities:**
```
Microsoft.WindowsTerminal
JanDeDobbeleer.OhMyPosh
Okibcn.Nano
```

### MeshLab Processing Configurations

**High-Quality Conversion:**
```batch
@set inputMeshFormat=ply
@set outputMeshFormat=obj
@set outputMeshOptions=-om vc fq wn
```

**Batch Processing All Formats:**
```batch
@set inputMeshFormat=*
@set outputMeshFormat=ply
```

**Custom Script Application:**
```batch
@set mlxScriptFile=custom_filter.mlx
@set mlxScriptFolder=scripts
```
