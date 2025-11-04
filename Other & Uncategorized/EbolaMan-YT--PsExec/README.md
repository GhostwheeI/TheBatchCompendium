# PsExec Batch File

## About

A batch file implementation inspired by Microsoft's Sysinternals PsExec tool. This script provides enhanced remote administration capabilities for Windows systems.

## Original Repository

This collection is from [EbolaMan-YT/PsExec](https://github.com/EbolaMan-YT/PsExec)

## Description

This is an enhanced batch file version of PsExec, designed to facilitate remote connections and operations on Windows systems. The script provides an improved and user-friendly interface for remote system administration tasks.

## Features

The `psexec.bat` script allows for various remote operations including:

- Opening remote shells
- Transferring files between systems
- Gathering system information remotely
- Shutting down remote machines
- Administrative operations over SMB and WinRM protocols
- Interactive menu for remote actions after connection

## How It Works

1. The script checks for WinRM availability on the target machine
2. Configures WinRM if necessary
3. Establishes a connection to the remote system
4. Provides an interactive menu for performing administrative tasks

## Requirements

- Windows operating system
- Administrator privileges
- WinRM enabled on target systems (script can configure this)
- Network connectivity to target machines
- Appropriate credentials for remote systems

## Usage

⚠️ **Important Security Notice**

This tool is intended for:
- Legitimate system administration tasks
- Authorized security testing and penetration testing
- Educational purposes in controlled environments

**WARNING**: Using this tool on systems you do not own or without explicit authorization is illegal and unethical. Always ensure you have proper authorization before running remote administration tools.

## Legal and Ethical Considerations

- Only use on systems you own or have explicit permission to access
- Comply with all applicable laws and regulations
- Follow your organization's security policies
- Use responsibly and ethically

## Files Included

- `psexec.bat` - Main batch script for remote administration
- `files/` - Supporting files directory

## Author

Created by EbolaMan-YT for educational and administrative purposes.

## Disclaimer

This tool is provided "as is" without warranty of any kind. The author is not responsible for any misuse or damage caused by this software. Users are solely responsible for ensuring their use complies with all applicable laws and regulations.
