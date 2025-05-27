import os
import pygame.mixer
import pygame.font


class SoundTable:
    all = {
        "Crash": "crash_sound.wav",
        "Background": "background_sound.wav",
        "Engine": "engine_sound.wav",
    }

    def __init__(self):
        pygame.mixer.init()

    def get(self, name):
        return pygame.mixer.Sound(os.path.abspath(f"sounds/{self.all[name]}"))


class FontTable:
    all = {
        "Simple": {"name": "ubuntu", "size": lambda x: int(x / 22.5)},
        "SimpleBig": {"name": "ubuntu", "size": lambda x: int(x / 15)},
    }

    def __init__(self, size):
        pygame.font.init()
        self.font_marker = size[0]

    def get(self, fname):
        newfont = self.all[fname]
        return pygame.font.SysFont(newfont["name"], newfont["size"](self.font_marker))
