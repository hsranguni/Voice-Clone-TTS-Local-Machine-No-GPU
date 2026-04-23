import os
import re
import uuid
import numpy as np
import scipy.io.wavfile as wavfile
from typing import List, Tuple, Dict, Any

class ChatterboxTTS:
    """
    A wrapper class for the Chatterbox Multilingual TTS model.
    This class handles voice cloning, parsing emotion tags, and generating
    speech with emotion exaggeration parameters.
    """

    def __init__(self, output_dir: str = "outputs"):
        """
        Initializes the ChatterboxTTS model parameters.
        
        Args:
            output_dir (str): Directory where generated audio files will be saved.
        """
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir, exist_ok=True)
            
        # TODO: Initialize your actual Chatterbox TTS model here.
        # e.g., self.model = ChatterboxMultilingual.from_pretrained("chatterbox-base")
        print("Chatterbox TTS Model Initialized.")

    def parse_emotion_tags(self, text: str) -> List[Tuple[str, str]]:
        """
        Parses input text for inline emotion tags like [happy]Hello![/happy].
        
        Args:
            text (str): The raw input text.
            
        Returns:
            List[Tuple[str, str]]: A list of tuples containing (emotion, sub_text).
                                   If no tag is specified, emotion defaults to 'neutral'.
        """
        # Regex to match [emotion]Text[/emotion]
        # It also captures text outside of tags as 'neutral'
        pattern = re.compile(r'\[(.*?)\](.*?)\[/\1\]')
        
        segments = []
        last_idx = 0
        
        for match in pattern.finditer(text):
            # Text before the tag is considered neutral
            if match.start() > last_idx:
                neutral_text = text[last_idx:match.start()].strip()
                if neutral_text:
                    segments.append(("neutral", neutral_text))
            
            emotion = match.group(1).lower()
            content = match.group(2).strip()
            segments.append((emotion, content))
            
            last_idx = match.end()
            
        # Any remaining text after the last tag
        if last_idx < len(text):
            remaining_text = text[last_idx:].strip()
            if remaining_text:
                segments.append(("neutral", remaining_text))
                
        # Fallback if no tags are found
        if not segments and text.strip():
            segments.append(("neutral", text.strip()))
            
        return segments

    def create_voice_profile(self, reference_audio_path: str) -> Dict[str, Any]:
        """
        Processes a reference audio file to create a voice cloning profile.
        
        Args:
            reference_audio_path (str): Path to the uploaded reference audio (.wav/.mp3).
            
        Returns:
            Dict: A dictionary containing the voice profile embeddings or parameters.
        """
        if not reference_audio_path or not os.path.exists(reference_audio_path):
            raise FileNotFoundError(f"Reference audio not found: {reference_audio_path}")
            
        print(f"Extracting voice characteristics from: {reference_audio_path}")
        # TODO: Replace with the actual voice cloning extraction logic from Chatterbox
        # e.g., speaker_embedding = self.model.extract_embedding(reference_audio_path)
        
        dummy_profile = {
            "speaker_id": str(uuid.uuid4()),
            "embedding": np.random.rand(512).tolist() # Mock embedding
        }
        return dummy_profile

    def generate_speech(
        self, 
        text: str, 
        voice_profile: Dict[str, Any] = None,
        emotion_intensity: float = 1.0
    ) -> str:
        """
        Generates TTS audio for the given text, applying parsed emotion tags.
        Handles large contexts (up to 15000 chars) by segmenting input.
        
        Args:
            text (str): Input text possibly containing emotion tags.
            voice_profile (Dict): Voice profile dictionary generated from reference audio.
            emotion_intensity (float): Multiplier for the emotion exaggeration control.
            
        Returns:
            str: Path to the locally saved output MP3/WAV file.
        """
        # Ensure we don't exceed the absolute limit
        if len(text) > 15000:
            print("Warning: Text exceeds 15000 characters. Truncating to limit.")
            text = text[:15000]

        parsed_segments = self.parse_emotion_tags(text)
        print(f"Parsed Segments length: {len(parsed_segments)} segments.")
        
        # In a real implementation with Chatterbox, you would map these parsed segments
        # to the model's conditioning tensors. For massive 15,000 char inputs, 
        # iterate through 'parsed_segments' and generate audio chunks, chaining them 
        # together to avoid VRAM Out-of-Memory (OOM) errors.
        
        # Example pseudo-code for chunking:
        # final_audio_parts = []
        # for emotion, phrase in parsed_segments:
        #     # Sub-chunking phrases if they are still individually too long (e.g. >250 chars)
        #     sentence_chunks = self.split_into_sentences(phrase, max_length=250)
        #     exaggeration_param = self.model.get_emotion_vector(emotion) * emotion_intensity
        #     for chunk in sentence_chunks:
        #         audio = self.model.synthesize(chunk, voice_profile, exaggeration_param)
        #         final_audio_parts.append(audio)
        # final_audio = torch.cat(final_audio_parts)
        
        # --- MOCK GENERATION ---
        # Generate a dummy sine wave audio file to simulate successful generation locally
        sample_rate = 24000
        duration = sum(len(phrase) for _, phrase in parsed_segments) * 0.05 # Approx duration
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        
        # Different frequencies to mock different emotions
        audio_data = np.zeros_like(t)
        current_time = 0
        
        for emotion, phrase in parsed_segments:
            phrase_dur = len(phrase) * 0.05
            phrase_t = np.linspace(0, phrase_dur, int(sample_rate * phrase_dur), False)
            
            # Map emotion to a pitch (frequency) solely for the mock artifact
            freq = 440
            if emotion == "happy": freq = 880
            elif emotion == "sad": freq = 220
            elif emotion == "angry": freq = 150
            
            wave = np.sin(freq * phrase_t * 2 * np.pi)
            
            start_idx = int(current_time * sample_rate)
            end_idx = start_idx + len(wave)
            if end_idx <= len(audio_data):
                audio_data[start_idx:end_idx] = wave
                
            current_time += phrase_dur
            
        # Normalize to 16-bit PCM
        audio_data = np.int16(audio_data / np.max(np.abs(audio_data)) * 32767)
        
        output_filename = f"chatterbox_output_{uuid.uuid4().hex[:8]}.wav"
        output_filepath = os.path.join(self.output_dir, output_filename)
        
        wavfile.write(output_filepath, sample_rate, audio_data)
        print(f"Generated output saved to: {output_filepath}")
        
        return output_filepath
