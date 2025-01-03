import time
import sounddevice as sd
import soundfile as sf
import numpy as np
import os
from datetime import datetime

def record_audio(duration, samplerate=16000, channels=1):
    """Record audio from microphone"""
    recording = sd.rec(int(duration * samplerate),
                      samplerate=samplerate,
                      channels=channels)
    sd.wait()
    return recording

def save_sample(audio, filename, directory, samplerate=16000):
    """Save recorded audio to file"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    filepath = os.path.join(directory, filename)
    sf.write(filepath, audio, samplerate)

def collect_samples(sample_type, duration=2, num_samples=1):
    """Collect multiple samples with countdown"""
    base_dir = f"{sample_type}"
    
    for i in range(num_samples):
        print(f"\nRecording {i+1}/{num_samples}")
        print("Starting in:")
        for j in range(3, 0, -1):
            print(f"{j}...")
            time.sleep(1)
            
        print("Recording...")
        audio = record_audio(duration)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{sample_type}_{timestamp}_{i+1}.wav"
        save_sample(audio, filename, base_dir)
        
        print(f"Saved: {filename}")
        
        # Wait between recordings
        time.sleep(1)

# Example usage
if __name__ == "__main__":
    print("Collecting wake word samples...")
    collect_samples("wake_word", duration=2, num_samples=10)