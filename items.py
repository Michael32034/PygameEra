import os
import pygame

from ui import Screen


class Element(pygame.sprite.Sprite):
    image: pygame.Surface
    rect: pygame.Rect

    def __init__(
        self,
        size: tuple[int, int],
        pos: tuple[int, int],
        color: tuple[int, int, int] = (0, 0, 0),
        image: str | None = None,
    ):
        super().__init__()
        if image != None:
            self.image = pygame.image.load(image).convert_alpha()
        else:
            self.image = pygame.Surface(size)
            self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)


class Car(Element):
    skinlist = {
        "main": os.path.abspath("storage/main_car.png"),
        "tractor": os.path.abspath("storage/tractor_car.png"),
        "passenger": os.path.abspath("storage/passenger_car.png"),
    }

    def __init__(
        self,
        size: tuple[int, int],
        pos: tuple[int, int],
        skin: str = "main",
        relative_width: float = 0.2,
    ):
        super().__init__(size, pos, image=self.skinlist[skin])
        window_width = Screen.current_width()
        self.image = pygame.transform.scale(
            self.image,
            (window_width * relative_width, window_width * relative_width * 2),
        )
        self.rect = self.image.get_rect()


class Road(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.size = Screen.current_size()
        self.road_width = int(self.size[0] / 1.4)
        self.roadmark_width = int(self.size[0] / 60)
        self.elements = [
            {
                "size": (self.road_width, self.size[1]),
                "pos": (self.size[0] / 2 - self.road_width / 2, 0),
                "color": (50, 50, 50),
            },
            {
                "size": (self.roadmark_width, self.size[1]),
                "pos": (self.size[0] / 2 - self.roadmark_width / 2, 0),
                "color": (255, 240, 60),
            },
            {
                "size": (self.roadmark_width, self.size[1]),
                "pos": (
                    self.size[0] / 2 - self.road_width / 2 + self.roadmark_width * 2,
                    0,
                ),
                "color": (255, 255, 255),
            },
            {
                "size": (self.roadmark_width, self.size[1]),
                "pos": (
                    self.size[0] / 2 + self.road_width / 2 - self.roadmark_width * 3,
                    0,
                ),
                "color": (255, 255, 255),
            },
        ]
        self._build_road()

    def _build_road(self):
        def add_sprite(
            size: tuple[int, int], pos: tuple[int, int], color: tuple[int, int, int]
        ):
            elem = Element(size, pos, color)
            self.add(elem)

        for i in self.elements:
            add_sprite(i["size"], i["pos"], i["color"])
