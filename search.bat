@REM Windows Batch File to run the basic search program

@echo off
call activate ai
if exist main.py (
    python main.py %1 -m %2
) else (
    echo Script file not found
)
pause