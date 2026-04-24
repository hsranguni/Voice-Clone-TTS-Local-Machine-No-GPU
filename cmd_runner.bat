@echo off
echo Running inner setup script...

if not exist "venv\" (
    echo Hunting for a compatible Python version ^(3.10 recommended^)...
    py -3.10 -m venv venv 2>nul
    if not exist "venv\" (
        py -3.9 -m venv venv 2>nul
    )
    if not exist "venv\" (
        py -3.11 -m venv venv 2>nul
    )
    if not exist "venv\" (
        echo Creating virtual environment using default 'python'...
        python -m venv venv
    )
    if not exist "venv\" (
        echo Creating virtual environment using default 'py'...
        py -m venv venv
    )
)

echo Activating environment...
call venv\Scripts\activate.bat

echo Installing core requirements...
python -m pip install -r requirements.txt

echo.
echo Installing Neural Voice Cloning AI (NOTE: May take 3 to 10 minutes depending on internet speed)...
echo If this fails, the app will safely fall back to the offline computer voice.
python -m pip install TTS

echo.
echo Starting Application...
python app.py
