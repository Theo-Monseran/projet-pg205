import enum


class Effect(enum.Enum):
    VIBRATO = 0
    
if __name__ == '__main__':
    mido = open_midi("example.midi")
    audio = open_audio("sound.wav")

    modified = apply_pitch_effect(mido, audio, Effect.VIBRATO)
    # modified = adapt_pitch_to(mido, audio)    
    export_mp3(modified)