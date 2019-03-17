import importlib


class CharacterDict(dict):
    def __missing__(self, key):
        return lambda a, b: key


def load_classes(name):
    try:
        default_classes = importlib.import_module(name)
        return CharacterDict(default_classes.character_classes)
    except ModuleNotFoundError:
        return None
