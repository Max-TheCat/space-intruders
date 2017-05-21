import json


class _SettingsPersistence:
    __FILE_NAME = "game-settings.json"

    def __init__(self):
        try:
            with open(self.__FILE_NAME) as settings_file:
                self.settings = json.load(settings_file)
        except IOError:
            self.settings = {}

    def save(self):
        with open(self.__FILE_NAME, "w") as settings_file:
            json.dump(self.settings, settings_file)
