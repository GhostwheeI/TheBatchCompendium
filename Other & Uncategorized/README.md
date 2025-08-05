# Other & Uncategorized

A diverse collection of Windows batch scripts and utilities that don't fit into specific categories but provide valuable functionality for system administration, automation, and general purpose computing tasks.

## Included Repositories:

### **corpnewt--Batch-Scripts** ⟼ [A collection of batch scripts I've written over the years.](./corpnewt--Batch-Scripts)
**Key Scripts:**
- **Network Interfaces.bat** - Administrative utility to manage and configure network interfaces with UAC privilege escalation
- **Network Shares.bat** - Tools for managing Windows network shares and connections
- **SymLink Creator.bat** - Creates symbolic links with proper permissions handling
- **Win10 Tool.bat** - Windows 10 specific configuration and tweaking utilities
- **Random Numbers (Animated).bat** - Generates animated random number displays
- **Timeout User.bat** - User session timeout management

**Usage:** Run individual scripts as administrator when prompted. Most utilities require elevated privileges for system-level operations.

### **Da2dalus--FunBatchCode-MalicousAndNonMalicous** ⟼ [Handy batch scripts (Malicous and not malicous)](./Da2dalus--FunBatchCode-MalicousAndNonMalicous)
**Educational and Demonstration Scripts:**
- **message.bat** - Creates VBScript message boxes for user notifications
- **crazymouse.bat** - Demonstrates mouse control automation
- **changepassword.bat** - User password modification utilities
- **disabletaskmanager.bat** - Task manager access control
- **rainbowmatrix.bat** - Colorful matrix-style display effects
- **restart.bat / turnoff.bat** - System power management scripts

**Usage:** Execute scripts from command prompt. These are primarily for educational purposes and system demonstration.

### **EbolaMan-YT--PsExec** ⟼ [Remote administration toolkit using PsExec functionality](./EbolaMan-YT--PsExec)
**Remote Administration Suite:**
- **psexec.bat** - Interactive remote system administration tool with GUI interface
  - Remote shell access via WinRS
  - File system browsing
  - System information gathering
  - Remote shutdown capabilities
  - Automatic WinRM configuration

**Usage:** Run `psexec.bat` and provide target computer credentials. Requires network access and appropriate permissions on target systems.

### **geekcomputers--Batch** ⟼ [General purpose system utilities and automation scripts](./geekcomputers--Batch)
**System Utilities:**
- **defrag.cmd** - Automated disk defragmentation with logging
- **itunes.cmd** - iTunes library backup automation
- **lockpc.bat** - Instant PC locking utility
- **logoff.bat** - Custom logoff script for scheduled use
- **putty_backup.bat** - PuTTY session configuration backup to registry file
- **start-up.bat** - Custom startup routine automation
- **cmd.bat** - Command prompt launcher for restricted environments

**Usage:** Place scripts in convenient locations or schedule via Task Scheduler. Most can run without elevation except system-level operations.

### **matej137--OutlookRemover** ⟼ [Prevent or remove Microsoft Outlook (new) installation](./matej137--OutlookRemover)
**Outlook Management Tool:**
- **Outlook.bat** - Prevents new Outlook app installation by registering a placeholder package
  - Automatic CPU architecture detection
  - Developer mode registry configuration
  - AppX manifest installation
  - Supports both x64 and x86 systems

**Usage:** Run `Outlook.bat` as administrator. The script will automatically prevent the new Outlook app from installing while preserving system functionality.

### **Nickfost--Batch** ⟼ [Diverse collection of utilities, calculators, and system tools](./Nickfost--Batch)
**Utility Collection:**
- **Calculator.bat** - Interactive command-line calculator with basic arithmetic operations
- **Clean free space.bat** - Disk space cleaning and optimization
- **Info Finder.bat** - System information gathering utility
- **RACA.BAT** - Registry and configuration analysis tool
- **Exponential Multiplication.bat** - Mathematical computation utility
- **sigcheck downloads folder checker.bat** - File signature verification for downloads

**Usage:** Execute individual scripts based on needs. Calculator provides interactive menu, while others typically run with minimal user input required.

### **npocmaka--batch.scripts** ⟼ [Comprehensive batch scripting library and utilities](./npocmaka--batch.scripts)
**Extensive Scripting Library organized by categories:**
- **DateAndTime/** - Date/time manipulation and formatting utilities
- **fileUtils/** - File operations, searching, and management tools
- **network/** - Network configuration and diagnostic scripts
- **system/** - System information and configuration utilities
- **stringutils/** - String manipulation and text processing
- **math/** - Mathematical calculations and number processing
- **ProcessesUtils/** - Process management and monitoring tools
- **printing/** - Print job management and documentation tools

**Usage:** Navigate to specific category folders and run scripts as needed. Many scripts accept command-line parameters for customization. Refer to individual script headers for parameter details.

## General Usage Notes:
- Most scripts require Windows Command Prompt or PowerShell
- Administrative privileges may be required for system-level operations
- Scripts are designed for Windows environments (7, 8, 10, 11)
- Test scripts in non-production environments when possible
- Some utilities may require specific Windows features or services to be enabled
