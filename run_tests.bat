@echo off
title Flappy Bird Clone - Formal Acceptance Test Suite (Problem Statement No. 61)
echo ==============================================================================
echo   EXECUTING FORMAL ACCEPTANCE TEST SUITE (Problem Statement No. 61)
echo   Rungta International Skills University - School of CSE
echo ==============================================================================
echo.

IF EXIST ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" main.py --test
    goto end
)

where uv >nul 2>nul
IF %ERRORLEVEL% EQU 0 (
    uv run --with pygame-ce main.py --test
    goto end
)

python main.py --test

:end
echo.
pause
