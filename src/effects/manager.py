import enum
import typing
import numpy as np
from effects import *
from threading import Lock

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
    NO_EFFECT = 9

mutex_cureff: Lock = Lock()
current_effect: Effect | None = None


def set_effect(effect: Effect, blocking_lock: bool):
    """Changes the current effect to apply. Thread-safe"""
    global current_effect
    global mutex_cureff
    locked = mutex_cureff.acquire(blocking_lock)
    current_effect = effect
    if locked:
        mutex_cureff.release()


def apply_effect(data: np.ndarray, effect: typing.Callable):
    """Applies an audio effect onto audio stream `data`"""
    sr = 22050
    match effect :
        case Effect.VIBRATO:
            return vibrato(data, len(data) / sr, sr, 1, 0.05)
        case Effect.TREMOLO:
            return tremolo(data, len(data) / sr, sr, 1, 0.05)
        case Effect.HIGH_PASS_FILTER:
            return high_pass(data)
        case Effect.LOW_PASS_FILTER:
            return low_pass(data)


if __name__ == '__main__':
    mido = open_midi("example.midi")
    audio = open_audio("sound.wav")

    modified = apply_pitch_effect(mido, audio, Effect.VIBRATO)
    # modified = adapt_pitch_to(mido, audio)    
    export_mp3(modified)