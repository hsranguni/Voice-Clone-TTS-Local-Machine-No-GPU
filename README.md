# Chatterbox Multilingual TTS - Local Web Interface

This repository provides a complete, local web-based Text-to-Speech (TTS) system using the **Chatterbox TTS model**. It includes a modern [Gradio](https://gradio.app/) interface, support for inline emotion tags, and voice cloning capabilities.

## 🌟 Key Features

1. **Multilingual Support:** Ready to interface with Chatterbox's 23 language capabilities.
2. **Inline Emotion Tagging:** Parse and render emotional responses directly from text using easy syntax like `[happy]Wow![/happy]`.
3. **Voice Cloning:** Create immediate voice clones by uploading a short reference `.wav` or `.mp3` file.
4. **Emotion Exaggeration Control:** Dynamically adjust the strength of the emotions using the UI slider.
5. **Local Management:** All inputs and output `.wav` files are maintained strictly on your local machine in the `outputs/` folder.

## ⚙️ Setup Instructions

### 1. Requirements

Ensure you have Python 3.9+ installed.

### 2. Install Dependencies

You can install all necessary packages primarily configured in `requirements.txt`:

```bash
pip install -r requirements.txt
```

*Note: Ensure you have `ffmpeg` installed on your host system if you intend to process a variety of audio formats (like specialized mp3s).*

### 3. Integrate Your Chatterbox Model Weights

This codebase is a modular container template. By default, it runs dummy tensor operations so the interface works out of the box.

To hook up your actual model:
1. Open `tts_model.py`.
2. Map your Chatterbox model initialization in the `__init__` function.
3. Replace the `create_voice_profile(...)` dummy code with actual feature/embedding extraction over `reference_audio_path`.
4. Send the returned parameters alongside `parsed_segments` in `generate_speech(...)` to complete the forward pass.

### 4. Running the Web Interface

Simply run `app.py`:

```bash
python app.py
```

Open the local network URL (typically `http://127.0.0.1:7860/`) in your browser to interact with the application.

## 📝 Example Prompts

Try prompting the interface with emotional shifts:

> "[sad]I waited for the bus in the rain for over an hour.[/sad] [happy]But then my best friend drove by and offered me a ride![/happy]"

Use the emotion intensity slide to see how exaggeration control scales the final output.
