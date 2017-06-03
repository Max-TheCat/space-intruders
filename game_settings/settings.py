from game_settings.settings_persistence import _SettingsPersistence

instance = None


class Settings(object):
    """Stores the game settings (Singleton)"""
    __SCREEN_WIDTH_SETTING_NAME = "screenWidth"
    __SCREEN_HEIGHT_SETTING_NAME = "screenHeight"
    __BACKGROUND_COLOR_SETTING_NAME = "backgroundColor"
    __BULLET_COLOR_SETTING_NAME = "bulletColor"

    __DEFAULT_SCREEN_WIDTH = 600
    __DEFAULT_SCREEN_HEIGHT = 400
    __DEFAULT_BACKGROUND_COLOR = (230, 230, 230)
    __DEFAULT_BULLET_COLOR = (60, 60, 60)

    __instance = None

    def __init__(self):
        """Initializes the game settings"""
        setting_persistence = _SettingsPersistence()
        setting_dictionary = setting_persistence.settings

        if self.__SCREEN_WIDTH_SETTING_NAME not in setting_dictionary:
            setting_dictionary[self.__SCREEN_WIDTH_SETTING_NAME] = self.__DEFAULT_SCREEN_WIDTH

        if self.__SCREEN_HEIGHT_SETTING_NAME not in setting_dictionary:
            setting_dictionary[self.__SCREEN_HEIGHT_SETTING_NAME] = self.__DEFAULT_SCREEN_HEIGHT

        if self.__BACKGROUND_COLOR_SETTING_NAME not in setting_dictionary:
            setting_dictionary[self.__BACKGROUND_COLOR_SETTING_NAME] = self.__DEFAULT_BACKGROUND_COLOR

        if self.__BULLET_COLOR_SETTING_NAME not in setting_dictionary:
            setting_dictionary[self.__BULLET_COLOR_SETTING_NAME] = self.__DEFAULT_BULLET_COLOR

        self.screen_width = setting_dictionary[self.__SCREEN_WIDTH_SETTING_NAME]
        self.screen_height = setting_dictionary[self.__SCREEN_HEIGHT_SETTING_NAME]
        self.background_color = setting_dictionary[self.__BACKGROUND_COLOR_SETTING_NAME]
        self.bullet_color = setting_dictionary[self.__BULLET_COLOR_SETTING_NAME]

        setting_persistence.save()

    def __new__(cls, *args, **kwargs):
        """Creates the instance if nt exists, returns the instance"""
        if Settings.__instance is None:
            Settings.__instance = object.__new__(cls)

        return Settings.__instance
