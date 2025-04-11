import enum
import typing
import numpy as np
from threading import Lock
import sounddevice as sd
import soundfile as sf
import playsound as ps

def tremolo(signal, rate, depth, sample_rate, phi=0):
    t = np.arange(len(signal), dtype=np.float32) / sample_rate  # Temps en secondes
    modulator = 1 - depth + depth * np.sin(2 * np.pi * rate * t + phi)  # Enveloppe sinusoïdale
    return signal * modulator

def vibrato(data, sr, intensity, speed, phi=0):
    t = np.arange(len(data), dtype=np.float32) / sr
    vib = intensity * np.sin(2 * np.pi * speed * t + phi)
    indices = t + vib / sr
    return np.interp(indices, t, data)

class Tremolo:
    def __init__(self):
        self.phi = 0
    
    def tremolo(self, data, sr):
        d = tremolo(data, 3, 1, sr, phi=self.phi)
        self.phi += len(data)
        return d

class Vibrato:
    def __init__(self):
        self.phi = 0
    
    def vibrato(self, data, sr):
        d = vibrato(data, sr, 10, 10, self.phi)
        self.phi += len(data)
        return d


if __name__ == '__main__':
    f, sr = sf.read("Recording.mp3")
    print(len(f), sr, len(f) // sr)
    f = f[:((len(f) // sr) * 44100)]
    f_full = f.copy()
    s = np.split(f, len(f) // (sr // 15))
    print(len(s), sr)

    vb = Vibrato()
    for frame in s:
        frame[:] = vb.vibrato(frame[:], sr)
        frame[:] = vb.vibrato(frame[:], sr)
    
    sf.write("frame_concat_vibrato.mp3", np.concatenate(s), sr)
    sf.write("frame_concat_vibrato_full.mp3", vb.vibrato(f_full[:], sr), sr)
