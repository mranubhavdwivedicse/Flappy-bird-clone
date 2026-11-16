@echo off
title Flappy Bird Clone - Formal Acceptance Test Suite
echo ==============================================================================
echo Executing Formal Acceptance Test Suite (Problem Statement No. 61)
echo ==============================================================================

IF EXIST ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" main.py --test
    goto end
)

python main.py --test

:end
echo.
pause
