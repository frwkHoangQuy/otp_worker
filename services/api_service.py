import logging

import requests


class ApiService:
    def __init__(self, cookies):
        self.cookies = cookies

    def process_account(self, user):
        url = "https://cts.vnpt.vn/linetest/Test/TestGponByList"
        headers = {"Accept": "application/json", "Content-Type": "application/json;charset=UTF-8"}
        payload = {"listInfo": user, "provinceCode": "NAN"}

        try:
            response = requests.post(url, json=payload, headers=headers, cookies=self.cookies)
            if response.status_code == 200:
                logging.info(f"API request successful for user: {user}")
                return {"username": user, "response": response.json()}
        except requests.RequestException as e:
            logging.error(f"API request error for user {user}: {e}")
        return {"username": user, "response": None}
