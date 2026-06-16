rem # SetResolution

rem # -f sets refresh rate (-f 60)



@echo off



echo.
echo SetResolution
echo.
echo 1. 640 x 480
echo 2. 800 x 600
echo 3. 1024 x 768
echo 4. 1280 x 960
echo 5. 1600 x 1200
echo 6. 1366 x 768
echo 7. 1920 x 1080
echo 8. 3840 x 2160
echo C. Cancel
echo.
choice /c 123456789C /m "Choose an option :"

if 9 EQU %ERRORLEVEL% (
   echo User chose to cancel.
) else if 8 EQU %ERRORLEVEL% (
   call :3840
) else if 7 EQU %ERRORLEVEL% (
   call :1920
) else if 6 EQU %ERRORLEVEL% (
   call :1366
) else if 5 EQU %ERRORLEVEL% (
   call :1600
) else if 4 EQU %ERRORLEVEL% (
   call :1280
) else if 3 EQU %ERRORLEVEL% (
   call :1024
) else if 2 EQU %ERRORLEVEL% (
   call :800
) else if 1 EQU %ERRORLEVEL% (
   call :640
) else if 0 EQU %ERRORLEVEL% (
   echo User bailed out.
)

goto :eof

:640
echo User chose 640 x 480

cd "%USERPROFILE%\Downloads"

sr SET -w 640 -h 480 -b 32 -o 0

goto :end



:800
echo User chose 800 x 600

cd "%USERPROFILE%\Downloads"

sr SET -w 800 -h 600 -b 32 -o 0

goto :end



:1024
echo User chose 1024 x 768

cd "%USERPROFILE%\Downloads"

sr SET -w 1024 -h 768 -b 32 -o 0

goto :end



:1280
echo User chose 1280 x 960

cd "%USERPROFILE%\Downloads"

sr SET -w 1280 -h 960 -b 32 -o 0

goto :end



:1600
echo User chose 1600 x 1200

cd "%USERPROFILE%\Downloads"

sr SET -w 1600 -h 1200 -b 32 -o 0

goto :end



:1366
echo User chose 1366 x 768

cd "%USERPROFILE%\Downloads"

sr SET -w 1366 -h 768 -b 32 -o 0

goto :end



:1920
echo User chose 1920 x 1080

cd "%USERPROFILE%\Downloads"

sr SET -w 1920 -h 1080 -b 32 -o 0

goto :end



:3840
echo User chose 3840 x 2160

cd "%USERPROFILE%\Downloads"

sr SET -w 3840 -h 2160 -b 32 -o 0

goto :end

:end

