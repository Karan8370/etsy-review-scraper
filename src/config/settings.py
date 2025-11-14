thonpython
import json
import os

class Settings:
    @staticmethod
    def load():
        path = os.path.join(os.path.dirname(__file__), "settings.example.json")
        with open(path, "r") as f:
            return json.load(f)