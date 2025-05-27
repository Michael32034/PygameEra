import json
import os

from glom import glom, assign


class Recorder:
    standart_view = {
        "Game": {
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
        "c": "Car",
        "sc": "SimpleCar",
        "simplecar": "Game.Car.SimpleCar",
        "and": "android",
        "win": "windows",
        "lin": "linux",
    }

    def __init__(self):
        # Check validity data.json
        if not os.path.exists("data.json"):
            self.nullable()
        with open("data.json", "r") as dt:
            if dt.readable():
                self.data = json.load(dt)
            else:
                self.nullable()

    def nullable(self):
        # Zeroing all record
        self.data = self.standart_view
        self.safe()
        return self

    def get(self, shortlink):
        sl = shortlink.split(".")
        return glom(
            self.data, ".".join([self.shorts[i] if i in self.shorts else i for i in sl])
        )

    def set(self, shortlink, new):
        sl = shortlink.split(".")
        return assign(
            self.data,
            ".".join([self.shorts[i] if i in self.shorts else i for i in sl]),
            new,
        )

    def safe(self):
        with open("data.json", "w") as dt:
            json.dump(self.data, dt, indent=4)
