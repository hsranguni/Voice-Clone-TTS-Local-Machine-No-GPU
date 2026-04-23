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

echo Installing requirements...
python -m pip install -r requirements.txt

echo Starting Application...
python app.py
