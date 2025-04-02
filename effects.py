import numpy as np
import soundfile as sf
import miditoolkit.midi as mtkm
import pedalboard as pb

def get_pure_sound(A, f, fs, length, phi=0):
    return [A * np.sin(n * 2 * np.pi * f / fs + phi) for n in range(int(fs * length))]


def vibrato(sound, length, fs, intensity, speed):
    
    t = np.arange(len(sound)) / fs
    vib = intensity * np.sin(2 * np.pi * speed * t)
    indices = t + vib / fs
    return np.interp(indices, t, sound)


def tremolo(length, fs, intensity, speed):
    return [intensity * np.sin(2 * np.pi * n*speed/1000) for n in range(int(fs * length))]

def pitch_shift(sound, fs, shift):
    board = pb.Pedalboard([pb.PitchShift(semitones = shift)])

    return board(sound, fs)

if __name__ == "__main__":
    sound = get_pure_sound(1, 440, 44100, 3)
    sound = pitch_shift(sound, 44100, 6)
    sf.write('./test_pitch_shift.mp3', sound, 44100)