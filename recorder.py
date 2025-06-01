import json
import os

from typing import Any
from glom import glom, assign


class Recorder:
    standart_view = {
        "Game": {
            "settings": {
                "FPS": 60
            },
            "Car": {
                "SimpleCar": {
                    "higth_scope": 0,
                    "android": {"start_speed": 10},
                    "windows": {"start_speed": 1},
                    "linux": {"start_speed": 1},
                }
            }
        }
    }

    shorts = {
        "g": "Game",
        "s": "settings",
        "c": "Car",
        "sc": "SimpleCar",
        "simplecar": "Game.Car.SimpleCar",
        "and": "android",
        "win": "windows",
        "lin": "linux",
    }

    data: dict

    def __init__(self) -> None:
        # Check validity data.json
        if not os.path.exists("data.json"):
            self.nullable()
        with open("data.json", "r") as dt:
            if dt.readable():
                self.data = json.load(dt)
            else:
                self.nullable()

    def nullable(self) -> "Recorder":
        # Zeroing all record
        self.data = self.standart_view
        self.safe()
        return self

    def get(self, shortlink: str) -> Any:
        sl = shortlink.split(".")
        return glom(
            self.data, ".".join([self.shorts[i] if i in self.shorts else i for i in sl])
        )

    def set(self, shortlink: str, new: object) -> None:
        sl = shortlink.split(".")
        assign(
            self.data,
            ".".join([self.shorts[i] if i in self.shorts else i for i in sl]),
            new,
        )

    def safe(self) -> None:
        with open("data.json", "w") as dt:
            json.dump(self.data, dt, indent=4)
