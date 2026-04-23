#!/bin/bash
echo "Starting Chatterbox TTS Setup..."
echo "Please wait..."

# Function to pause before exiting so the terminal doesn't close immediately if run via double-click
pause_on_exit() {
    echo ""
    read -p "Press [Enter] to close this window..."
    exit
}

# Trap unexpected errors
trap 'echo "[ERROR] An unexpected error occurred."; pause_on_exit' ERR

# 1. Check Python
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python3 is not installed or not in your PATH."
    pause_on_exit
fi

# 2. Activate venv or create it
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "[ERROR] Failed to create virtual environment. Do you have python3-venv installed?"
        pause_on_exit
    fi
fi

echo "Activating environment..."
source venv/bin/activate

# 3. Install requirements
echo "Installing core requirements..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to install core requirements."
    pause_on_exit
fi

echo ""
echo "Installing Neural Voice Cloning AI (NOTE: May take 3 to 10 minutes depending on internet speed)..."
echo "If this fails, the app will safely fall back to the offline computer voice."
python3 -m pip install TTS

echo ""
# 4. Run the app
echo "Launching App..."
python3 app.py

# Keep window open after app closes
pause_on_exit