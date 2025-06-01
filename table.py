import os
import pygame.mixer
import pygame.font

from ui import Screen


class SoundTable:
    all = {
        "Crash": "crash_sound.wav",
        "Background": "background_sound.wav",
        "Engine": "engine_sound.wav",
    }

    def __init__(self):
        pygame.mixer.init()

    def get(self, name: str) -> pygame.mixer.Sound:
        return pygame.mixer.Sound(os.path.abspath(f"sounds/{self.all[name]}"))


class FontTable:
    def __init__(self):
        pygame.font.init()
        self.font_marker: int = Screen.current_width()
        self.all = {
            "Simple": {"name": "ubuntu", "size": int(self.font_marker / 22.5)},
            "SimpleBig": {"name": "ubuntu", "size": int(self.font_marker / 15)},
        }

    def get(self, fname) -> pygame.font.Font:
        newfont = self.all[fname]
        return pygame.font.SysFont(newfont["name"], newfont["size"])

    def size(self, fname) -> int:
        return self.all[fname]["size"]
