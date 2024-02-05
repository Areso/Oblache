import json
import random
import time
from datetime import datetime
from string import ascii_letters

import allure
import mysql.connector

import data.data
from tests.conftest import TestData
from utils.checking import Checking
from utils.http_methods import HttpMethods


class API(TestData):
    def __init__(self, connection):
        self.connection = connection
        self.connector = mysql.connector

    @staticmethod
    def get_tos():
        get_resource = '/tos'  # Resource for method GET
        get_url = TestData.base_url + get_resource
        with allure.step(f'GET {get_url}'):
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
        with allure.step(f'GET {get_url}'):
            print(get_url)
        result_get = HttpMethods.get_with_cookie(get_url, {}, TestData.sid)
        print('Response body: ', result_get.text)
        return result_get

    @staticmethod
    def get_status():
        """
        :return:
        """
        get_resource = '/get_profile'  # Resource for method
        get_url = TestData.base_url + get_resource
        with allure.step(f'GET {get_url}'):
            print(get_url)
        result_get = HttpMethods.get_with_cookie(get_url, {
            "queue_db_create_orders": 3,
            "queue_db_delete_orders": 1,
            "number_of_stuck_tasks": 0
        }, TestData.sid)
        print('Response body: ', result_get.text)
        return result_get

    @staticmethod
    def get_list_dbtypes():
        get_resource = '/list_dbtypes'  # Resource for method GET
        get_url = TestData.base_url + get_resource
        with allure.step(f'GET {get_url}'):
            print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def get_list_dbversions():
        get_resource = '/list_dbversions'  # Resource for method GET
        get_url = TestData.base_url + get_resource
        with allure.step(f'GET {get_url}'):
            print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def get_list_envs():
        get_resource = '/list_dbenvs'  # Resource for method GET
        get_url = TestData.base_url + get_resource
        with allure.step(f'GET {get_url}'):
            print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def get_list_regions():
        get_resource = '/list_regions'  # Resource for method GET
        get_url = TestData.base_url + get_resource
        with allure.step(f'GET {get_url}'):
            print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def get_bad_request():
        get_resource = '/bad_request'  # Resource for method GET
        get_url = TestData.base_url + get_resource
        with allure.step(f'GET {get_url}'):
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
        with allure.step(f'POST {post_url}'):
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
        json_for_create_new_user = {"email": f'aqa{data.data.time}@{mail}.{prefix}',
                                    "password": TestData.password}
        print(f'Data for request: {json_for_create_new_user}')
        post_resource = '/register'  # Resource for method POST
        post_url = TestData.base_url + post_resource
        with allure.step(f'POST {post_url}'):
            print(post_url)
        with allure.step(f'Params:'
                         f'{json_for_create_new_user}'):
            pass
        result_post = HttpMethods.post(post_url, json_for_create_new_user)
        print('Response body: ', result_post.text)
        return result_post

    @staticmethod
    def post_login(body: dict):
        post_resource = '/login'  # Resource for method GET
        post_url = TestData.base_url + post_resource
        with allure.step(f'POST {post_url}'):
            print(post_url)
        result_post = HttpMethods.post(post_url, body)
        print(result_post)
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
        with allure.step(f'POST {post_url}'):
            print(post_url)
        result_post = HttpMethods.post_with_cookie(post_url, {}, sid)
        print('Response body: ', result_post.text)
        return result_post

    @staticmethod
    def post_db_list_with_filter(sid: dict, db_uuid: str):
        """
        Getting information about bd by uuid
        :param sid: dict
        :param db_uuid: str
        :return:
        """
        post_resource = '/db_list'  # Resource for method
        post_url = TestData.base_url + post_resource
        print(post_url)
        result_post = HttpMethods.post_with_cookie_without_body(post_url, sid, {"db_uuid": db_uuid}, )
        print('Response body: ', result_post.text)
        return result_post

    @staticmethod
    def post_db_create(sid: dict):
        post_resource = '/db_create'  # Resource for method
        post_url = TestData.base_url + post_resource
        with allure.step(f'POST {post_url}'):
            pass
        body = {"dbtype": 3, "dbversion": 5, "env": 3, "region": 3}
        result_post = HttpMethods.post_with_cookie_without_body(post_url, sid, body)
        print('Url:', post_url)
        print(f'Status code: {result_post.status_code}')
        print('Response body: ', result_post.text)
        return result_post

    @staticmethod
    def post_db_create_wrong_value_dbtype(sid: dict):
        post_resource = '/db_create'  # Resource for method
        post_url = TestData.base_url + post_resource
        with allure.step(f'POST {post_url}'):
            print(post_url)
        body = {"dbtype": random.randint(4, 100), "dbversion": 5, "env": 3, "region": 3}
        result_post = HttpMethods.post_with_cookie_without_body(post_url, sid, body)
        print(f'Status code: {result_post.status_code}')
        print('Response body: ', result_post.text)
        return result_post

    @staticmethod
    def post_db_create_wrong_value_dbversion(sid: dict):
        post_resource = '/db_create'  # Resource for method
        post_url = TestData.base_url + post_resource
        with allure.step(f'POST {post_url}'):
            print(post_url)
        body = {"dbtype": 3, "dbversion": random.randint(6, 100), "env": 3, "region": 3}
        result_post = HttpMethods.post_with_cookie_without_body(post_url, sid, body)
        print(f'Status code: {result_post.status_code}')
        print('Response body: ', result_post.text)
        return result_post

    @staticmethod
    def post_db_create_wrong_value_env(sid: dict):
        post_resource = '/db_create'  # Resource for method
        post_url = TestData.base_url + post_resource
        with allure.step(f'POST {post_url}'):
            print(post_url)
        body = {"dbtype": 3, "dbversion": 5, "env": random.randint(4, 100), "region": 3}
        result_post = HttpMethods.post_with_cookie_without_body(post_url, sid, body)
        print(f'Status code: {result_post.status_code}')
        print('Response body: ', result_post.text)
        return result_post

    @staticmethod
    def post_db_create_wrong_value_region(sid: dict):
        post_resource = '/db_create'  # Resource for method
        post_url = TestData.base_url + post_resource
        with allure.step(f'POST {post_url}'):
            print(post_url)
        body = {"dbtype": 3, "dbversion": 5, "env": 3, "region": random.randint(4, 100)}
        result_post = HttpMethods.post_with_cookie_without_body(post_url, sid, body)
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
        with allure.step(f'DELETE {delete_url}'):
            print(delete_url)
        db_uuid = {"db_uuid": f"{uuid}"}
        with allure.step(f'Db uuid is: {db_uuid}'):
            pass
        json_db_uuid = json.dumps(db_uuid)
        result_delete = HttpMethods.post_for_delete_db(delete_url, json_db_uuid, sid)
        print(f'Status code: {result_delete.status_code}')
        print('Response body: ', result_delete.text)
        return result_delete

    @staticmethod
    def check_full_cycle2(sid):
        print('\nCheck Time: ', str(datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
        start_value_db_list = API.post_db_list(sid)
        API.get_profile()
        API.post_db_list(sid)
        result_db_create = API.post_db_create(sid)
        db_uuid = result_db_create.json()["db_uuid"]
        result_db_delete = API.delete_db(db_uuid, sid)
        assert result_db_delete.status_code == 400
        Checking.check_json_search_word_in_value(result_db_delete, "content",
                                                 "msg[18]: error: can't delete a db while it's creating")
        while True:
            result_db_list = API.post_db_list_with_filter(sid, db_uuid)
            message = result_db_list.json()['content'][db_uuid][2]
            if message == 'db_created':
                break
            else:
                time.sleep(4)
                continue
        assert message == 'db_created'
        API.get_profile()
        assert API.delete_db(db_uuid, sid).status_code == 200
        result_db_delete = API.delete_db(db_uuid, sid)
        assert result_db_delete.status_code == 400
        Checking.check_json_search_word_in_value(result_db_delete, 'content',
                                                 "error: can't delete a db while it's deleting")
        while True:
            current_value_db_list = API.post_db_list(sid)
            if start_value_db_list.text == current_value_db_list.text:
                break
            else:
                time.sleep(4)
                continue
        last_db_delete = API.delete_db(db_uuid, sid)
        assert last_db_delete.status_code == 400
        Checking.check_json_search_word_in_value(last_db_delete, 'content', 'requested database is not found')

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
