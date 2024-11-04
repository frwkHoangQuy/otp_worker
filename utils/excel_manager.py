# utils/excel_manager.py

import logging

import pandas as pd


class ExcelManager:
    def read_users(self, filename):
        try:
            user_data = pd.read_excel(filename)
            return user_data["MA_TB"].tolist()
        except FileNotFoundError:
            logging.error(f"File {filename} not found.")
            return []
