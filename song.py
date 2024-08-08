'''
song file interpreter and main file
- PaiShoFish49
'''

import soundfile
import numpy as np
import math
import playsound
import re
import time

class Song():
    def __init__(self) -> None:
        self.title = 'untitled'
        self.auther = 'John Doe'
        self.output = None
        self.tempoHertz = 2
        self.durationSamples = 7938000
        self.timeSignature = (4, 4)
        self.baseKey = 'C4'
        self.scaleHalfsteps = [0, 2, 4, 5, 7, 9, 11]
        self.tuneHertz = 440
        self.sampleRate = 44100
        self.stereo = True

        self.vars = {
            'song': np.zeros(self.durationSamples)
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

    def decibelsToDegs(self, db):
        return 10 ** (db / 10)

    def degsToDecibels(self, degs):
        return 10 * math.log(degs, 10)

    def stringToHertz(self, string: str):
        if string.endswith('n'):
            return self.keyToHertz(string[:-1])

    def generateWave(self, shape, duration, frequency = 'Cn', amplitude = 1, phase = 0):
        frequency = self.stringToHertz(frequency)
        line = np.linspace(0 - phase, (duration * frequency / self.sampleRate) - phase, duration)
        if shape == 'sine':
            return np.sin(line * 2 * np.pi) * amplitude
        elif shape == 'square':
            return -np.sign(np.mod(line, 1) - 0.5) * amplitude
        elif shape == 'sawup':
            return (np.mod(line, 1) - 0.5) * amplitude
        elif shape == 'sawdown':
            return (-np.mod(line, 1) + 0.5) * amplitude

    def readLine(self, line):
        pass

    def readFile(self, text: str):
        for i in text.splitlines():
            self.readLine(i)

def start():
    with open('renderList.txt', 'r') as renderList:
        for i in renderList.readlines():
            x = Song()

a = Song()
b = a.generateWave('sine', 44100, 'C0n', 0.5, 0)
c = a.generateWave('sine', 44100, 'C1n', 0.5, 0)
soundfile.write('test.wav', b + c, 44100)
time.sleep(1)
playsound.playsound('test.wav')