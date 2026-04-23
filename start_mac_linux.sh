#!/bin/bash

echo "========================================================"
echo "      CHATTERBOX TTS - 1-CLICK SETUP & LAUNCHER"
echo "========================================================"
echo ""

# Check if Python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python3 is not installed."
    echo "Please install Python 3.9 or newer."
    exit 1
fi

echo "[SKIP] Python3 is installed."
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "[1/3] Creating a new Python virtual environment (venv)..."
    python3 -m venv venv
else
    echo "[1/3] Virtual environment already exists."
fi

echo ""
echo "[2/3] Activating virtual environment and installing/updating dependencies..."
source venv/bin/activate
pip install -r requirements.txt

echo ""
echo "[3/3] Setup complete! Starting the Chatterbox TTS neural engine..."
echo "========================================================"
python3 app.py
