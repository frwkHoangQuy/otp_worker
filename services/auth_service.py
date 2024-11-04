# services/auth_service.py

import logging
import time
from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from config.config import Config
from services.telegram_service import TelegramService
from utils.cookie_manager import CookieManager


class AuthService:
    def __init__(self):
        self.config = Config()
        self.driver = self._initialize_driver()
        self.cookie_manager = CookieManager()
        self.telegram_service = TelegramService()

    def _initialize_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        return webdriver.Chrome(options=chrome_options)

    def login(self):
        try:
            self.driver.get("https://cts.vnpt.vn/Linetest/Test/TestL2GponPortList")
            self.driver.find_element(By.ID, "username").send_keys(self.config.username)
            self.driver.find_element(By.ID, "password").send_keys(self.config.password)
            self.driver.find_element(By.XPATH, "//button[text()='ĐĂNG NHẬP']").click()
            self.telegram_service.send_message("i need otp")
            otp = self._wait_for_otp()
            if otp:
                self.driver.find_element(By.ID, "passOTP").send_keys(otp)
                self.driver.find_element(By.XPATH, "//button[text()='ĐĂNG NHẬP']").click()
                cookies = {cookie['name']: cookie['value'] for cookie in self.driver.get_cookies()}
                self.cookie_manager.save_cookies(cookies)
        finally:
            self.driver.quit()

    def _wait_for_otp(self):
        login_time = datetime.now()
        while datetime.now() - login_time < timedelta(minutes=10):
            otp = self.telegram_service.get_otp(login_time)
            if otp:
                return otp
            time.sleep(5)
        logging.error("OTP not received within 10 minutes.")
        return None
