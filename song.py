'''
song file interpreter and main file
- PaiShoFish49
'''

import soundfile
import numpy as np
import math
import playsound
import re

patterns = {
    'time': r'([/0-9\. ]+(sm|s|m|b|fr))',
    'frequency': r'(\d+(hz|sd|hs|bpm)|[ABCDEFG]\d[#\$%]?n)',
    'amplitude': r'([/0-9\. ]+ad|)',
    'pure': r'pure (sine|square|sawup|sawdown|triangle) ',
    'assignment': r'.+='
}

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

    def decibelsToDegs(self, db):
        return 10 ** (db / 10)

    def degsToDecibels(self, degs):
        return 10 * math.log(degs, 10)

    def generateWave(self, shape, duration, frequency = 'Cn', amplitude = 1):
        if shape == 'sine':
            pass

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
print(a.keyToHertz('C4'))