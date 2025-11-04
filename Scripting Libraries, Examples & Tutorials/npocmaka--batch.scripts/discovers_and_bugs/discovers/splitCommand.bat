@echo off

:: https://stackoverflow.com/a/64752041/388389
:: Splits a long command into a few lines.
:: Limitations are that some special symbols should be escaped (carets, closing brackets and etc.)

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
set "{{=setlocal enableDelayedExpansion&for %%a in (" & set "}}="::end::" ) do if "%%~a" neq "::end::" (set command=!command! %%a) else (call !command! & endlocal)"
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:: Example:

%{{%
    echo
    "command"
    written
    on a
    few lines
%}}%
