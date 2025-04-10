import enum
import typing
import numpy as np
from effects import *
from threading import Lock
import sounddevice as sd
class Effect(enum.Enum):
    VIBRATO = 0
    TREMOLO = 1
    PITCH_UP = 2
    PITCH_DOWN = 3
    FOLLOW_PITCH = 4 
    INTENSITY_MULT = 5
    HIGH_PASS_FILTER = 6
    LOW_PASS_FILTER = 7
    APPLY_OTHER_FILE = 8

mutex_cureff: Lock = Lock()
current_effect: Effect

effects: dict[Effect, typing.Callable] = {}

def setup():
    effects[Effect.TREMOLO] = tremolo_wrapper()

def tremolo_wrapper() -> typing.Callable:
    last_elem = 0
    def func(*args):
        nonlocal last_elem
        data = tremolo(*args, last_elem)
        last_elem = data[-1]
        return data
    return func

def available_devices() -> dict[int, str]:
    return sd.querydevices

def apply_effect(data: np.ndarray, effect: typing.Callable):
    sr = 44100
    f = effects[effect]
    match effect :
        case Effect.VIBRATO:
            return normalize(vibrato(data, sr, 10, 10))
        case Effect.TREMOLO:
            return normalize(f(data, len(data) / sr, sr, 1, 0.05))
        case Effect.HIGH_PASS_FILTER:
            return normalize(high_pass(data))
        case Effect.LOW_PASS_FILTER:
            return normalize(low_pass(data))
    
if __name__ == '__main__':
    mido = open_midi("example.midi")
    audio = open_audio("sound.wav")

    modified = apply_pitch_effect(mido, audio, Effect.VIBRATO)
    # modified = adapt_pitch_to(mido, audio)    
    export_mp3(modified)