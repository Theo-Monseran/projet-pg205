from effects.manager import get_effect, apply_effect
import sounddevice as sd

class VACPlayer:
    def __init__(self, device=None, samplerate=44100, blocksize=512, channels=2):
        self.stream = sd.Stream(device=device, samplerate=samplerate, blocksize=blocksize, channels=channels, callback=callback, latency="low")
        self.active = False

    def toggle(self, active):
        if self.active:
            self.stream.stop()
        else:
            self.stream.start()
        self.active = not self.active

    def change_device(self, device: tuple[int, int]):
        if len(device) != 2 or type(device[0]) != int or type(device[1]) != int:
            raise ValueError(f"Invalid value for device : {device}. Requires a tuple of int, or None for default.")
        
        sr, bs, c, l = self.stream.samplerate, self.stream.blocksize, self.stream.channels, self.stream.latency
        self.stream.stop()
        self.stream = sd.Stream(device=device, samplerate=sr, blocksize=bs, channels=c, callback=callback, latency=l)
        self.stream.start()


def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    effect = get_effect(blocking_lock=True)
    print(f"DEBUG: indata: {indata[:, 0]}\noutdata: {outdata}, time: {time}")
    indata[:, 0] = apply_effect(indata[:, 0], effect)
    indata[:, 1] = apply_effect(indata[:, 1], effect)
    outdata[:] = indata
    