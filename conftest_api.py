import os

import mysql.connector
import requests
from dotenv import load_dotenv

from tests_api.utils.http_methods import HttpMethods


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
        token = result.json()['token']
        if token != {}:
            new_password, old_password = old_password, new_password
            print(token)
    except Exception as ex:
        print(ex)
        old_password, new_password = new_password, old_password
        body = {"email": email, "password": f'{old_password}'}
        result = requests.post('https://dbend.areso.pro/login', json=body)
        token = result.json()['token']
        print(token)

    @staticmethod
    def connection(db_uuid):
        print(db_uuid)
        post_resource = '/db_list'
        post_url = TestData().base_url + post_resource
        result_post = HttpMethods.post(post_url, token=TestData.token, body=TestData.body)
        json_list_db = result_post.json()
        print(json_list_db['data'])
        db_name = json_list_db['data'][db_uuid][0]
        user_name = json_list_db['data'][db_uuid][3].split(':')[1].replace('//', '')
        host = json_list_db['data'][db_uuid][3].split(':')[2].partition('@')[2]
        password_db = json_list_db['data'][db_uuid][3].split(':')[2].partition('@')[0]
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

# TestData()
