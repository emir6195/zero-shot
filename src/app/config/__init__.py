from configparser import ConfigParser


class Configurations:
    def __init__(self) -> None:
        self.config = ConfigParser()
        self.config.read("../../config/config.ini")

    def getDefault(self, key, fallback = None):
        return self.config.get("default", key, fallback=fallback)


ins_config = Configurations()
