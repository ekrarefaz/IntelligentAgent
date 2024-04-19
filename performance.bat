@REM Windows Batch File to run the performance testing extension against a specified grid

@echo off
call activate ai
if exist main.py (
    python main.py %1 -p
) else (
    echo Script file not found
)
pause