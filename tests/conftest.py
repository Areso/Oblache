import json
import os
from pprint import pprint

import mysql.connector
import requests
from dotenv import load_dotenv


class TestData:
    base_url = 'https://dbend.areso.pro'  # Base url
    load_dotenv()
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    MY_EMAIL = os.getenv('EMAIL')
    MY_PASSWORD = os.getenv('PASSWORD')
    body = {"email": f'{email}', "password": f'{password}'}
    result = requests.post('https://dbend.areso.pro/login', json=body)
    sid = dict(result.cookies)

    @staticmethod
    def connection():
        post_resource = '/db_list'
        post_url = TestData().base_url + post_resource
        print(post_url)
        result_post = requests.post(post_url, cookies=TestData().result.cookies, json=TestData().body)
        pprint(result_post.text)
        json_list_db = json.loads(result_post.text)
        first_db_uuid = list(json_list_db['content'].keys())[0]
        db_name = json_list_db['content'][first_db_uuid][0]
        user_name = json_list_db['content'][first_db_uuid][3].split(':')[1].replace('//', '')
        host = json_list_db['content'][first_db_uuid][3].split(':')[2].partition('@')[2]
        password_db = json_list_db['content'][first_db_uuid][3].split(':')[2].partition('@')[0]
        print('\nConnecting to DB...')
        db = mysql.connector.connect(host=host,
                                     port=3306,
                                     user=user_name,
                                     database=db_name,
                                     password=password_db
                                     )
        print('Successfully connected...')
        assert db.is_connected() is True
        return db
