@echo off
title Flappy Bird Clone - RISU B.Tech CSE (Problem Statement No. 61)
echo ==============================================================================
echo   FLAPPY BIRD CLONE - 60 FPS SENIOR ARCADE ENGINE
echo   Problem Statement No. 61 (Rungta International Skills University)
echo ==============================================================================
echo   Controls:
echo     [SPACE] or [UP] or [Click] : Flap / Start / Replay
echo     [P]                        : Pause / Resume
echo     [M]                        : Toggle Audio Mute / Unmute
echo     [R]                        : Instant Reset
echo     [T]                        : Run Acceptance Test Suite in Terminal
echo     [ESC]                      : Exit Game
echo ==============================================================================
echo.

IF EXIST ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" main.py
    goto end
)

where uv >nul 2>nul
IF %ERRORLEVEL% EQU 0 (
    uv run --with pygame main.py
    goto end
)

python main.py

:end
echo.
echo Game session ended.
pause
