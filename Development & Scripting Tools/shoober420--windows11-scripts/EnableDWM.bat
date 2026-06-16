rem # Enable DWM

rem # Disabling Shell Infrastructure Host (sihost.exe) makes system much slower

rem # Renaming dwmapi.dll freezes system after boot

rem # https://youtu.be/K_4i6X5OAw8
rem # https://youtu.be/1iXfUThaQ1Q
rem # https://youtu.be/j6_GXujgM3Y



rem # Launch SetACL.bat to take ownership of reg keys
cd "%~dp0"
ECHO R | powershell.exe ./SetACL.bat
cd "%USERPROFILE%\Downloads"

cd "%USERPROFILE%\Downloads\windows11-scripts-main"
ECHO R | powershell.exe ./SetACL.bat
cd "%USERPROFILE%\Downloads"

cd "%USERPROFILE%\Downloads\windows11-scripts-main\windows11-scripts-main"
ECHO R | powershell.exe ./SetACL.bat
cd "%USERPROFILE%\Downloads"

cd "%USERPROFILE%\Downloads\windows11-scripts\windows11-scripts"
ECHO R | powershell.exe ./SetACL.bat
cd "%USERPROFILE%\Downloads"

cd "%USERPROFILE%\Downloads\windows11-scripts"
ECHO R | powershell.exe ./SetACL.bat
cd "%USERPROFILE%\Downloads"

TIMEOUT /T 5



rem # Restore dwm.exe (to restore run "sfc /scannow")
takeown /s %computername% /u %username% /f "C:\Windows\System32\dwm.exe"
icacls "C:\Windows\System32\dwm.exe" /grant:r %username%:F
taskkill /im dwm.exe /f
rem del "C:\Windows\System32\dwm.exe" /s /f /q
rem ren "C:\Windows\System32\dwm.exe.bak" "dwm.exe"

copy "C:\Windows\System32\dwm.exe.bak" "C:\Windows\System32\dwm.exe"

rem # Fix Black screen at login
takeown /s %computername% /u %username% /f "C:\Windows\System32\Windows.UI.logon.dll"
icacls "C:\Windows\System32\Windows.UI.logon.dll" /grant:r %username%:F
rem taskkill /im Windows.UI.logon.dll /f
rem del "C:\Windows\System32\Windows.UI.logon.dll" /s /f /q
ren "C:\Windows\System32\Windows.UI.logon.dll.bak" "Windows.UI.logon.dll"

rem # Fix Mouse
takeown /s %computername% /u %username% /f "C:\Windows\System32\dwminit.dll"
icacls "C:\Windows\System32\dwminit.dll" /grant:r %username%:F
rem taskkill /im dwminit.dll /f
rem del "C:\Windows\System32\dwminit.dll" /s /f /q
ren "C:\Windows\System32\dwminit.dll.bak" "dwminit.dll"

rem # Enable UWP apps
takeown /s %computername% /u %username% /f "C:\Windows\SystemApps" /R
icacls "C:\Windows\SystemApps" /grant:r %username%:F /T
rem del "C:\Windows\SystemApps" /s /f /q
ren "C:\Windows\SystemAppsbak" "SystemApps"

rem # Enable Resources
rem # Enable Modern Theme
takeown /s %computername% /u %username% /f "C:\Windows\Resources" /R
icacls "C:\Windows\Resources" /grant:r %username%:F /T
rem del "C:\Windows\Resources" /s /f /q
rem ren "C:\Windows\Resourcesbak" "Resources"
copy "C:\Windows\Resourcesbak" "Resources"

rem # Enable DWM DLLs
takeown /s %computername% /u %username% /f "C:\Windows\System32\dwmapi.dll"
takeown /s %computername% /u %username% /f "C:\Windows\System32\dwmcore.dll"
takeown /s %computername% /u %username% /f "C:\Windows\System32\dwmghost.dll"
takeown /s %computername% /u %username% /f "C:\Windows\System32\dwmredir.dll"
takeown /s %computername% /u %username% /f "C:\Windows\System32\dwmscene.dll"

icacls "C:\Windows\System32\dwmapi.dll" /grant:r %username%:F
icacls "C:\Windows\System32\dwmcore.dll" /grant:r %username%:F
icacls "C:\Windows\System32\dwmghost.dll" /grant:r %username%:F
icacls "C:\Windows\System32\dwmredir.dll" /grant:r %username%:F
icacls "C:\Windows\System32\dwmscene.dll" /grant:r %username%:F

rem # FREEZES SYSTEM AFTER BOOT
ren "C:\Windows\System32\dwmapi.dll.bak" "dwmapi.dll"

ren "C:\Windows\System32\dwmcore.dll.bak" "dwmcore.dll"
ren "C:\Windows\System32\dwmghost.dll.bak" "dwmghost.dll"
ren "C:\Windows\System32\dwmredir.dll.bak" "dwmredir.dll"
ren "C:\Windows\System32\dwmscene.dll.bak" "dwmscene.dll"

cd "%~dp0"

call EnableShellInfrastructureHost.bat

cd "%~dp0"

PAUSE

