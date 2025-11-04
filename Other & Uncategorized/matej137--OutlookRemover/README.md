# Outlook (New) Permanent Removal Script

This script prevents the Outlook (new) app from installing by installing a custom blank app with the same package id as the original one, thus making its installation fail. To do this, it enables the developer mode via registry and registers the modified New Outlook manifest as an unpacked Appx package. It even supports the 32 Bit version of Windows for the 5 or so people out there that are still using it.

## Original Repository

This collection is from [matej137/OutlookRemover](https://github.com/matej137/OutlookRemover)

## How to use it?

1. Unpack the ZIP file (if you didn't already)
2. Run the `Outlook.bat` batch file as an Admin
3. DONE! You can now remove the files

## How exactly does it work?

1. It checks the CPU architecture
2. Copies the correct AppxManifest.xml to the \Users folder
3. Enables developer mode (i.e. sideloading apps) via registry
4. Uninstalls the New Outlook (if present)
5. Installs the fake one

## How to remove it?

1. Open settings > apps
2. Find "Outlook (new)" > click uninstall
3. You can now download the new Outlook from the Windows store

## Issues when removing the original new outlook?

1. Open settings > apps
2. Find "Outlook (new)" > click uninstall
3. Run the script again (now disregard any errors at this step)

## Files Included

- `Outlook.bat` - Main removal script
- `AppxManifest.xml` - Manifest for 64-bit systems
- `AppxManifestx86.xml` - Manifest for 32-bit systems
- `AppxManifest-ARM64.xml` - Manifest for ARM64 systems
