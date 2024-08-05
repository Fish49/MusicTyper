'''
song file interpreter and main file
- PaiShoFish49
'''

import soundfile
import numpy as np
import math
import playsound

class Song():
    def __init__(self) -> None:
        self.title = 'untitled'
        self.auther = 'John Doe'
        self.output = None
        self.tempoBPM = 120
        self.durationSeconds = 180
        self.timeSignature = (4, 4)
        self.baseKey = 'C4'
        self.scaleHalfsteps = [0, 2, 4, 5, 7, 9, 11]
        self.tuneHertz = 440
        self.sampleRate = 44100
        self.stereo = True

        self.vars = {
            'song': np.zeros(self.durationSeconds * self.sampleRate)
        }

    def keyToHertz(self, key):
        onPiano = 'C.D.EF.G.A.B'.index(key[0].upper()) + (int(key[1]) * 12)
        fromA4 = onPiano - 57
        if len(key) > 2:
            if key[2] == '#':
                fromA4 += 1
            elif key[2] == '$':
                fromA4 -= 1

        return (2**(fromA4 / 12)) * self.tuneHertz

x = np.zeros(44100 * 2)

allo = [
    [1.0, 0.8, 0.8, 0.8, 0.7, 0.6, 0.5, 0.5],
    [1.0, 0.6, 0.3, 0.2, 0.1, 0.0, 0.0, 0.0],
    [1.0, 0.5, 0.2, 0.1, 0.0, 0.0, 0.0, 0.0],
    [1.0, 0.2, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
    [1.0, 0.5, 0.5, 0.5, 0.2, 0.2, 0.1, 0.0],
    [1.0, 0.5, 0.5, 0.5, 0.2, 0.2, 0.1, 0.0],
]

overtones = allo[0]
for i in range(len(overtones)):
    a = np.linspace(0, 2, 44100 * 2)
    b = np.sin(np.radians(a * ((440 * (i + 1)) * 180)))
    x += b * (overtones[i] / 8)

soundfile.write('test1.wav', x, 44100)
playsound.playsound('test1.wav')