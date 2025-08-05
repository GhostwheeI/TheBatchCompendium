# File & Media Utilities

This directory contains a comprehensive collection of batch scripts and utilities for file management, media processing, system optimization, and various administrative tasks. The tools are organized by category below with detailed usage instructions.

## Video & Audio Processing

### **ManzDev--video-converter-scripts** — [Easy drag-and-drop video/audio format conversion](./ManzDev--video-converter-scripts)
**Usage:** Simply drag any video or audio file onto the desired conversion script (.bat file). Supports 26+ formats including:
- Video: MP4, MKV, AVI, WEBM, MOV, FLV, GIF, MPEG, OGG, WMV
- Audio: MP3, AAC, FLAC, OGG, WAV, WMA, Opus

**Quick Start:** Download the scripts, drag your media file to the appropriate `.bat` file (e.g., `conversor a mp4.bat` for MP4 conversion).

### **KnightDanila--BAT_FFMPEG** — [FFMPEG batch script collection](./KnightDanila--BAT_FFMPEG)
**Usage:** Collection of ready-to-use FFMPEG batch scripts for advanced video processing tasks.

### **NabiKAZ--video2gif** — [Convert videos to animated GIFs](./NabiKAZ--video2gif)
**Usage:** Drag video files onto the script to convert them to optimized animated GIF format.

### **describe19--check-video** — [Video file integrity checker](./describe19--check-video)
**Usage:** Run `check-videos.bat` to verify the integrity of video files using FFMPEG. Requires FFMPEG to be installed or available in the script directory.

### **Serede--mkvtoolnix-batch** — [Batch processing with MKVToolNix](./Serede--mkvtoolnix-batch)
**Usage:** Automate batch processing of Matroska video files using MKVToolNix utilities.

## Image Processing

### **FoxP--PNG-to-ICO** — [Convert images to multi-resolution ICO files](./FoxP--PNG-to-ICO)
**Usage:** 
- **Right-click method:** Right-click any image file or folder → Select "PNG to ICO" from context menu
- **Drag-drop method:** Drag image files or folders onto `png_to_ico.bat`
- **Supported formats:** PNG, GIF, BMP, SVG, JPG
- **Output:** Multi-resolution ICO files (16x16 to 256x256 pixels) in the same directory as source images

## YouTube & Media Downloads

### **edinsuta--youtube-dl-batch** — [Simplified YouTube-DL interface](./edinsuta--youtube-dl-batch)
**Usage:** Place `youtube-dl.exe` in the same directory as the batch files, then run:
- `ytdlBasic.bat` — Download best quality video automatically
- `ytdlAdvanced.bat` — Choose specific video/audio formats manually
- `ytdlCustom.bat` — Enter custom command-line arguments
- `ytdlInfo.bat` — Display information about your youtube-dl installation
- `ytdlUpdate.bat` — Update youtube-dl to the latest version

## File Management & Cloud Storage

### **Moodkiller--SendTo-rclone-GDrive** — [Upload files to Google Drive via right-click](./Moodkiller--SendTo-rclone-GDrive)
**Usage:** After setup, right-click any file or folder → "Send to" → Select the configured Google Drive option. Requires rclone configuration.

### **JaredCabot--OneDrive-Uninstaller** — [Complete OneDrive removal](./JaredCabot--OneDrive-Uninstaller)
**Usage:** Run as administrator:
- `OneDrive Uninstaller v1.4.bat` (latest version) — Completely removes OneDrive from Windows 10/11
- Multiple versions available for different system configurations

### **moom825--batch-extention-spoofer** — [File extension spoofing tool](./moom825--batch-extention-spoofer)
**Usage:** Spoof file extensions using Unicode character U+202E for security testing purposes.

## Android & Mobile Device Tools

### **K3V1991--ADBKit** — [Android Debug Bridge toolkit](./K3V1991--ADBKit)
**Usage:** 
- Run `Open CMD.bat` to open command prompt with ADB tools ready
- Use included ADB executables for Android device management and debugging
- Full ADB functionality for app installation, file transfer, and device control

### **mitchv2020--QuestToolbox** — [Oculus Quest VR toolkit](./mitchv2020--QuestToolbox)
**Usage:** Comprehensive batch file with utilities for Quest 1/2 VR headset management, sideloading, and optimization.

## System Optimization & Performance

### **ancel1x--Ancels-Performance-Batch** — [Interactive system performance optimizer](./ancel1x--Ancels-Performance-Batch)
**Usage:** Run the interactive script and follow prompts to optimize system performance and reduce latency. Choose specific optimizations based on your system configuration.

### **NARCOTIC--Windows-Optimizer** — [Storage optimization and defragmentation](./NARCOTIC--Windows-Optimizer)
**Usage:** Automatically optimizes and defragments all connected storage drives while fixing file system errors.

### **Batlez--Batlez-Tweaks** — [System tweaks collection](./Batlez--Batlez-Tweaks)
**Usage:** Collection of Windows optimization and customization scripts for improved system performance.

### **tcja--Windows-10-tweaks** — [Windows 10 optimization scripts](./tcja--Windows-10-tweaks)
**Usage:** Multiple scripts targeting different aspects of Windows 10 optimization and customization.

## Network & Connectivity

### **warengonzaga--wifi-passview** — [WiFi password viewer](./warengonzaga--wifi-passview)
**Usage:** Run the script to display saved WiFi passwords on the current system. Requires administrator privileges.

### **MansourM--ez-dns-changer.bat** — [Easy DNS configuration changer](./MansourM--ez-dns-changer.bat)
**Usage:** Simple batch script to change DNS settings for improved performance or privacy.

### **szybnev--TTL-Changer** — [Network TTL modification tool](./szybnev--TTL-Changer)
**Usage:** Modify Time-To-Live (TTL) values for network packets, useful for bypassing certain network restrictions.

## Security & Diagnostics

### **AhmetHan--EDR_Tester** — [EDR detection and response testing](./AhmetHan--EDR_Tester)
**Usage:** Run to test Endpoint Detection and Response (EDR) system capabilities in a controlled, noisy manner for security assessment.

### **gladiatx0r--Powerless** — [Windows privilege escalation enumeration](./gladiatx0r--Powerless)
**Usage:** Execute on target systems to enumerate potential privilege escalation vectors. Designed for legacy Windows systems without PowerShell.

### **azmatt--windowsEnum** — [Windows enumeration for privilege escalation](./azmatt--windowsEnum)
**Usage:** Automated Windows enumeration script for identifying privilege escalation opportunities during security assessments.

### **swagkarna--Defeat-Defender-V1.2.0** — [Windows Defender bypass techniques](./swagkarna--Defeat-Defender-V1.2.0)
**Usage:** Collection of scripts for disabling or bypassing Windows Defender for security testing purposes.

## Development & Build Tools

### **eddex--aseprite-windows-docker-build** — [Aseprite compilation automation](./eddex--aseprite-windows-docker-build)
**Usage:** Simplified Docker-based approach to compile Aseprite from source on Windows systems.

### **slathrop--git-scripts-win** — [Git operation batch scripts](./slathrop--git-scripts-win)
**Usage:** Simple Windows batch files for common Git operations and repository management tasks.

### **ImGuiNET--ImGui.NET-nativebuild** — [ImGui.NET native build scripts](./ImGuiNET--ImGui.NET-nativebuild)
**Usage:** Run `git submodule update --init` followed by the build scripts to compile ImGui.NET native components.

## Specialized Tools

### **C0nw0nk--qBittorrent** — [qBittorrent automation script](./C0nw0nk--qBittorrent)
**Usage:** Command-line automation for qBittorrent with multiple features for torrent management.

### **prashantmi--Rar-Password-Cracker** — [RAR archive password recovery](./prashantmi--Rar-Password-Cracker)
**Usage:** Batch script for attempting to recover passwords from RAR encrypted archives using dictionary attacks.

### **CoolDotty--NeverWake** — [Prevent random Windows wake-ups](./CoolDotty--NeverWake)
**Usage:** Run to configure Windows power settings and prevent the system from randomly waking up from sleep mode.

### **jpalbert--webcam-settings-dialog-windows** — [Webcam settings configuration](./jpalbert--webcam-settings-dialog-windows)
**Usage:** Launch webcam settings dialog for adjusting camera properties and configurations.

## Activation & Licensing

### **prestonsn--windows-10-activation-script** — [Windows 10 activation](./prestonsn--windows-10-activation-script)
**Usage:** Run as administrator to activate Windows 10. Ensure you have appropriate licensing rights.

### **LintangWisesa--Microsoft_Office_2016_Activator** — [Office 2016 activation](./LintangWisesa--Microsoft_Office_2016_Activator)
**Usage:** Microsoft Office 2016 activation utility. Ensure compliance with licensing agreements.

## Collections & Examples

### **happy05dz--Batch-Script-Collection** — [Comprehensive batch script examples](./happy05dz--Batch-Script-Collection)
**Usage:** Educational collection covering system administration, file management, maintenance, Internet tools, and network administration.

### **PassingTheKnowledge--Batchography** — [Batch scripting recipes and snippets](./PassingTheKnowledge--Batchography)
**Usage:** Scripts and examples from the Batchography book for learning advanced batch scripting techniques.

### **scottgriv--batch-useful_bat_files** — [Collection of useful batch utilities](./scottgriv--batch-useful_bat_files)
**Usage:** Curated collection of practical batch files for various Windows administration tasks.

## Additional Utilities

- **abbodi1406--BatUtil** — [General batch utilities](./abbodi1406--BatUtil)
- **AndrewHazelden--MultiMesh-Scripting** — [Multi-mesh scripting tools](./AndrewHazelden--MultiMesh-Scripting)
- **anonymlol--Encoding_automation_scripts** — [Text encoding automation](./anonymlol--Encoding_automation_scripts)
- **ardyan69--wa** — [WhatsApp automation tools](./ardyan69--wa)
- **chsliu--batch** — [General Windows batch file collection](./chsliu--batch)
- **conan513--TrinityBuilder** — [TrinityCore server builder](./conan513--TrinityBuilder)
- **Espionage724--Windows** — [Privacy and performance batch scripts](./Espionage724--Windows)
- **fr0st-iwnl--WinConfigs** — [Windows configuration scripts](./fr0st-iwnl--WinConfigs)
- **Honguito98--enctool-batch** — [Batch file text protection tool](./Honguito98--enctool-batch)
- **JonnyBanana--BatchMan-e-Robby** — [Batman-themed batch utilities](./JonnyBanana--BatchMan-e-Robby)
- **kezoponk--DDoS.bat** — [Network stress testing tool](./kezoponk--DDoS.bat)
- **leetfin--Windows10Tools** — [Windows 10 utility collection](./leetfin--Windows10Tools)
- **m2nlight--WindowsServerToWindowsDesktop** — [Windows Server to Desktop converter](./m2nlight--WindowsServerToWindowsDesktop)
- **PAXANDDOS--ForzaHorizonFix** — [Forza Horizon game fixes](./PAXANDDOS--ForzaHorizonFix)
- **peterjc123--pytorch-scripts** — [PyTorch building scripts (deprecated)](./peterjc123--pytorch-scripts)
- **rossy--mpv-install** — [MPV media player installer](./rossy--mpv-install)
- **TerryHuangHD--Windows10-VersionSwitcher** — [Windows 10 version switching tool](./TerryHuangHD--Windows10-VersionSwitcher)
- **userdocs--LFTP4WIN** — [LFTP Windows deployment tool](./userdocs--LFTP4WIN)