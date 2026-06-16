rem # Windows.UI.login.dll

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



@echo off

echo.
echo Windows.UI.login.dll
echo.
echo 1. Terminal Login
echo 2. Default Login
echo 3. SKIP
echo.
choice /c 123C /m "Choose an option :"

if 4 EQU %ERRORLEVEL% (
   echo User chose to cancel.
) else if 3 EQU %ERRORLEVEL% (
   call :zcepe
) else if 2 EQU %ERRORLEVEL% (
   call :termoff
) else if 1 EQU %ERRORLEVEL% (
   call :termon
) else if 0 EQU %ERRORLEVEL% (
   echo User bailed out.
)

goto :eof

:termon
echo User chose Terminal Login ON

rem # Fix Black Screen at Login
takeown /s %computername% /u %username% /f "C:\Windows\System32\Windows.UI.logon.dll"
icacls "C:\Windows\System32\Windows.UI.logon.dll" /grant:r %username%:F
rem taskkill /im Windows.UI.logon.dll /f
rem del "C:\Windows\System32\Windows.UI.logon.dll" /s /f /q
ren "C:\Windows\System32\Windows.UI.logon.dll" "Windows.UI.logon.dll.bak"

goto :end

:termoff
echo User chose Default Login

rem # Fix Black screen at login
takeown /s %computername% /u %username% /f "C:\Windows\System32\Windows.UI.logon.dll"
icacls "C:\Windows\System32\Windows.UI.logon.dll" /grant:r %username%:F
rem taskkill /im Windows.UI.logon.dll /f
rem del "C:\Windows\System32\Windows.UI.logon.dll" /s /f /q
ren "C:\Windows\System32\Windows.UI.logon.dll.bak" "Windows.UI.logon.dll"

goto :end

:zcepe
echo User chose SKIP

goto :end

:end

PAUSE