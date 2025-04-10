import enum
import typing
import numpy as np
from effects.effects import *
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
    NO_EFFECT = 9

mutex_cureff: Lock = Lock()
current_effect: Effect | None = Effect.NO_EFFECT

effects: dict[Effect, typing.Callable[[np.ndarray, int], np.ndarray]] = {}

def setup():
    effects[Effect.TREMOLO] = tremolo_wrapper()
    effects[Effect.VIBRATO] = lambda data, sr: normalize(vibrato(data, sr, 10, 10))
    effects[Effect.HIGH_PASS_FILTER] = lambda data, _: generic_filter(data, a=np.array([0.5, 0.5]), low_pass=False)
    effects[Effect.LOW_PASS_FILTER] = lambda data, _: generic_filter(data, a=np.array([0.5, 0.5]), low_pass=True)
    effects[Effect.NO_EFFECT] = lambda data, _: data

def tremolo_wrapper() -> typing.Callable:
    last_elem = 0
    def func(data, sr):
        nonlocal last_elem
        data = tremolo(data, len(data), sr, 1, 0.05, previous=last_elem)
        print("meowfinished")
        last_elem = data[-1]
        return data
    return func

def available_devices() -> dict[int, str]:
    return sd.querydevices()

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
    return f(data, sr)