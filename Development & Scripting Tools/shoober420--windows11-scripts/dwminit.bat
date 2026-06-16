rem # dwminit.dll

@echo off



echo.
echo dwminit.dll
echo.
echo 1. Disable dwminit.dll (RECOMMENDED)
echo 2. Enable dwminit.dll
echo C. Cancel
echo.
choice /c 123C /m "Choose an option :"

if 3 EQU %ERRORLEVEL% (
   echo User chose to cancel.
) else if 2 EQU %ERRORLEVEL% (
   call :initon
) else if 1 EQU %ERRORLEVEL% (
   call :initoff
) else if 0 EQU %ERRORLEVEL% (
   echo User bailed out.
)

goto :eof

:initoff
echo User chose Disable dwminit.dll (RECOMMENDED)

rem # Fix Mouse
takeown /s %computername% /u %username% /f "C:\Windows\System32\dwminit.dll"
icacls "C:\Windows\System32\dwminit.dll" /grant:r %username%:F
rem taskkill /im dwminit.dll /f
rem del "C:\Windows\System32\dwminit.dll" /s /f /q
ren "C:\Windows\System32\dwminit.dll" "dwminit.dll.bak"

goto :end

:initon
echo User chose Enable dwminit.dll

rem # Fix Mouse
takeown /s %computername% /u %username% /f "C:\Windows\System32\dwminit.dll"
icacls "C:\Windows\System32\dwminit.dll" /grant:r %username%:F
rem taskkill /im dwminit.dll /f
rem del "C:\Windows\System32\dwminit.dll" /s /f /q
ren "C:\Windows\System32\dwminit.dll.bak" "dwminit.dll"

goto :end

:end

PAUSE