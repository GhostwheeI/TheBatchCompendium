@echo off
setlocal ENABLEDELAYEDEXPANSION

if not exist "tools" mkdir tools

for /D %%F in (*) do (
    if /I not "%%F"=="tools" if /I not "%%F"==".git" (
        move "%%F" "tools\%%F"
    )
)

echo Done moving folders into 'tools'.
pause
