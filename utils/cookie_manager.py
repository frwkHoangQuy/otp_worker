# utils/cookie_manager.py

import json
import logging
from config.config import Config

class CookieManager:
    def __init__(self):
        self.config = Config()

    def load_cookies(self):
        try:
            with open(self.config.cookies_file, "r") as file:
                cookies = json.load(file)
                logging.info("Cookies loaded successfully.")
                return cookies
        except (FileNotFoundError, json.JSONDecodeError):
            logging.warning("Cookie file not found or corrupted.")
            return None

    def save_cookies(self, cookies):
        with open(self.config.cookies_file, "w") as file:
            json.dump(cookies, file)
        logging.info("Cookies saved successfully.")
