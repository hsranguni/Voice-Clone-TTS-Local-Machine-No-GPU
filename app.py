import os
import gradio as gr
from tts_model import ChatterboxTTS

# Initialize the Chatterbox wrapper
# Output directory to manage local generations
OUTPUT_DIR = "outputs"
tts_backend = ChatterboxTTS(output_dir=OUTPUT_DIR)

def generate_tts(text_input, reference_audio, intensity):
    """
    Function bound to the Gradio interface to handle TTS generation requests.
    """
    if not text_input.strip():
        raise gr.Error("Please enter some text to generate speech.")
        
    voice_profile = None
    if reference_audio is not None:
        try:
            # reference_audio comes as a file path in Gradio's standard filepath format
            voice_profile = tts_backend.create_voice_profile(reference_audio)
        except Exception as e:
            raise gr.Error(f"Error during voice cloning: {str(e)}")
            
    try:
        output_filepath = tts_backend.generate_speech(
            text=text_input, 
            voice_profile=voice_profile, 
            emotion_intensity=intensity
        )
        return output_filepath
    except Exception as e:
        raise gr.Error(f"Error generating speech: {str(e)}")

# ==========================================
# Gradio Web Interface Layout
# ==========================================
with gr.Blocks(title="Chatterbox Local TTS", theme=gr.themes.Default(primary_hue="blue")) as demo:
    gr.Markdown("# 🗣️ Chatterbox Multilingual TTS")
    
    # State Banner to inform the user exactly what engine is running
    if tts_backend.has_neural_clone:
        gr.Markdown(
            "✅ **NEURAL ENGINE ACTIVE**: Full XTTS Voice Cloning and Deep Emotion Prosody unlocked."
        )
    else:
        gr.Markdown(
            "⚠️ **BASIC OFFLINE MODE ACTIVE**: The neural cloning engine failed to install (Likely because you have Python 3.12+ instead of Python 3.10). "
            "App is falling back to standard Windows/Mac robotic voices. **Voice Cloning is disabled.**"
        )
    
    with gr.Row():
        with gr.Column(scale=2):
            text_input = gr.Textbox(
                label="Text Input (Use Emotion Tags - Max 15,000 characters)",
                placeholder="Example: [happy]Hello there! I am so excited![/happy] But honestly, [sad]I'm a bit tired today.[/sad]",
                lines=10,
                max_lines=30,
                info="Generates chunks dynamically. Supports up to ~15,000 characters.",
            )
            
            with gr.Accordion("Supported Emotion Tags", open=False):
                gr.Markdown(
                    "- `[happy]...[/happy]`\n"
                    "- `[sad]...[/sad]`\n"
                    "- `[angry]...[/angry]`\n"
                    "- `[surprised]...[/surprised]`\n"
                    "- `[fear]...[/fear]`\n\n"
                    "*Text without tags is processed as 'neutral'.*"
                )
                
            intensity_slider = gr.Slider(
                minimum=0.1, 
                maximum=2.0, 
                value=1.0, 
                step=0.1, 
                label="Emotion Context (Impacts Neural output generation)"
            )
            
        with gr.Column(scale=1):
            reference_audio = gr.Audio(
                label="Voice Cloning (Reference Audio)",
                type="filepath",
                interactive=tts_backend.has_neural_clone,
                visible=tts_backend.has_neural_clone
            )
            
            if not tts_backend.has_neural_clone:
                gr.Markdown(
                    "> **Unlock Voice Cloning:** Install **Python 3.10.x** from python.org, delete this folder's `venv` so it resets, and double-click `start_windows.bat` again!"
                )
            
            generate_btn = gr.Button("🎤 Generate Speech", variant="primary")
            
    with gr.Row():
        output_audio = gr.Audio(label="Generated Audio Output", type="filepath", interactive=False)

    generate_btn.click(
        fn=generate_tts,
        inputs=[text_input, reference_audio, intensity_slider],
        outputs=output_audio
    )

if __name__ == "__main__":
    print("Starting Chatterbox Gradio Interface...")
    # For local execution, setting server_name to "127.0.0.1"
    # Launching share=False keeps it strictly local
    demo.launch(server_name="127.0.0.1", server_port=7860, share=False)
