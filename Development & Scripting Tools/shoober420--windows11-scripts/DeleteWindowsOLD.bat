rem # Delete Windows.old directory

cd "%USERPROFILE%\Downloads\SetACL (executable version)\64 bit"

SetACL.exe -on "C:\Windows.old" -ot file -actn setowner -ownr "n:Administrators" -rec cont_obj

SetACL.exe -on "C:\Windows.old" -ot file -actn ace -ace "n:Administrators;p:full" -rec cont_obj

cd "%~dp0"



takeown /s %computername% /u %username% /f "C:\Windows.old"
icacls "C:\Windows.old" /grant:r %username%:F
rem ren "C:\Windows.old" "C:\Windows.old.bak"
del "C:\Windows.old" /s /f /q
rmdir "C:\Windows.old" /s /q

PAUSE