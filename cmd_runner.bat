@echo off
echo Running inner setup script...

if not exist "venv\" (
    echo Creating virtual environment using 'python'...
    python -m venv venv
    if not exist "venv\" (
        echo Creating virtual environment using 'py'...
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
