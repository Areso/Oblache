import os

import pytest
import requests
from dotenv import load_dotenv

from tests_api.utils.checking import Checking

base_url = 'https://dbend.areso.pro'  # Base url


@pytest.fixture()
def get_token():
    load_dotenv()
    email = os.getenv('EMAIL')
    old_password = os.getenv('PASSWORD')
    new_password = '123456789'
    try:
        body = {"email": email, "password": f'{old_password}'}
        result = requests.post('https://dbend.areso.pro/login', json=body)
        token = result.json()['token']
        if token != {}:
            new_password, old_password = old_password, new_password
        Checking.check_status_code(result, 200)
        return token, body, new_password, old_password, email
    except Exception as ex:
        print(ex)
        old_password, new_password = new_password, old_password
        body = {"email": email, "password": f'{old_password}'}
        result = requests.post('https://dbend.areso.pro/login', json=body)
        token = result.json()['token']
        Checking.check_status_code(result, 200)
        return token, body, new_password, old_password, email
