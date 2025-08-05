## 🔒 Privacy & Debloating Script Collections

This directory catalogues Windows privacy enhancement and system debloating utilities available throughout TheBatchCompendium. These tools help reduce telemetry, remove bloatware, and enhance system privacy.

### **🛡️ Comprehensive Debloating Solutions**
- **[Scrut1ny--Windows-Debloating-Script](../Cleanup%20&%20Maintenance/Scrut1ny--Windows-Debloating-Script)** - ⚠️ **CAUTION REQUIRED** - Advanced PowerShell-based Windows debloating with comprehensive telemetry removal
- **[daboynb--windows_scripts/aio_debloater](../Cleanup%20&%20Maintenance/daboynb--windows_scripts/aio_debloater)** - All-in-one debloater with OneDrive removal and system cleanup
- **[Jisll--windows11/Debloating](../All-In-One/Jisll--windows11/Debloating)** - Windows 11 focused debloating suite with modular scripts

### **🔍 Privacy Enhancement Tools**
- **[dend--windows-dev-box/privacy.bat](../Cleanup%20&%20Maintenance/dend--windows-dev-box/scripts/privacy.bat)** - Disable Cortana, Bing search, and privacy-invasive Windows features
- **[dend--windows-dev-box/edge-privacy.bat](../Cleanup%20&%20Maintenance/dend--windows-dev-box/scripts/edge-privacy.bat)** - Microsoft Edge privacy configuration and telemetry blocking
- **[leetfin--Windows10Tools/adolfintel-Windows10-Privacy](../File%20&%20Media%20Utilities/leetfin--Windows10Tools/adolfintel-Windows10-Privacy)** - Comprehensive Windows 10 privacy toolkit

### **🗑️ Bloatware Removal Utilities**
- **[leetfin--Windows10Tools/FullDebloat.bat](../File%20&%20Media%20Utilities/leetfin--Windows10Tools/WIPs/FullDebloat.bat)** - Complete Windows bloatware removal with service optimization
- **[leetfin--Windows10Tools/Debloatx.bat](../File%20&%20Media%20Utilities/leetfin--Windows10Tools/WIPs/Debloatx.bat)** - Extended debloating script with telemetry controls

### **📡 Telemetry & Data Collection Control**
- **[Jisll--windows11/Disable Telemetry.cmd](../All-In-One/Jisll--windows11/Debloating/Disable%20Telemetry.cmd)** - Comprehensive telemetry disabling including Nvidia tracking
- **[Jisll--windows11/Disable Services.cmd](../All-In-One/Jisll--windows11/Debloating/Disable%20Services.cmd)** - Disable privacy-invasive Windows services
- **[Jisll--windows11/Disable Tasks.cmd](../All-In-One/Jisll--windows11/Debloating/Disable%20Tasks.cmd)** - Remove scheduled tasks that collect user data

### **🌐 Microsoft Services Removal**
- **[Jisll--windows11/Remove Microsoft Edge.cmd](../All-In-One/Jisll--windows11/Debloating/Remove%20Microsoft%20Edge.cmd)** - Complete Microsoft Edge removal utility
- **[Jisll--windows11/Remove OneDrive.cmd](../All-In-One/Jisll--windows11/Debloating/Remove%20OneDrive.cmd)** - OneDrive complete removal and cleanup
- **[Jisll--windows11/Remove Packages.cmd](../All-In-One/Jisll--windows11/Debloating/Remove%20Packages.cmd)** - Remove unwanted Windows app packages

### **⚙️ System Optimization & Cleanup**
- **[Jisll--windows11/CleanUp.cmd](../All-In-One/Jisll--windows11/Debloating/CleanUp.cmd)** - System cleanup with privacy focus
- **[Jisll--windows11/Disable Features.cmd](../All-In-One/Jisll--windows11/Debloating/Disable%20Features.cmd)** - Disable unnecessary Windows features
- **[Jisll--windows11/Replace Startmenu.cmd](../All-In-One/Jisll--windows11/Debloating/Replace%20Startmenu.cmd)** - Start menu customization and debloating

## 🚀 Usage Instructions

### **Basic Execution**
Most scripts require administrative privileges. Run Command Prompt as Administrator before executing:

```cmd
cd "Path\To\Script\Directory"
script_name.bat
```

### **PowerShell Scripts**
For PowerShell-based tools like Scrut1ny's debloater:

```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
.\debloat.ps1
```

### **Modular Approach**
Many collections offer modular scripts. Execute specific components based on your needs:

```cmd
:: Example: Disable only telemetry
"Disable Telemetry.cmd"

:: Example: Remove only Edge browser  
"Remove Microsoft Edge.cmd"
```

### **Batch Processing**
For comprehensive system debloating, scripts can be chained:

```cmd
"Disable Telemetry.cmd" && "Remove Packages.cmd" && "CleanUp.cmd"
```

## 📋 Script Categories Guide

### **🔴 High Impact (System-Wide Changes)**
- Full debloating solutions (Scrut1ny, AIO debloater)
- Service and feature disabling scripts
- Microsoft service removal tools

### **🟡 Medium Impact (Privacy Focused)**
- Telemetry and tracking disabling
- Search and Cortana removal
- Registry privacy tweaks

### **🟢 Low Impact (Cleanup & Optimization)**
- Temporary file cleanup
- Start menu customization
- App package management

## 💡 Best Practices

### **Pre-Execution Preparation**
- Create system restore point before running major debloating scripts
- Review script contents to understand modifications
- Start with individual component scripts before running comprehensive tools

### **Execution Order**
1. **Telemetry Control**: Start with telemetry disabling scripts
2. **Service Management**: Disable unnecessary services  
3. **Package Removal**: Remove unwanted app packages
4. **System Cleanup**: Run cleanup and optimization scripts
5. **Browser Configuration**: Configure or remove Edge/OneDrive

### **Post-Execution Verification**
- Restart system to ensure changes take effect
- Verify critical system functions remain operational
- Test internet connectivity and Windows Update functionality
