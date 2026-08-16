import numpy as np
import soundfile as sf

def load_mono(path):
    audio, sr = sf.read(path, always_2d=True)
    return audio.mean(axis=1).astype(np.float32), int(sr)

def crop(audio, sr, start, end):
    return audio[max(0,int(start*sr)):min(len(audio),int(end*sr))].copy()
