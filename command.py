# command.py

import logging

from services.api_service import ApiService

from services.auth_service import AuthService
from utils.cookie_manager import CookieManager
from utils.excel_manager import ExcelManager


class Command:
    def __init__(self):
        self.auth_service = AuthService()
        self.cookie_manager = CookieManager()
        self.excel_manager = ExcelManager()

    def handle(self):
        cookies = self.cookie_manager.load_cookies()
        if not cookies:
            self.auth_service.login()
            cookies = self.cookie_manager.load_cookies()

        if cookies:
            api_service = ApiService(cookies)
            user_list = self.excel_manager.read_users("TB.xlsx")
            for user in user_list:
                response = api_service.process_account(user)
                logging.info(f"Processed user: {user} - Response: {response}")
