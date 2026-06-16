rem # SystemApps (UWP apps)

rem # REQUIRES WINRE ENVIRONMENT

rem # Microsoft.WindowsAppRuntime.vNext.CBS contains File Explorer

rem # Microsoft.UI.Xaml.CBS causes constant screen flicker and blinking when removed

rem # MicrosoftWindows.Client.Core causes black screen after login when removed



cd "%USERPROFILE%\Downloads\SetACL (executable version)\64 bit"

SetACL.exe -on "C:\Windows\SystemApps" -ot file -actn setowner -ownr n:"n:Administrators" -rec cont_obj

SetACL.exe -on "C:\Windows\SystemApps" -ot file -actn ace -ace "n:Administrators;p:full" -rec cont_obj

cd "%~dp0"



@echo off

echo.
echo UWP Apps (SystemApps)
echo REQUIRES WINRE ENVIRONMENT
echo.
echo 1. Disable UWP Apps
echo 2. Enable UWP Apps
echo 3. SKIP
echo C. Cancel
echo.
choice /c 123C /m "Choose an option :"

if 4 EQU %ERRORLEVEL% (
   echo User chose to cancel.
) else if 3 EQU %ERRORLEVEL% (
   call :zkepp
) else if 2 EQU %ERRORLEVEL% (
   call :uwpon
) else if 1 EQU %ERRORLEVEL% (
   call :uwpoff
) else if 0 EQU %ERRORLEVEL% (
   echo User bailed out.
)

goto :eof

:uwpoff
echo User chose Disable UWP Apps

rem # Disable UWP apps
takeown /s %computername% /u %username% /f "C:\Windows\SystemApps" /R
icacls "C:\Windows\SystemApps" /grant:r %username%:F /T
rem del "C:\Windows\SystemApps" /s /f /q
rem copy "C:\Windows\SystemApps" "C:\Windows\SystemAppsbak"
ren "C:\Windows\SystemApps" "SystemAppsbak"

goto :end

:uwpon
echo User chose Enable UWP Apps

rem # Enable UWP apps
takeown /s %computername% /u %username% /f "C:\Windows\SystemApps" /R
icacls "C:\Windows\SystemApps" /grant:r %username%:F /T
rem del "C:\Windows\SystemApps" /s /f /q
rem copy "C:\Windows\SystemAppsbak" "C:\Windows\SystemApps"
ren "C:\Windows\SystemAppsbak" "SystemApps"


goto :end

:zkepp
echo User chose SKIP

goto :end

:end

PAUSE