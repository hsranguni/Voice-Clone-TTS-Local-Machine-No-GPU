# Chatterbox Multilingual TTS - Local Immersive Web UI

This repository provides a complete, local web-based Text-to-Speech (TTS) system using the **Chatterbox TTS model**. It includes a modern, cyberpunk "Immersive UI" based on Gradio and React, support for inline emotion tags, large-scale character chunking (15,000+ characters), and voice cloning capabilities.

## 🌟 Key Features
1. **Immersive UI:** A deeply stylized, cyberpunk aesthetic React interface with audio waveform playback.
2. **Massive Context Window:** Safely handles up to 15,000 characters by automatically segmenting inputs into manageable chunks to prevent VRAM memory overflows.
3. **Inline Emotion Tagging:** Parse and render emotional responses locally (e.g., `[joy]Wow![/joy]`).
4. **Voice Cloning:** Immediate zero-shot voice clones via reference audio uploads.
5. **1-Click Launchers:** Fully automated setup scripts for Windows, Mac, and Linux that strictly keep your environment safely containerized and hold the Terminal open to view background processes!

## 🚀 How to Install and Run Locally

You do **not** need to manually configure terminals. We have provided automatic 1-click installer scripts!

**(Prerequisite):** You must have **Python 3.9+** installed on your computer. 

### For Windows Users
1. Export this project and extract the ZIP file to your folder/Desktop.
2. Double click **`start_windows.bat`**.
   *(Note: It uses `cmd_runner.bat` in the background to ensure your window forcibly stays open in case of errors!)*
3. It will automatically build an isolated environment, download all neural dependencies natively, and successfully launch!

### For Mac / Linux Users
1. Export and extract the ZIP file.
2. Open your terminal, navigate to the folder, and make the script executable:
   ```bash
   chmod +x start_mac_linux.sh
   ```
3. Run the launch script:
   ```bash
   ./start_mac_linux.sh
   ```
   *(If double-clicking from a file explorer natively natively supported on your OS, this script is explicitly configured using a trap catch to pause at the end so you can read any system output without the terminal blinking shut!)*

## ⚙️ Manual Integration Instructions
If you wish to link up standard Chatterbox `.safetensors` or `.pth` weights:
1. Open up `tts_model.py`.
2. Wire your custom PyTorch model into `__init__`.
3. The automatic `chunking` infrastructure is already wired safely inside `generate_speech()` to parse the entire 15k limit safely. 
