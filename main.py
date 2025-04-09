import enum
import typing
import numpy as np
from effects import *

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
    
    
def apply_effect(data: np.ndarray, effect: typing.Callable):
    match effect :
        case Effect.VIBRATO:
            return vibrato(data)
        case Effect.TREMOLO:
            return tremolo(data, len(data), 22050, 1, 1)
    
if __name__ == '__main__':
    mido = open_midi("example.midi")
    audio = open_audio("sound.wav")

    modified = apply_pitch_effect(mido, audio, Effect.VIBRATO)
    # modified = adapt_pitch_to(mido, audio)    
    export_mp3(modified)