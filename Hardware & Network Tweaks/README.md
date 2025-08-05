# Hardware & Network Tweaks

This directory contains utilities and scripts for hardware optimization, network configuration, and system-specific fixes. These tools help manage network settings, retrieve system information, and optimize performance for specific applications.

## Included Repositories:

### **Deadshot0x7--Wifipassword** — [Wi-Fi Password Retrieval Tool](./Deadshot0x7--Wifipassword)
Retrieves saved Wi-Fi passwords from Windows systems for previously connected networks.

**Available Script:**
- `WifiPasswordFInder.bat` - Interactive Wi-Fi password finder

**Usage:**
1. Right-click on `WifiPasswordFInder.bat` and select "Run as Administrator"
2. The script will display all saved Wi-Fi profiles on your system
3. Enter the network SSID (name) when prompted
4. The script will display the network details including the password

**Prerequisites:**
- Windows operating system
- Administrator privileges required
- Target network must have been previously connected to the system

---

### **ermannog--BatchScripts** — [Comprehensive Batch Script Collection](./ermannog--BatchScripts)
Collection of batch scripts for various system and network administration tasks.

**Network Scripts (`./Network/`):**

**`ResetNetworkAdapters.cmd`**
- Resets IPv4 and IPv6 settings to default
- Resets Windows Firewall and Winsock Catalog
- Flushes DNS cache and restarts the system

**Usage:** Run as Administrator, restart required after execution

**`ResetNetworkConnection.cmd`** 
- Comprehensive network connection reset utility
- Performs Winsock catalog restoration, TCP/IP reset, ARP cache clearing
- Handles NetBIOS name cache, DNS cache, and DHCP lease renewal

**Usage:** Execute as Administrator for complete network stack reset

**`SetIEProxy.cmd`**
- Configures proxy settings in Internet Explorer
- Modifies registry entries for proxy configuration

**Usage:** Run as Administrator to apply proxy settings system-wide

**Additional Script Categories:**
- **Acrobat Reader**: Configuration scripts for Reader 2017 Classic, 2020 Classic, and DC
- **Java**: Java environment configuration utilities
- **Operating System**: General Windows system scripts
- **Printing**: Print service and driver management
- **Security**: Security configuration and hardening scripts
- **Storage**: Disk and storage management utilities
- **Windows Update**: Update service management scripts
- **Windows Session**: User session and profile management
- **WSUS**: Windows Server Update Services configuration

---

### **Octanium91--NFS_Heat_CPU_Load_FIX** — [Need for Speed Heat CPU Optimization](./Octanium91--NFS_Heat_CPU_Load_FIX)
Fixes high CPU usage (90-100%) in Need for Speed Heat by optimizing thread processor allocation.

**Available Script:**
- `nfs_hits_cpu90_fix.cmd` - CPU load optimization script

**Usage:**
1. Copy `nfs_hits_cpu90_fix.cmd` to your Need for Speed Heat main installation folder
2. Run the script as Administrator
3. The script will automatically detect your CPU cores and threads
4. Creates a `user.cfg` file with optimized processor settings
5. Launch the game normally

**What the script does:**
- Detects CPU core and thread count using PowerShell commands
- Creates/updates `user.cfg` with optimized thread settings:
  - `Thread.ProcessorCount` - Set to physical core count
  - `Thread.MaxProcessorCount` - Set to physical core count  
  - `Thread.MinFreeProcessorCount` - Set to 0
  - `Thread.JobThreadPriority` - Set to 0
  - `GstRender.Thread.MaxProcessorCount` - Set to logical processor count

**Prerequisites:**
- Need for Speed Heat installed
- Windows PowerShell (for CPU detection)
- Administrator privileges recommended