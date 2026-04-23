@echo off
title Chatterbox TTS - Local Server Setup
echo ========================================================
echo       CHATTERBOX TTS - 1-CLICK SETUP ^& LAUNCHER
echo ========================================================
echo.

set PYTHON_CMD=python

REM Check if 'python' is installed and in PATH
python --version >nul 2>&1
if %errorlevel% neq 0 (
    REM Fallback: check if the 'py' launcher works (common on Windows)
    py --version >nul 2>&1
    if %errorlevel% equ 0 (
        set PYTHON_CMD=py
    ) else (
        echo [ERROR] Python is not recognized in your system PATH.
        echo Even though Python is installed, Windows cannot find it.
        echo.
        echo FIX INSTRUCTIONS:
        echo 1. Open the Windows Start Menu, search for your Python Installer and run it.
        echo 2. Choose "Modify" setup.
        echo 3. Check the box that says "Add Python to environment variables" or "Add Python to PATH".
        echo 4. Finish the setup and try running this script again.
        echo.
        pause
        exit /b
    )
)

echo [SKIP] Python found (%PYTHON_CMD%).
echo.

REM Check for virtual environment and create if it doesn't exist
if not exist "venv\" (
    echo [1/3] Creating a new Python virtual environment (venv)...
    %PYTHON_CMD% -m venv venv
) else (
    echo [1/3] Virtual environment already exists.
)

echo.
echo [2/3] Activating virtual environment and installing/updating dependencies...
call venv\Scripts\activate
pip install -r requirements.txt

echo.
echo [3/3] Setup complete! Starting the Chatterbox TTS neural engine...
echo ========================================================
%PYTHON_CMD% app.py

echo.
pause
