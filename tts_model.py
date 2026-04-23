import os
import re
import uuid
import wave
import contextlib
import numpy as np
import scipy.io.wavfile as wavfile
from typing import List, Tuple, Dict, Any

class ChatterboxTTS:
    """
    A wrapper class for the Chatterbox Multilingual TTS model.
    Handles basic offline TTS fallback, OR loads massive Neural Voice Cloning models (XTTS v2).
    """

    def __init__(self, output_dir: str = "outputs"):
        """
        Initializes the ChatterboxTTS model parameters.
        """
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir, exist_ok=True)
            
        print("Checking for Neural Voice Cloning Engine (Coqui TTS)...")
        # Attempt to load the real Voice Cloning Model
        try:
            os.environ["COQUI_TOS_AGREED"] = "1"
            import torch
            from TTS.api import TTS
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
            print(f"Loading Real Voice Cloning AI on {self.device.upper()}! (This will download ~2GB of weights if first time)")
            self.model = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(self.device)
            self.has_neural_clone = True
        except ImportError:
            print("[NOTICE] Neural Cloning Engine 'TTS' not installed.")
            print("[NOTICE] Falling back to standard Windows/Mac built-in offline voice.")
            import pyttsx3
            # Initialize offline fallback engine
            self.engine = pyttsx3.init()
            self.has_neural_clone = False

    def parse_emotion_tags(self, text: str) -> List[Tuple[str, str]]:
        """Parses input text for inline emotion tags like [happy]Hello![/happy]."""
        pattern = re.compile(r'\[(.*?)\](.*?)\[/\1\]')
        segments = []
        last_idx = 0
        for match in pattern.finditer(text):
            if match.start() > last_idx:
                neutral_text = text[last_idx:match.start()].strip()
                if neutral_text:
                    segments.append(("neutral", neutral_text))
            emotion = match.group(1).lower()
            content = match.group(2).strip()
            segments.append((emotion, content))
            last_idx = match.end()
        if last_idx < len(text):
            remaining_text = text[last_idx:].strip()
            if remaining_text:
                segments.append(("neutral", remaining_text))
        if not segments and text.strip():
            segments.append(("neutral", text.strip()))
        return segments

    def create_voice_profile(self, reference_audio_path: str) -> Dict[str, Any]:
        """Provides the audio path to the cloning engine."""
        if not reference_audio_path or not os.path.exists(reference_audio_path):
            raise FileNotFoundError(f"Reference audio not found: {reference_audio_path}")
        # For XTTS v2, we just need to pass the path directly to the generator
        return {"reference_path": reference_audio_path}

    def generate_speech(
        self, 
        text: str, 
        voice_profile: Dict[str, Any] = None,
        emotion_intensity: float = 1.0
    ) -> str:
        """
        Generates TTS audio using either the neural cloning AI or standard offline voices.
        """
        # Ensure we don't exceed the absolute limit
        if len(text) > 15000:
            print("Warning: Text exceeds 15000 characters. Truncating to limit.")
            text = text[:15000]

        output_filename = f"chatterbox_output_{uuid.uuid4().hex[:8]}.wav"
        output_filepath = os.path.join(self.output_dir, output_filename)

        if self.has_neural_clone:
            # ----------------------------------------------------
            # ACTUAL REAL-TIME VOICE CLONING (XTTS v2)
            # ----------------------------------------------------
            print("Using Deep Neural Voice Cloning...")
            reference_audio = voice_profile.get("reference_path") if voice_profile else None
            
            # If no reference uploaded, fall back to a default voice provided by Coqui
            # Or throw an error. For safety, we need at least one audio file to clone.
            if not reference_audio:
                raise ValueError("Neural Voice Cloning REQUIRES a reference sample audio to be uploaded!")

            # Strip tags for XTTSv2 as it infers emotion from the reference audio inherently
            clean_text = re.sub(r'\[.*?\]', '', text) 
            
            self.model.tts_to_file(
                text=clean_text, 
                speaker_wav=reference_audio, 
                language="en", 
                file_path=output_filepath
            )
            print(f"Cloned Neural Audio saved to: {output_filepath}")
            return output_filepath

        else:
            # ----------------------------------------------------
            # BASIC OFFLINE FALLBACK (pyttsx3)
            # ----------------------------------------------------
            print("Using Standard Computer Voice Engine (No Cloning active)...")
            # Strip emotion tags so the robot doesn't read the word "[happy]" out loud
            clean_text = re.sub(r'\[.*?\]', '', text) 
            
            # Change speed/intensity to simulate the slider
            base_rate = self.engine.getProperty('rate')
            self.engine.setProperty('rate', int(base_rate * emotion_intensity * 0.8)) # Adjust speed

            self.engine.save_to_file(clean_text, output_filepath)
            self.engine.runAndWait()

            print(f"Basic Offline Audio saved to: {output_filepath}")
            return output_filepath
