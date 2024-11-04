# services/telegram_service.py

import logging
from datetime import datetime

import requests

from config.config import Config


class TelegramService:
    def __init__(self):
        self.config = Config()

    def send_message(self, message):
        url = f"https://api.telegram.org/bot{self.config.telegram_bot_token}/sendMessage"
        payload = {"chat_id": self.config.chat_id, "text": message}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                logging.info("Message sent to Telegram.")
            else:
                logging.error("Failed to send message to Telegram.")
        except requests.RequestException as e:
            logging.error(f"Telegram message error: {e}")

    def get_otp(self, login_time):
        url = f"https://api.telegram.org/bot{self.config.telegram_bot_token}/getUpdates"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                messages = response.json().get("result", [])
                for message in reversed(messages):
                    if "text" in message["message"] and message["message"]["chat"]["id"] == int(self.config.chat_id):
                        message_time = datetime.fromtimestamp(message["message"]["date"])
                        if message_time > login_time:
                            otp_code = message["message"]["text"]
                            if otp_code.isdigit():
                                return otp_code
        except requests.RequestException as e:
            logging.error(f"Error retrieving OTP from Telegram: {e}")
        return None
