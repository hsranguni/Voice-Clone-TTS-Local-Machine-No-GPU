# ⚠️ Prerequisites & Troubleshooting for Voice Cloning

If you want to use the **Basic Offline Computer Voice**, you only need any version of Python. 

However, if you want to unlock the **Deep Neural Voice Cloning (XTTS v2)** and **Emotion Prosody**, your Windows computer *must* have two specific developer dependencies installed. If you are seeing the ⚠️ BASIC OFFLINE MODE ACTIVE banner, follow these steps to fix your computer's environment!

---

## 1. Python 3.10 is Strictly Required
The neural AI models that power Voice Cloning currently **do not support** Python 3.12 or 3.13. You must install exactly Python 3.10.

1. **Download:** [Click Here to Download Python 3.10.11 for Windows](https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe)
2. **Install:** Run the downloaded `.exe` file.
3. 🚨 **CRITICAL:** Before you click "Install Now", you **MUST** check the box at the very bottom that says **"Add Python 3.10 to PATH"**. If you skip this, Windows will not know Python exists.
4. Click "Install Now".

---

## 2. Microsoft Visual C++ Build Tools & Redistributable
Because Voice Cloning uses deep learning frameworks (`PyTorch`) and raw C++ code to process audio at lightning speeds, Windows needs to know how to "compile" and execute C++ code.

If you don't have this, you will see a red error in your terminal saying `error: Microsoft Visual C++ 14.0 or greater is required` OR `OSError: [WinError 1114] A dynamic link library (DLL) initialization routine failed`.

**Part A: The C++ Build Tools**
1. **Download:** [Click Here to get Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
2. Click the **"Download Build Tools"** button on that website and run the installer.
3. 🚨 **CRITICAL:** A window will pop up asking what you want to install. You **MUST** check the box in the top-left corner that says **"Desktop development with C++"**.
4. Click **Install** in the bottom right corner. *(Note: This is a few gigabytes and may take 5-10 minutes).*

**Part B: The C++ Runtime Library (Crucial for PyTorch)**
If the engine installed successfully but instantly crashed when booting up the UI with a "PyTorch DLL WinError 1114", your computer is missing the core runtime libraries.
1. **Download:** [Click Here to get the vc_redist.x64.exe (Official Microsoft Link)](https://aka.ms/vs/17/release/vc_redist.x64.exe)
2. Run the downloaded file and install it.

**Restart your computer** once you finish installing these to ensure Windows registers the new C++ compilers.

---

## 3. How to Reset and Try Again
If you had the wrong Python version or were missing C++ tools the first time you ran the app, your project folder will contain a broken `venv` (Virtual Environment). 

To fix this and trigger a clean installation:
1. Open your project folder.
2. Select the **`venv`** folder and **Delete it**.
3. Double-click **`start_windows.bat`** again.

The setup script will now automatically detect your correct Python 3.10 and C++ compilers, successfully download the 2.5 GB neural networks, and launch the UI with the **✅ NEURAL ENGINE ACTIVE** banner!
