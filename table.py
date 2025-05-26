import os
import pygame.mixer


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
