'''
GUI app to help with song creation
- PaiShoFish49
'''

import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

class Piano():
    def __init__(self) -> None:
        self.keys = [
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False
        ]

class Overtones():
    def __init__(self) -> None:
        self.overtones = [
            1.0
        ]

window = ThemedTk(theme = 'breeze')
window.title('Song Type Toolkit')

window.mainloop()