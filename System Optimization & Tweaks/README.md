# System Optimization & Tweaks

This directory contains powerful system optimization utilities designed to enhance Windows performance, reduce latency, and optimize system settings for improved responsiveness.

## Included Repositories:
- **UnLovedCookie--CoutX** ⚡ [Free PC optimizer written in C++ and batch to give your computer a performance boost. Includes an intuitive GUI and simple settings.](./UnLovedCookie--CoutX)

## Scripts and Utilities

### CoutX.bat - Comprehensive PC Optimizer

**Location:** `UnLovedCookie--CoutX/CoutX.bat`  
**Version:** 2.1.1  
**Requirements:** Administrator privileges required

CoutX is a comprehensive system optimization script that performs extensive Windows tweaks to improve performance, reduce latency, and enhance gaming experience.

#### Usage

```bat
cd "UnLovedCookie--CoutX"
CoutX.bat
```

#### Features and Capabilities

**Display and Graphics Optimizations:**
- Enables detailed BSOD for better debugging
- Configures GameDVR settings for optimal performance
- Enables Windows Variable Refresh Rate (VRR)
- Optimizes windowed mode performance
- Enables Hardware Accelerated GPU Scheduling
- Configures NVIDIA-specific optimizations including G-Sync
- Sets up ReBar (Resizable BAR) for supported hardware
- Configures texture filtering for performance
- Enables MSI mode for GPUs

**System Performance Tweaks:**
- Implements quick boot and shutdown configurations
- Optimizes Windows interface responsiveness
- Disables unnecessary animations
- Configures memory management settings
- Enables SSD TRIM optimization
- Optimizes NTFS file system settings
- Configures CPU scheduling priorities
- Sets up optimal network configurations

**Network Optimizations:**
- Disables Nagle's algorithm for reduced latency
- Enables Winsock autotuning
- Configures BBR2 congestion control
- Optimizes RSS (Receive Side Scaling)
- Configures network task offloading
- Sets up optimal network adapter settings
- Maximizes port ranges for improved connectivity

**Privacy and Telemetry:**
- Disables Windows telemetry collection
- Removes advertising ID tracking
- Blocks diagnostics data transmission
- Disables Cortana data collection
- Stops automatic app suggestions
- Configures privacy-focused registry settings

**Power and CPU Management:**
- Creates optimized power plans
- Configures Intel-specific power settings
- Sets up CPU interrupt steering
- Optimizes processor scheduling
- Configures multimedia class scheduler service (MMCSS)

**Storage and Memory:**
- Disables hibernation to free disk space
- Configures page file settings
- Optimizes memory decommitting thresholds
- Enables Physical Address Extension (PAE)
- Sets up optimal disk caching

**Hardware-Specific Features:**
- **NVIDIA GPUs:** Applies comprehensive driver optimizations, disables telemetry, configures profiles
- **Intel CPUs:** Applies Intel-specific power and performance tweaks
- **Network Adapters:** Configures RSS, interrupt moderation, and offloading features

#### What the Script Does

The script automatically detects your hardware configuration and applies appropriate optimizations:

1. **System Check:** Verifies administrator privileges and hardware compatibility
2. **Registry Modifications:** Applies performance-oriented registry tweaks
3. **Service Configuration:** Optimizes Windows services for performance
4. **Driver Settings:** Configures graphics and network drivers
5. **Power Management:** Sets up optimized power profiles
6. **Network Stack:** Optimizes TCP/IP settings and network adapters

#### Dependencies

The script references external tools that may enhance functionality:
- `SetTimerResolution.exe` - For timer resolution optimization
- `nvidiaProfileInspector` - For NVIDIA GPU profile management

#### Output

The script provides real-time feedback showing which optimizations are being applied:
- Display and graphics configurations
- Network optimizations
- System performance tweaks
- Hardware-specific adjustments
- Privacy and telemetry configurations

#### Compatibility

- **Operating System:** Windows 10/11
- **Architecture:** x64 systems
- **GPU Support:** NVIDIA GPUs receive additional optimizations
- **CPU Support:** Intel CPUs receive specific power optimizations