@echo off
title Flappy Bird Clone - RISU B.Tech CSE (Problem Statement 61)
echo ==============================================================================
echo Launching Flappy Bird Clone (60 FPS Arcade Engine)
echo Controls: [SPACE] Flap / Restart  ^|  [P] Pause  ^|  [M] Mute  ^|  [ESC] Quit
echo ==============================================================================

IF EXIST ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" main.py
    goto end
)

where uv >nul 2>nul
IF %ERRORLEVEL% EQU 0 (
    uv run --python 3.12 --with pygame python main.py
    goto end
)

python main.py

:end
pause
