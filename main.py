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

mutex_cureff: Lock = Lock()
current_effect: Effect
    
def apply_effect(data: np.ndarray, effect: typing.Callable):
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