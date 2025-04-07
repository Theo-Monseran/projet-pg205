import numpy as np
import soundfile as sf
import miditoolkit.midi as mtkm
import librosa
import cProfile

def get_pure_sound(A, f, sr, length, phi=0):
    return [A * np.sin(n * 2 * np.pi * f / sr + phi) for n in range(int(sr * length))]


def vibrato(sound, length, sr, intensity, speed):
    
    t = np.arange(len(sound)) / sr
    vib = intensity * np.sin(2 * np.pi * speed * t)
    indices = t + vib / sr
    return np.interp(indices, t, sound)


def tremolo(length, sr, intensity, speed):
    return [intensity * np.sin(2 * np.pi * n*speed/1000) for n in range(int(sr * length))]

def pitch_shift(sound, sr, shift):
    return librosa.effects.pitch_shift(np.array(sound) , sr=sr, n_steps=shift)

def intensity_mult(sound, mult):
    return np.array(sound) * mult

if __name__ == "__main__":
    sound = get_pure_sound(1, 440, 22050, 3)
    sound = pitch_shift(sound, 22050, -6)
    sf.write('./test_pitch_shift.mp3', sound, 22050)