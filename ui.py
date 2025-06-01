import pygame
from config import *


class Screen:
    def __init__(self, size: tuple):
        self.size = size
        self.display = pygame.display.set_mode(
            size,
        )
        self.display.fill((60, 220, 0))
        pygame.display.set_caption("PygameEra")

    @staticmethod
    def current_size() -> tuple[int, int]:
        info = pygame.display.Info()
        return (info.current_w, info.current_h)

    @staticmethod
    def current_width() -> int:
        info = pygame.display.Info()
        return info.current_w

    @staticmethod
    def current_heigth() -> int:
        info = pygame.display.Info()
        return info.current_h


class Text:
    def __init__(
        self,
        text: str,
        font: pygame.font.Font,
        pos: tuple[int, int] = (0, 0),
        color: tuple[int, int, int] = black,
        antialias=True,
    ):
        self.font = font
        self.text = font.render(text, antialias, color)
        self.pos = pos


class Window(pygame.sprite.Sprite):
    lt: list[Text] = []

    def __init__(
        self,
        pos: tuple[int, int],
        relative_size: tuple[float, float] = (0.5, 0.5),
        color: tuple[int, int, int] = (0, 0, 0),
        center=False,
    ):
        super().__init__()
        screen_size = Screen.current_size()
        self.size = (
            int(screen_size[0] * relative_size[0]),
            int(screen_size[0] * relative_size[1]),
        )
        self.image = pygame.Surface(self.size)
        self.image.fill(color)
        if center == False:
            self.rect = self.image.get_rect(topleft=pos)
        else:
            self.rect = self.image.get_rect(
                center=(screen_size[0] / 2, screen_size[1] / 2)
            )

    def add_context(self, *el):
        for e in el:
            self.lt.append(e)

    def update(self):
        for e in self.lt:
            self.image.blit(e.text, e.pos)
