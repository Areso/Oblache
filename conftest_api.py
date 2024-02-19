import json
import os

import mysql.connector
import requests
from dotenv import load_dotenv


class TestData:
    base_url = 'https://dbend.areso.pro'  # Base url
    load_dotenv()
    email = os.getenv('EMAIL')
    old_password = os.getenv('PASSWORD')
    new_password = '123456789'
    try:
        body = {"email": email, "password": f'{old_password}'}
        result = requests.post('https://dbend.areso.pro/login', json=body)
        print(result.text)
        sid = dict(result.cookies)
        if sid != {}:
            new_password, old_password = old_password, new_password
            print(sid)
        # assert sid != {}
    except:
        old_password, new_password = new_password, old_password
        body = {"email": email, "password": f'{old_password}'}
        result = requests.post('https://dbend.areso.pro/login', json=body)
        print(result.text)
        sid = dict(result.cookies)
        print(sid)
        # assert sid != {}

    @staticmethod
    def connection(db_uuid):
        post_resource = '/db_list'
        post_url = TestData().base_url + post_resource
        result_post = requests.post(post_url, cookies=TestData().result.cookies, json=TestData().body)
        json_list_db = json.loads(result_post.text)
        db_name = json_list_db['content'][db_uuid][0]
        user_name = json_list_db['content'][db_uuid][3].split(':')[1].replace('//', '')
        host = json_list_db['content'][db_uuid][3].split(':')[2].partition('@')[2]
        password_db = json_list_db['content'][db_uuid][3].split(':')[2].partition('@')[0]
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

TestData()