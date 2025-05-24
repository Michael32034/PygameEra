import json
import os


class Recorder:
    standart_view = {"Game": {"Car": {"SimpleCar": {"higth_scope": 0}}}}

    shorts = {"g": "Game", "c": "Car", "sc": "SimpleCar"}

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
        with open("data.json", "w") as dt:
            json.dump(self.standart_view, dt)
            self.data = self.standart_view
        return self

    def get(self, shortlink):
        sl = shortlink.split(".")
        return self.data[self.shorts[sl[0]]][self.shorts[sl[1]]][self.shorts[sl[2]]][
            sl[3]
        ]

    def set(self, shortlink, new):
        sl = shortlink.split(".")
        self.data[self.shorts[sl[0]]][self.shorts[sl[1]]][self.shorts[sl[2]]][
            sl[3]
        ] = new

    def safe(self):
        with open("data.json", "w") as dt:
            json.dump(self.data, dt)
