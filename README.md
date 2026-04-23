# Chatterbox Multilingual TTS - Local Immersive Web UI

This repository provides a complete, local web-based Text-to-Speech (TTS) system using the **Chatterbox TTS model**. It includes a modern, cyberpunk "Immersive UI" based on Gradio and React, support for inline emotion tags, large-scale character chunking (15,000+ characters), and voice cloning capabilities.

## 🌟 Key Features
1. **Immersive UI:** A deeply stylized, cyberpunk aesthetic React interface with audio waveform playback.
2. **Massive Context Window:** Safely handles up to 15,000 characters by automatically segmenting inputs into manageable chunks to prevent VRAM memory overflows.
3. **Inline Emotion Tagging:** Parse and render emotional responses locally (e.g., `[joy]Wow![/joy]`).
4. **Automated Dual-Engine AI:** Seamlessly falls back to lightweight, speedy offline voices (`pyttsx3`) for quick tests, but automatically downloads and implements **XTTS v2 Neural Cloning** natively if you upload a reference voice!
5. **1-Click Launchers:** Fully automated setup scripts for Windows, Mac, and Linux that strictly keep your environment safely containerized.

> **Having trouble unlocking Voice Cloning?** Check out the [REQUIREMENTS.md](./REQUIREMENTS.md) file for the exact fixes (Python 3.10 and Microsoft C++ Tools).

---

## 🚀 How to Install and Run Locally
You **never** need to manually configure terminals, run `pip install`, or use the command line directly. We have provided automatic 1-click installer scripts!

**(Prerequisite):** You must have **Python 3.9+** installed on your computer. 

### For Windows Users
**Daily Workflow:**
1. Extract the project ZIP to a folder.
2. Double-click **`start_windows.bat`**.
   *(Note: This pops open a safe terminal window that physically stays open to prevent crashing.)*
3. **The First Time Only:** It will spend 5-10 minutes downloading the heavy Voice Cloning neural network libraries (`XTTS v2`, `PyTorch`) and creating a safe `venv` folder.
4. **Every Time After That:** It will see the `venv` folder, skip the download, and boot up your app in **2 seconds**.
5. Once it says `Running on local URL: http://127.0.0.1:7860`, open that exact link in Chrome/Edge.
6. When you are done using the TTS engine, simply click the "X" on the black terminal window to turn the engine off.

### For Mac / Linux Users
**Daily Workflow:**
1. Extract the project ZIP to a folder.
2. Open your terminal, navigate to the folder, and run:
   ```bash
   chmod +x start_mac_linux.sh
   ./start_mac_linux.sh
   ```
3. It will safely build out a `.venv` sandbox and install Torch/Gradio matrices.
4. Open the `http://127.0.0.1:7860` address provided in your terminal.
5. Press `CTRL+C` or close the terminal when you are finished!

---

## 🛠️ Modifying the UI or Engine
* **UI Theme:** Go to `src/App.tsx` and run `npm run dev` to play with the React/Tailwind frontend.
* **TTS Logic:** Open up `tts_model.py`. This is where you can wire your actual PyTorch model weights directly into the chunking engine. The chunking infrastructure is heavily documented for easy swapping!
