# 🔐 Security & Diagnostics

Advanced security hardening scripts and diagnostic utilities for Windows systems. This collection includes comprehensive hardening solutions for various Windows versions, security configurations, and malware protection tools.

## 🛡️ Available Scripts & Utilities

### Windows Hardening Scripts
Located in `atlantsecurity--windows-hardening-scripts/`

#### **Windows-10-Hardening-script.cmd**
🎯 **Purpose:** Comprehensive Windows 10 security hardening with 900+ security configurations  
🚀 **Usage:**
```cmd
cd "Security & Diagnostics\atlantsecurity--windows-hardening-scripts"
Windows-10-Hardening-script.cmd
```
**Features:**
- Registry hardening for Windows 10
- Microsoft 365 and Office security settings
- Chrome, Edge, and Adobe Reader configurations
- File association protection against ransomware
- Service and feature optimization

#### **windows-11-hardening-script**
🎯 **Purpose:** Security hardening specifically designed for Windows 11  
🚀 **Usage:**
```cmd
cd "Security & Diagnostics\atlantsecurity--windows-hardening-scripts"
windows-11-hardening-script
```
**Features:**
- Windows 11 specific security configurations
- Enhanced privacy settings
- Modern security feature optimization

#### **windows-server-2019-hardening-script.cmd**
🎯 **Purpose:** Enterprise-grade Windows Server 2019 hardening following DISA STIG guidelines  
🚀 **Usage:**
```cmd
cd "Security & Diagnostics\atlantsecurity--windows-hardening-scripts"
windows-server-2019-hardening-script.cmd
```
**Features:**
- DISA STIG compliance configurations
- Server-specific security hardening
- Enterprise environment optimizations

#### **aws-workspaces-windows-hardening.cmd**
🎯 **Purpose:** Specialized hardening for AWS WorkSpaces Windows instances  
🚀 **Usage:**
```cmd
cd "Security & Diagnostics\atlantsecurity--windows-hardening-scripts"
aws-workspaces-windows-hardening.cmd
```
**Features:**
- AWS WorkSpaces specific configurations
- Cloud environment security optimizations
- Remote workspace protection

### Security Configuration Files

#### **chrome.reg**
🎯 **Purpose:** Chrome browser security policy configurations  
🚀 **Usage:**
```cmd
cd "Security & Diagnostics\atlantsecurity--windows-hardening-scripts"
regedit /s chrome.reg
```
**Features:**
- Advanced Protection enabled
- Popup and geolocation blocking
- Plugin and extension restrictions
- Privacy and tracking protection

#### **hosts**
🎯 **Purpose:** Comprehensive malware and tracking domain blocklist (58,866+ domains)  
🚀 **Usage:**
```cmd
cd "Security & Diagnostics\atlantsecurity--windows-hardening-scripts"
copy hosts C:\Windows\System32\drivers\etc\hosts
```
**Features:**
- Blocks malware domains
- Prevents tracking and ads
- Based on StevenBlack/hosts collection
- Community-maintained blocklist

#### **azure-block-passwords.txt**
🎯 **Purpose:** Common password blocklist for Azure AD environments  
🚀 **Usage:**
- Import into Azure AD Password Protection
- Use with organizational password policies
- Reference for creating custom password filters

**Features:**
- Common weak password patterns
- Azure AD integration ready
- Enterprise security compliance

## 📋 Prerequisites

> ⚠️ **Administrator Rights Required**  
> All hardening scripts require elevated Command Prompt or PowerShell

## 🎯 Quick Start

### Basic Hardening Workflow:
```cmd
# Navigate to the directory
cd "Security & Diagnostics\atlantsecurity--windows-hardening-scripts"

# For Windows 10 systems:
Windows-10-Hardening-script.cmd

# For Windows 11 systems:
windows-11-hardening-script

# For Windows Server 2019:
windows-server-2019-hardening-script.cmd

# Apply Chrome security settings:
regedit /s chrome.reg

# Install comprehensive hosts file:
copy hosts C:\Windows\System32\drivers\etc\hosts
```

## 🔧 Advanced Usage

### Script Customization
Most scripts contain configurable sections marked with `:: EDIT:` comments. Review and modify these sections according to your environment:

- **Individual Users:** Most default settings appropriate
- **Small Organizations:** Review Active Directory compatibility
- **Enterprise:** Modify domain and group policy sections

### Selective Application
Scripts can be run in sections by copying specific registry commands or configuration blocks to apply only desired hardening measures.

## 📁 Included Repositories
- **atlantsecurity--windows-hardening-scripts** — [Professional Windows security hardening scripts](./atlantsecurity--windows-hardening-scripts)
