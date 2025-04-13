from effects.manager import get_effect, apply_effect, Effect
import sounddevice as sd
import numpy as np
import noisereduce as nr

class VACPlayer:

    blocksize = 0
    samplerate = 0

    effect = Effect.NO_EFFECT

    def __init__(self, device=None, samplerate=44100, blocksize=512, channels=2):
        self.stream = sd.Stream(device=device, samplerate=samplerate, blocksize=blocksize, channels=channels, callback=VACPlayer.callback, latency=0.05, dtype=np.float32, dither_off=True)
        VACPlayer.blocksize = self.stream.blocksize
        VACPlayer.samplerate = self.stream.samplerate
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
        self.stream = sd.Stream(device=device, samplerate=sr, blocksize=bs, channels=c, callback=VACPlayer.callback, latency=l, dtype=np.float32, dither_off=True)
        VACPlayer.blocksize = self.stream.blocksize
        VACPlayer.samplerate = self.stream.samplerate
        self.stream.start()

    @staticmethod
    def callback(indata, outdata, frames, time, status):
        global data
        if status:
            print(status)
        
        #if data is None:
        #    data = np.zeros(indata.shape)

        # print(f"LENGTH:{len(data[:, 0])}")
        
        # if len(data[:, 0]) >= 44100 * 5:
        #     sf.write("vibrato_data.mp3", data[:, 0], 44100)
        #     exit(0)

        e, locked = get_effect(blocking_lock=False)
        if locked:
            VACPlayer.effect = e
        #print(f"DEBUG:\n time: {time}\nframes: {frames}")
        
        indata[:, 0] = nr.reduce_noise(indata[:, 0], VACPlayer.samplerate)
        indata[:, 1] = nr.reduce_noise(indata[:, 1], VACPlayer.samplerate)

        indata[:, 0] = apply_effect(indata[:, 0], VACPlayer.effect)
        indata[:, 1] = apply_effect(indata[:, 1], VACPlayer.effect)


        #data = np.concatenate((data, indata))

        outdata[:] = indata

    