@REM Windows Batch File to run the search algorithm for multiple goals

@echo off
call activate ai
if exist main.py (
    python main.py %1 -m %2 -e
) else (
    echo Script file not found
)
pause