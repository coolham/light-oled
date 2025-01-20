@echo off

REM Clear .log files
for /r %%i in (*.log) do (
    del /f /q "%%i"
)

REM Clear directories using a subroutine
call :ClearDirectory "__pycache__"
call :ClearDirectory ".pytest_cache"
call :ClearDirectory "build"
call :ClearDirectory "dist"
call :ClearDirectory "light-oled/build"
call :ClearDirectory "light-oled/dist"


echo Cleanup complete!
goto :eof

REM Subroutine to clear directories
:ClearDirectory
for /r /d %%d in (*%~1*) do (
    rd /s /q "%%d"
)
goto :eof
