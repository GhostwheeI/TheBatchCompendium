# Update & Activation Utilities

A collection of Windows activation and system update utilities designed to streamline license management and system maintenance tasks.

## 🚀 Quick Start

> **Important:** All activation scripts require **Administrator privileges** to function properly. Right-click and select "Run as administrator" or execute from an elevated command prompt.

## 📋 Included Repositories

### **akhilnathe--winactivate**
**Description:** Easy-to-use Windows HWID/KMS38 activation script supporting Windows 10 and 11.

**Features:**
- Automatic activation method detection (HWID/KMS38)
- Support for Windows build 10240 and above
- Command-line options for advanced users
- Compatible with x86 and x64 architectures (ARM64 not supported)

**Usage:**
```batch
# Basic activation (recommended)
winactivate.cmd

# Force KMS38 activation method
winactivate.cmd /forcekms38

# Skip administrator privilege detection
winactivate.cmd /skipadmincheck
```

**Location:** `./akhilnathe--winactivate/winactivate.cmd`

---

### **BingLingGroup--run-udp2raw-batch**
**Description:** Windows batch scripts for launching UDP acceleration tools including udp2raw, udpspeeder, and kcptun for network optimization.

**Features:**
- Automated UDP tunnel establishment
- Support for multiple acceleration protocols
- Configurable local and remote ports
- Password-based authentication

**Available Scripts:**
- `run-udp2raw-kcptun-udpspeeder.bat` - Combined UDP acceleration with kcptun
- `run-udp2raw-udpspeeder-tinyportmapper.bat` - UDP acceleration with port mapping

**Usage:**
```batch
# Edit configuration variables in the script before running:
# - remote_ip: Your remote server IP address
# - remote_uk_port: Remote UDP2RAW port for kcptun
# - remote_uu_port: Remote UDP2RAW port for udpspeeder
# - local_uk_port: Local UDP2RAW port for kcptun
# - local_uu_port: Local UDP2RAW port for udpspeeder
# - local_ss_port: Local shadowsocks server port
# - passwd: Universal password for authentication

# Run the desired script:
run-udp2raw-kcptun-udpspeeder.bat
# or
run-udp2raw-udpspeeder-tinyportmapper.bat
```

**Prerequisites:**
- UDP2RAW, UDPSpeeder, and KCPTUN binaries must be present in system PATH
- Network connectivity to remote server
- Proper firewall configuration for specified ports

**Location:** `./BingLingGroup--run-udp2raw-batch/`

---

### **danielj0nes--Activate-Windows10-Pro-Script**
**Description:** Windows 10 Pro activation script using KMS (Key Management Service) method.

**Features:**
- Installs Windows 10 Pro product key
- Configures KMS server for activation
- Automatic activation execution
- Requires non-activated Windows 10 Pro installation

**Usage:**
```batch
# Execute the activation script
script.bat
```

**Prerequisites:**
- Windows 10 Pro edition (non-activated)
- Administrator privileges
- Internet connectivity for KMS server communication

**Process:**
1. Installs generic Windows 10 Pro license key
2. Sets KMS server to `kms.digiboy.ir`
3. Attempts activation against the configured server

**Location:** `./danielj0nes--Activate-Windows10-Pro-Script/script.bat`

---

### **virusfreak7--Windows11-activator-script-**
**Description:** Comprehensive Windows 11 activation tool based on Microsoft Activation Scripts (MAS) supporting multiple activation methods.

**Features:**
- **Digital License (HWID):** Permanent activation for Windows 10/11
- **KMS38:** Extended activation until 2038 for Windows 10/11 and Server
- **Online KMS:** 180-day activation cycles for Windows/Server/Office

**Activation Methods:**
| Method | Supported Products | Duration |
|--------|-------------------|----------|
| Digital License | Windows 10/11 | Permanent |
| KMS38 | Windows 10/11/Server | Until 2038 |
| Online KMS | Windows/Server/Office | 180 Days |

**Usage:**
```batch
# Run the Microsoft Activation Tool
"Microsoft Activation Tool.cmd"
```

**Interactive Menu:** The script provides an interactive interface to:
- Select activation method
- Choose target product (Windows/Office)
- Configure activation options
- Monitor activation status

**Prerequisites:**
- Windows 11 compatible system
- Administrator privileges
- Internet connectivity (for Online KMS method)

**Location:** `./virusfreak7--Windows11-activator-script-/Microsoft Activation Tool.cmd`

## 🔧 General Usage Notes

- **Compatibility:** Scripts are designed for Windows 10 build 10240 and above
- **Execution:** Always run activation scripts with Administrator privileges
- **Network:** Some utilities require internet connectivity for license verification
- **Architecture:** Most tools support x86 and x64 systems (ARM64 support varies)

## 📁 Directory Structure

```
Update & Activation Utilities/
├── akhilnathe--winactivate/
│   ├── winactivate.cmd           # Main activation script
│   ├── gatherosstate.exe         # System state utility
│   └── slc.dll                   # License component
├── BingLingGroup--run-udp2raw-batch/
│   ├── run-udp2raw-kcptun-udpspeeder.bat
│   └── run-udp2raw-udpspeeder-tinyportmapper.bat
├── danielj0nes--Activate-Windows10-Pro-Script/
│   └── script.bat                # Windows 10 Pro activation
└── virusfreak7--Windows11-activator-script-/
    └── Microsoft Activation Tool.cmd
```
