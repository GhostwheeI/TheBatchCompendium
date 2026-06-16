rem # Disable DWM

rem # Disabling Shell Infrastructure Host (sihost.exe) makes system much slower

rem # Disabling DWM borks admin rights

rem # Renaming dwmapi.dll freezes system after boot

rem # https://youtu.be/K_4i6X5OAw8
rem # https://youtu.be/1iXfUThaQ1Q
rem # https://youtu.be/j6_GXujgM3Y

rem # SystemApps REQUIRES WINRE ENVIRONMENT

rem # CLASSIC THEME MUST BE ENABLED OR GAMES RUN SLOW WHEN DWM IS DISABLED



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



rem # Backup dwm.exe (to restore run "sfc /scannow")
takeown /s %computername% /u %username% /f "C:\Windows\System32\dwm.exe"
icacls "C:\Windows\System32\dwm.exe" /grant:r %username%:F
rem taskkill /im dwm.exe /f
rem del "C:\Windows\System32\dwm.exe" /s /f /q
ren "C:\Windows\System32\dwm.exe" "dwm.exe.bak"

copy "C:\Windows\System32\cmd.exe" "C:\Windows\System32\dwm.exe"

call SystemApps.bat

call ClassicTheme.bat

rem # Fix Black Screen at Login
takeown /s %computername% /u %username% /f "C:\Windows\System32\Windows.UI.logon.dll"
icacls "C:\Windows\System32\Windows.UI.logon.dll" /grant:r %username%:F
rem taskkill /im Windows.UI.logon.dll /f
rem del "C:\Windows\System32\Windows.UI.logon.dll" /s /f /q
ren "C:\Windows\System32\Windows.UI.logon.dll" "Windows.UI.logon.dll.bak"

rem # Fix Mouse
takeown /s %computername% /u %username% /f "C:\Windows\System32\dwminit.dll"
icacls "C:\Windows\System32\dwminit.dll" /grant:r %username%:F
rem taskkill /im dwminit.dll /f
rem del "C:\Windows\System32\dwminit.dll" /s /f /q
ren "C:\Windows\System32\dwminit.dll" "dwminit.dll.bak"



@echo off



echo.
echo Shell Infrastructure Host (sihost.exe)
echo.
echo 1. Disable Shell Infrastructure Host (sihost.exe) (SLOW SYSTEM)
echo 2. Enable Shell Infrastructure Host (sihost.exe) (RECOMMENDED)
echo 3. SKIP
echo C. Cancel
echo.
choice /c 123C /m "Choose an option :"

if 4 EQU %ERRORLEVEL% (
   echo User chose to cancel.
) else if 3 EQU %ERRORLEVEL% (
   call :zkepppp
) else if 2 EQU %ERRORLEVEL% (
   call :sion
) else if 1 EQU %ERRORLEVEL% (
   call :sioff
) else if 0 EQU %ERRORLEVEL% (
   echo User bailed out.
)

goto :eof

:sioff
echo User chose Disable Shell Infrastructure Host (sihost.exe) (SLOW SYSTEM)

cd "%~dp0"
call DisableShellInfrastructureHost.bat

goto :end

:sion
echo User chose Enable Shell Infrastructure Host (sihost.exe) (RECOMMENDED)

cd "%~dp0"
call EnableShellInfrastructureHost.bat

goto :end

:zkepppp
echo User chose SKIP

goto :end

:end



echo.
echo DWM DLLs
echo.
echo 1. Disable DWM DLLs
echo 2. Enable DWM DLLs
echo 3. SKIP
echo C. Cancel
echo.
choice /c 123C /m "Choose an option :"

if 4 EQU %ERRORLEVEL% (
   echo User chose to cancel.
) else if 3 EQU %ERRORLEVEL% (
   call :zkeppppp
) else if 2 EQU %ERRORLEVEL% (
   call :dllon
) else if 1 EQU %ERRORLEVEL% (
   call :dlloff
) else if 0 EQU %ERRORLEVEL% (
   echo User bailed out.
)

goto :eof

:dlloff
echo User chose Disable DWM DLLs

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
rem ren "C:\Windows\System32\dwmapi.dll" "dwmapi.dll.bak"

ren "C:\Windows\System32\dwmcore.dll" "dwmcore.dll.bak"
ren "C:\Windows\System32\dwmghost.dll" "dwmghost.dll.bak"
ren "C:\Windows\System32\dwmredir.dll" "dwmredir.dll.bak"
ren "C:\Windows\System32\dwmscene.dll" "dwmscene.dll.bak"

goto :end

:dllon
echo User chose Enable DWM DLLs

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

goto :end

:zkeppppp
echo User chose SKIP

goto :end

:end

PAUSE



rem # Disabling dwminit.dll is required when using DWM and disabling "Windows\Resources" or screen flickers then turns black

rem # DWM: OFF / sihost: OFF / Resources: OFF / SystemApps: ON = GAME CRASH / VERY SLOW

rem # DWM: OFF / sihost: ON / Resources: OFF / SystemApps: ON = SYSTEM BROKEN

rem # DWM: OFF / sihost: OFF / Resources: OFF / SystemApps: OFF = GAME CRASH / VERY SLOW

rem # DWM: OFF / sihost: ON / Resources: OFF / SystemApps: OFF = WORKS (GAME BROKEN ON VANILLA SYSTEM)

rem # DWM: ON / sihost: ON / Resources: OFF / SystemApps: OFF = SYSTEM BROKEN

rem # DWM: ON / sihost: OFF / Resources: OFF / SystemApps: OFF = SYSTEM BROKEN

rem # DWM: ON / sihost: OFF / Resources: ON / SystemApps: OFF = WORKS

rem # DWM: ON / sihost: ON / Resources: ON / SystemApps: OFF = WORKS
