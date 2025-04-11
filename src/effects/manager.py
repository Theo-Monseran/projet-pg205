import enum
import typing
import numpy as np
from effects.effects import *
from threading import Lock
import sounddevice as sd
import soundfile as sf
import playsound as ps

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
current_effect: Effect = Effect.NO_EFFECT

effects: dict[Effect, typing.Callable[[np.ndarray, int], np.ndarray]] = {}
blocksize = 0

class ApplyFile:
    def __init__(self):
        self.audio, sr = sf.read("rff_winter_theme_44100.mp3")
        print(sr)
        self.offset = 0
        self.i = 0
        self.A = 0.1

    def add_audio_file(self, data, sr):
        global blocksize
        bs = blocksize
        data[:] += normalize(self.A * self.audio[:, self.i][self.offset:self.offset+bs], self.audio.max())
        self.i = (self.i + 1) % 2
    
        if self.i == 0:
            self.offset = self.offset + bs % len(self.audio)
    
        return data

af = ApplyFile()

class Tremolo:
    def __init__(self):
        self.phi = 0
        self.nmax = 0
    
    def tremolo(self, data, sr):
        d = normalize(tremolo(data, 3, 1, sr, phi=self.phi), self.nmax)
        self.phi += len(data)
        self.nmax = d.max() if d.max() >= self.nmax else self.nmax
        return d

tr = Tremolo()

class Vibrato:
    def __init__(self):
        self.phi = 0
        self.nmax = 0
    
    def vibrato(self, data, sr):
        print(f"maxvalue: {self.nmax}")
        d = normalize(vibrato(data, 10, 5, sr, phi=self.phi), self.nmax)
        self.phi += len(data)
        self.nmax = d.max() if d.max() >= self.nmax else self.nmax
        return d

vb = Vibrato()

def setup():
    effects[Effect.NO_EFFECT] = lambda data, _: data
    effects[Effect.TREMOLO] = lambda data, sr: tr.tremolo(data, sr)
    effects[Effect.VIBRATO] = lambda data, sr: vb.vibrato(data, sr)
    effects[Effect.HIGH_PASS_FILTER] = lambda data, _: generic_filter(data, a=np.array([0.5, 0.5], dtype=np.float32), low_pass=False)
    effects[Effect.LOW_PASS_FILTER] = lambda data, _: generic_filter(data, a=np.array([0.5, 0.5], dtype=np.float32), low_pass=True)
    effects[Effect.APPLY_OTHER_FILE] = af.add_audio_file


def available_devices() -> dict[int, str]:
    return sd.query_devices()

def get_effect(blocking_lock: bool):
    global current_effect
    global mutex_cureff
    locked = mutex_cureff.acquire(blocking_lock)
    e = None
    if locked:
        e = current_effect
        mutex_cureff.release()
    return e

def set_effect(effect: Effect, blocking_lock: bool):
    """Changes the current effect to apply. Thread-safe"""
    global current_effect
    global mutex_cureff
    locked = mutex_cureff.acquire(blocking_lock)
    if locked:
        print(f"[Log]: Effect changed to {effect}")
        current_effect = effect
        mutex_cureff.release()


def apply_effect(data: np.ndarray, effect: typing.Callable):
    sr = 44100
    f = effects[effect]
    d = f(data, sr)
    print(f"DTYPE: {d.dtype}")
    return d