import json
import random
from datetime import datetime
from string import ascii_letters

import allure
import mysql.connector

import data.data
from tests.conftest import TestData
from utils.http_methods import HttpMethods


class API(TestData):
    def __init__(self, connection):
        self.connection = connection
        self.connector = mysql.connector

    @staticmethod
    def get_tos():
        get_resource = '/tos'  # Resource for method GET
        get_url = TestData.base_url + get_resource
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def get_profile():
        """
        :return:
        """
        get_resource = '/get_profile'  # Resource for method
        get_url = TestData.base_url + get_resource
        print(get_url)
        result_get = HttpMethods.get_set_cookie(get_url, {}, TestData.sid)
        print('Response body: ', result_get.text)
        return result_get

    @staticmethod
    def get_list_dbtypes():
        get_resource = '/list_dbtypes'  # Resource for method GET
        get_url = TestData.base_url + get_resource
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def get_list_dbversions():
        get_resource = '/list_dbversions'  # Resource for method GET
        get_url = TestData.base_url + get_resource
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def get_list_envs():
        get_resource = '/list_envs'  # Resource for method GET
        get_url = TestData.base_url + get_resource
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def get_list_regions():
        get_resource = '/list_regions'  # Resource for method GET
        get_url = TestData.base_url + get_resource
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def post_registration():
        """
        Method for create new user
        :return: JSON Response
        """
        json_for_create_new_user = {"email": TestData.email, "password": TestData.password}

        post_resource = '/register'  # Resource for method POST
        post_url = TestData.base_url + post_resource
        print(post_url)
        result_post = HttpMethods.post(post_url, json_for_create_new_user)
        print('Response body: ', result_post.text)
        return result_post

    @staticmethod
    def post_registration_variety_email(mail, prefix):
        """
        Method for create new user
        :return: JSON Response
        """
        json_for_create_new_user = {"email": f'aqa(date){data.data.time}@{mail}.{prefix}',
                                    "password": TestData.password}
        print(f'Data for request: {json_for_create_new_user}')
        post_resource = '/register'  # Resource for method POST
        post_url = TestData.base_url + post_resource
        print(post_url)
        result_post = HttpMethods.post(post_url, json_for_create_new_user)
        print('Response body: ', result_post.text)
        return result_post

    @staticmethod
    def post_login(body: dict):
        post_resource = '/login'  # Resource for method GET
        post_url = TestData.base_url + post_resource
        print(post_url)
        result_post = HttpMethods.post(post_url, body)
        cookies = result_post.cookies
        print(f'Cookies: {cookies}')
        sid = result_post.cookies.values()[0]
        with allure.step('Body: {"email":"your_email","password":"your_password"}'):
            pass
        print('Response: ', result_post.text, f'Sid: {sid}')
        print(f'Sid: {sid}')
        return result_post, sid

    @staticmethod
    def post_db_list(sid: dict):
        """
        :param sid:
        :return:
        """
        post_resource = '/db_list'  # Resource for method
        post_url = TestData.base_url + post_resource
        print(post_url)
        result_post = HttpMethods.post_set_cookie(post_url, {}, sid)
        print('Response body: ', result_post.text)
        return result_post

    @staticmethod
    def post_db_create(sid: dict):
        post_resource = '/db_create'  # Resource for method
        post_url = TestData.base_url + post_resource
        body = {"dbtype": 3, "dbversion": 5, "env": 3, "region": 3}
        result_post = HttpMethods.post_set_cookie_without_body(post_url, sid, body)
        print('Url: ', post_url)
        print(f'Status code: {result_post.status_code}')
        print('Response body: ', result_post.text)
        return result_post

    @staticmethod
    def post_db_create_wrong_value_dbtype(sid: dict):
        post_resource = '/db_create'  # Resource for method
        post_url = TestData.base_url + post_resource
        body = {"dbtype": random.randint(4, 100), "dbversion": 5, "env": 3, "region": 3}
        result_post = HttpMethods.post_set_cookie_without_body(post_url, sid, body)
        print('Url: ', post_url)
        print(f'Status code: {result_post.status_code}')
        print('Response body: ', result_post.text)
        return result_post

    @staticmethod
    def post_db_create_wrong_value_dbversion(sid: dict):
        post_resource = '/db_create'  # Resource for method
        post_url = TestData.base_url + post_resource
        body = {"dbtype": 3, "dbversion": random.randint(6, 100), "env": 3, "region": 3}
        result_post = HttpMethods.post_set_cookie_without_body(post_url, sid, body)
        print('Url: ', post_url)
        print(f'Status code: {result_post.status_code}')
        print('Response body: ', result_post.text)
        return result_post

    @staticmethod
    def post_db_create_wrong_value_env(sid: dict):
        post_resource = '/db_create'  # Resource for method
        post_url = TestData.base_url + post_resource
        body = {"dbtype": 3, "dbversion": 5, "env": random.randint(4, 100), "region": 3}
        result_post = HttpMethods.post_set_cookie_without_body(post_url, sid, body)
        print('Url: ', post_url)
        print(f'Status code: {result_post.status_code}')
        print('Response body: ', result_post.text)
        return result_post

    @staticmethod
    def post_db_create_wrong_value_region(sid: dict):
        post_resource = '/db_create'  # Resource for method
        post_url = TestData.base_url + post_resource
        body = {"dbtype": 3, "dbversion": 5, "env": 3, "region": random.randint(4, 100)}
        result_post = HttpMethods.post_set_cookie_without_body(post_url, sid, body)
        print('Url: ', post_url)
        print(f'Status code: {result_post.status_code}')
        print('Response body: ', result_post.text)
        return result_post

    @staticmethod
    def put_default_user(user_id):
        """
        Method for changing new location
        :param user_id: int
        :return: JSON Response
        """
        put_resource = 'api/users/'  # Resource for method PUT
        put_url = TestData.base_url + put_resource + user_id
        print(put_url)
        json_for_update_new_place = \
            {
                "name": 'morpheus',
                "job": "zion resident"
            }
        result_put = HttpMethods.put(put_url, json_for_update_new_place)
        print('Response body: ', result_put.text)
        return result_put

    @staticmethod
    def delete_db(uuid, sid):
        delete_resource = '/db_delete'  # Resource for method DELETE
        delete_url = TestData.base_url + delete_resource
        print('Url: ', delete_url)
        db_uuid = {"db_uuid": f"{uuid}"}
        json_db_uuid = json.dumps(db_uuid)
        result_delete = HttpMethods.post_for_delete_db(delete_url, json_db_uuid, sid)
        print(f'Status code: {result_delete.status_code}')
        print('Response body: ', result_delete.text)
        return result_delete

    @staticmethod
    def check_full_cycle(sid):
        print('\nCheck Time: ', str(datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
        empty_db_list = API.post_db_list(sid).text
        result_db_create = API.post_db_create(sid)
        db_uuid = result_db_create.json()["db_uuid"]
        while True:
            try:
                db = TestData.connection(db_uuid)
                cursor = db.cursor()
                cursor.execute("""select 1 from dual""")
                res_query = cursor.fetchall()
                print(res_query)
            except Exception as ex:
                print('Exception: ', ex)
            result_post_db_delete = API.delete_db(db_uuid, sid)
            json_delete_db = json.loads(result_post_db_delete.text)
            message = list(json_delete_db.values())[0].split(':')
            if 'msg[18]' in message:
                print(str(datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            elif 'msg[19]' in message:
                print(str(datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
                result_post_db_delete = API.delete_db(db_uuid, sid)
                json.loads(result_post_db_delete.text)
            elif 'msg[13]' in message:
                result_post_db_delete = API.delete_db(db_uuid, sid)
                json_delete_db = json.loads(result_post_db_delete.text)
                print('json_delete_db', json_delete_db)
                print('Finish: ', str(datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            else:
                print('Finish: ', str(datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
                break
        cur_db_list = API.post_db_list(sid)
        with allure.step(f'Compare {cur_db_list.text} == {empty_db_list}'):
            print(f'Compare: {cur_db_list.text} == {empty_db_list}')
        assert cur_db_list.text == empty_db_list, f'DB is not deleted. {cur_db_list.text}'

    def load_db_v2(self):
        letters = ascii_letters
        cursor = self.connection()
        for x in range(1):
            for i in range(10):
                my_string = "".join(random.choice(letters) for _ in range(4096))
                cursor.execute("""
                INSERT INTO accounts (name, text) 
                VALUES (
                'lambotik',
                %(my_string)s);""",
                               {'my_string': my_string})
            self.connection.commit()
