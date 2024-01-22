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
    def connection(db_uuid):
        post_resource = '/db_list'
        post_url = TestData().base_url + post_resource
        result_post = requests.post(post_url, cookies=TestData().result.cookies, json=TestData().body)
        json_list_db = json.loads(result_post.text)
        db_name = json_list_db['content'][db_uuid][0]
        print('db_name', db_name)
        db_status = db_name[2]
        user_name = json_list_db['content'][db_uuid][3].split(':')[1].replace('//', '')
        print('user_name', user_name)
        host = json_list_db['content'][db_uuid][3].split(':')[2].partition('@')[2]
        print('host', host)
        password_db = json_list_db['content'][db_uuid][3].split(':')[2].partition('@')[0]
        print('password_db', password_db)
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
