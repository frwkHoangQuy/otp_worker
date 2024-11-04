# config/config.py

import configparser


class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance.config = configparser.ConfigParser()
            cls._instance.config.read("config/config.ini")
        return cls._instance

    @property
    def telegram_bot_token(self):
        return self.config.get("Telegram", "bot_token")

    @property
    def chat_id(self):
        return self.config.get("Telegram", "chat_id")

    @property
    def cookies_file(self):
        return self.config.get("Paths", "cookies_file")

    @property
    def max_retries(self):
        return int(self.config.get("Settings", "max_retries"))

    @property
    def username(self):
        return self.config.get("Credentials", "username")

    @property
    def password(self):
        return self.config.get("Credentials", "password")
