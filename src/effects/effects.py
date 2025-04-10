import numpy as np
import soundfile as sf
import miditoolkit.midi as mtkm
import librosa
import cProfile

def get_pure_sound(A, f, sr, length, phi=0):
    return [A * np.sin(n * 2 * np.pi * f / sr + phi) for n in range(int(sr * length))]

def normalize(sound):    
    return sound/sound.max() if sound.max() != 0 else sound

def vibrato(data, sr, intensity, speed):
    
    t = np.arange(len(data)) / sr
    vib = intensity * np.sin(2 * np.pi * speed * t)
    indices = t + vib / sr
    return np.interp(indices, t, data)


def tremolo(data, length, sr, intensity, speed, previous=0):
    return data * [intensity * np.sin(2 * np.pi * n*speed + np.arcsin(previous)) for n in range(int(sr * length))]

def pitch_shift(data, sr, shift):
    return librosa.effects.pitch_shift(np.array(data) , sr=sr, n_steps=shift)

def intensity_mult(data, mult):
    return np.array(data) * mult

def generic_filter(x: np.ndarray, a: np.ndarray, low_pass: bool) -> np.ndarray: 
     sign = 1 if low_pass else -1
     y = np.zeros(len(x))
     for n in range(0, len(x)):
         y[n] = x[n] * a[0]
         for i in range(1, len(a)):
             if i >= n:
                 break
             y[n] += sign * a[i] * x[n - i]
     return normalize(y)


if __name__ == "__main__":
    sound = sf.read('Enregistrement.wav')
    sound = pitch_shift(sound, 22050, -6)
    sf.write('./test_pitch_shift.mp3', sound, 22050)