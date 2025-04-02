import enum


class Effect(enum.Enum):
    VIBRATO = 0
    TREMOLO = 1
    PITCH_UP = 2
    PITCH_DOWN = 3
    FOLLOW_PITCH = 4 
    INTENSITY_UP = 5
    INTENSITY_DOWN = 6
    HIGH_PASS_FILTER = 7
    LOW_PASS_FILTER = 8
    APPLY_OTHER_FILE = 9
    REVERB = 10
    
    
if __name__ == '__main__':
    mido = open_midi("example.midi")
    audio = open_audio("sound.wav")

    modified = apply_pitch_effect(mido, audio, Effect.VIBRATO)
    # modified = adapt_pitch_to(mido, audio)    
    export_mp3(modified)