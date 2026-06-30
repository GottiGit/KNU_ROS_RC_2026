import numpy as np
import pyaudio

volume = 0.5
fs = 48000
duration = 5.0
f = 440.0       # 라 음

data = (np.sin(2 * np.pi * np.arange(fs*duration) * f/fs)).astype(np.float32)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)
stream.write(volume * data)

stream.stop_stream()
stream.close()
p.terminate()

class Tone:
    def __init__(self, volume=0.5, rate =48000, channels=1):
        self.volume = volume
        self.rate = rate
        self.channels = channels
        self.p = pyaudio.PyAudio()
        self.stream = p.open(format=pyaudio.paFloat32,channels=self.channels,rate=self.rate,output=True)
        
        def play(self, octave = 3, note=1, duration=2):
            f = 2**(octave)* 55*2**(((note)-10)/12)
            sample = (np.sin(2 * np.pi * np.arange(self.rate*duration) * f/self.rate)).astype(np.float32)
            self.stream.write(self.volume * sample)
            
        def stop(self):
            self.stream.stop_stream()
            self.stream.close()
            self.p.terminate()