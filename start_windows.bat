@echo off
title Chatterbox TTS - Local Server Setup
echo ========================================================
echo       CHATTERBOX TTS - 1-CLICK SETUP ^& LAUNCHER
echo ========================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not added to your system PATH.
    echo Please install Python 3.9 or newer from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b
)

echo [SKIP] Python is installed.
echo.

REM Check for virtual environment and create if it doesn't exist
if not exist "venv\" (
    echo [1/3] Creating a new Python virtual environment (venv)...
    python -m venv venv
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
python app.py

echo.
pause
