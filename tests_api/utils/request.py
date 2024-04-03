import random
import time
from datetime import datetime
from string import ascii_letters

import allure
import mysql.connector

import tests_api
from connection_data import ConnectionData
from tests_api.data import data
from .checking import Checking
from .http_methods import HttpMethods


class API(ConnectionData):
    def __init__(self, connection):
        self.connection = connection
        self.connector = mysql.connector

    @staticmethod
    @allure.step('get_tos')
    def get_tos():
        """
        Get information about databases limit.
        :return: Response
        """
        get_resource = '/tos'  # Resource for method GET
        get_url = ConnectionData.base_url + get_resource
        with allure.step(f'GET {get_url}'):
            result_get = HttpMethods.get(get_url)
        with allure.step(f'Response JSON: {result_get.text}'):
            print(result_get.json())
            return result_get

    @staticmethod
    @allure.step('get_profile')
    def get_profile(token):
        """
        Get profile information.
        :param token:
        :return: Response
        """
        get_resource = '/get_profile'  # Resource for method
        get_url = ConnectionData.base_url + get_resource
        with allure.step(f'GET {get_url}'):
            result_get = HttpMethods.get(get_url, token=token)
        with allure.step(f'Response JSON: {result_get.text}'):
            print(result_get.json())
            return result_get

    @staticmethod
    @allure.step('get_status')
    def get_status():
        """
        Get profile status.
        :return: Response
        """
        get_resource = '/get_profile'  # Resource for method
        get_url = ConnectionData.base_url + get_resource
        with allure.step(f'GET {get_url}'):
            result_get = HttpMethods.get(get_url, {
                "queue_db_create_orders": 3,
                "queue_db_delete_orders": 1,
                "number_of_stuck_tasks": 0
            }, ConnectionData.token)
        with allure.step(f'Response JSON: {result_get.text}'):
            return result_get

    @staticmethod
    @allure.step('get_list_db_types')
    def get_list_db_types():
        """
        Get databases type list.
        :return: Response
        """
        get_resource = '/list_dbtypes'  # Resource for method GET
        get_url = ConnectionData.base_url + get_resource
        with allure.step(f'GET {get_url}'):
            result_get = HttpMethods.get(get_url)
        with allure.step(f'Response JSON: {result_get.text}'):
            return result_get

    @staticmethod
    @allure.step('get_list_dbversions')
    def get_list_dbversions():
        """
        Get list databases versions.
        :return: Response
        """
        get_resource = '/list_dbversions'  # Resource for method GET
        get_url = ConnectionData.base_url + get_resource
        with allure.step(f'GET {get_url}'):
            result_get = HttpMethods.get(get_url)
        with allure.step(f'Response JSON: {result_get.text}'):
            return result_get

    @staticmethod
    @allure.step('get_list_envs')
    def get_list_envs():
        """
        Get list environments.
        :return: Response
        """
        get_resource = '/list_dbenvs'  # Resource for method GET
        get_url = ConnectionData.base_url + get_resource
        with allure.step(f'GET {get_url}'):
            result_get = HttpMethods.get(get_url)
        with allure.step(f'Response JSON: {result_get.text}'):
            return result_get

    @staticmethod
    @allure.step('get_list_regions')
    def get_list_regions():
        """
        Get list regions.
        :return: Response
        """
        get_resource = '/list_regions'  # Resource for method GET
        get_url = ConnectionData.base_url + get_resource
        with allure.step(f'GET {get_url}'):
            result_get = HttpMethods.get(get_url)
        with allure.step(f'Response JSON: {result_get.text}'):
            return result_get

    @staticmethod
    @allure.step('get_bad_request')
    def get_bad_request():
        """
        Send bad request.
        :return: Response
        """
        get_resource = '/bad_request'  # Resource for method GET
        get_url = ConnectionData.base_url + get_resource
        with allure.step(f'GET {get_url}'):
            result_get = HttpMethods.get(get_url)
        with allure.step(f'Response JSON: {result_get.text}'):
            return result_get

    @staticmethod
    @allure.step('post_registration')
    def post_registration(language: str, tos_agree: bool):
        """
        Method for create new user.
        :param language:
        :param tos_agree:
        :return: JSON Response
        """
        json_for_create_new_user = {"email": ConnectionData.email,
                                    "password": ConnectionData.old_password,
                                    "tos_agree": tos_agree,
                                    'language': language}

        post_resource = '/register'  # Resource for method POST
        post_url = ConnectionData.base_url + post_resource
        with allure.step(f'POST {post_url}'):
            result_post = HttpMethods.post(post_url, json_for_create_new_user)
        return result_post

    @staticmethod
    @allure.step('post_registration_variety_email')
    def post_registration_variety_email(mail: str, prefix: str, language: str, tos_agree: bool):
        """
        Method for create new user.
        :param mail:
        :param prefix:
        :param language:
        :param tos_agree:
        :return: JSON Response
        """
        json_for_create_new_user = {"email": f'aqa{tests_api.data.data.time}@{mail}.{prefix}',
                                    "password": ConnectionData.old_password,
                                    "tos_agree": tos_agree,
                                    "language": language
                                    }
        post_resource = '/register'
        post_url = ConnectionData.base_url + post_resource
        with allure.step(f'POST {post_url}. Params:'f'{json_for_create_new_user}'):
            result_post = HttpMethods.post(post_url, json_for_create_new_user)
        with allure.step(f'Response JSON: {result_post.text}'):
            return result_post

    @staticmethod
    def post_login(body: dict):
        """
        :param body:
        :return: Response
        """
        with allure.step('post_login'):
            post_resource = '/login'
            post_url = ConnectionData.base_url + post_resource
            with allure.step(f'POST {post_url}'):
                result_post = HttpMethods.post(post_url, body)
            with allure.step('Body: {"email":"your_email","password":"your_password"}'):
                return result_post

    @staticmethod
    def post_is_logged(token):
        """
        :param token:
        :return: Response
        """
        with allure.step('post_is_logged'):
            post_resource = '/is_logged'
            post_url = ConnectionData.base_url + post_resource
            with allure.step(f'POST {post_url}'):
                result_post = HttpMethods.post(post_url, token=token)
            with allure.step('Body: {"email":"your_email","password":"your_password"}'):
                pass
            with allure.step(f'Response JSON: {result_post.text}'):
                return result_post

    @staticmethod
    def post_is_logged_with_wrong_token():
        """
        :return: Response
        """
        with allure.step('post_is_logged'):
            post_resource = '/is_logged'
            post_url = ConnectionData.base_url + post_resource
            with allure.step(f'POST {post_url}'):
                result_post = HttpMethods.post(post_url, token=1)
            with allure.step('Body: {"email":"your_email","password":"your_password"}'):
                pass
            with allure.step(f'Response JSON: {result_post.text}'):
                return result_post

    @staticmethod
    def post_db_list(token: dict):
        """
        :param token:
        :return: Response
        """
        with allure.step('post_db_list'):
            post_resource = '/db_list'  # Resource for method
            post_url = ConnectionData.base_url + post_resource
            with allure.step(f'POST {post_url}'):
                result_post = HttpMethods.post(post_url, token=token)
            return result_post

    @staticmethod
    def post_container_list(token: dict):
        """
        :param token:
        :return: Response
        """
        with allure.step('post_container_list'):
            post_resource = '/container_list'  # Resource for method
            post_url = ConnectionData.base_url + post_resource
            with allure.step(f'POST {post_url}'):
                result_post = HttpMethods.post(post_url, token=token)
            return result_post

    @staticmethod
    def post_change_password(token: dict, old_password: str, new_password: str):
        """
        Body example {"current_password":"", "new_password":""}.
        :param token:
        :param old_password:
        :param new_password:
        :return: Response
        """
        with allure.step('post_change_password'):
            post_resource = '/password_update'  # Resource for method
            post_url = ConnectionData.base_url + post_resource
            with allure.step(f'POST {post_url}'):
                result_post = HttpMethods.post(post_url,
                                               {"current_password": old_password, "new_password": new_password},
                                               token=token)
            with allure.step(f'Response JSON: {result_post.text}'):
                return result_post

    @staticmethod
    def post_db_list_with_filter(token: dict, db_uuid: str):
        """
        Getting information about bd by uuid
        :param token: dict
        :param db_uuid: str
        :return: Response
        """
        with allure.step('post_db_list_with_filter'):
            post_resource = '/db_list'  # Resource for method
            post_url = ConnectionData.base_url + post_resource
        with allure.step(f'POST {post_url}'):
            result_post = HttpMethods.post(post_url, {"db_uuid": db_uuid}, token=token)
            return result_post

    @staticmethod
    def post_db_create(token: dict):
        """
        :param token:
        :return: Response
        """
        with allure.step('post_db_create'):
            post_resource = '/db_create'  # Resource for method
            post_url = ConnectionData.base_url + post_resource
            body = {"dbtype": 3, "dbversion": 5, "env": 3, "region": 3}
            with allure.step(f'POST {post_url}, body: {body}'):
                result_post = HttpMethods.post(post_url, body, token=token)
            with allure.step(f'Response JSON: {result_post.text}'):
                return result_post

    @staticmethod
    def post_db_create_wrong_value_db_type(token: dict):
        """
        :param token:
        :return: Response
        """
        with allure.step('post_db_create_wrong_value_db_type'):
            post_resource = '/db_create'  # Resource for method
            post_url = ConnectionData.base_url + post_resource
            body = {"dbtype": random.randint(4, 100), "dbversion": 5, "env": 3, "region": 3}
            with allure.step(f'POST {post_url}, body: {body}'):
                result_post = HttpMethods.post(post_url, body, token=token)
            with allure.step(f'Response JSON: {result_post.text}'):
                return result_post

    @staticmethod
    def post_db_create_wrong_value_db_version(token: dict):
        """
        :param token:
        :return: Response
        """
        with allure.step('post_db_create_wrong_value_db_version'):
            post_resource = '/db_create'  # Resource for method
            post_url = ConnectionData.base_url + post_resource
            body = {"dbtype": 3, "dbversion": random.randint(6, 100), "env": 3, "region": 3}
            with allure.step(f'POST {post_url}, body: {body}'):
                result_post = HttpMethods.post(post_url, body, token=token)
            with allure.step(f'Response JSON: {result_post.text}'):
                return result_post

    @staticmethod
    def post_db_create_wrong_value_env(token: dict):
        """
        :param token:
        :return: Response
        """
        with allure.step('post_db_create_wrong_value_env'):
            post_resource = '/db_create'
            post_url = ConnectionData.base_url + post_resource
            body = {"dbtype": 3, "dbversion": 5, "env": random.randint(4, 100), "region": 3}
            with allure.step(f'POST {post_url}, body: {body}'):
                result_post = HttpMethods.post(post_url, body, token=token)
            with allure.step(f'Response JSON: {result_post.text}'):
                return result_post

    @staticmethod
    def post_db_create_wrong_value_region(token: dict):
        """
        :param token:
        :return: Response
        """
        with allure.step('post_db_create_wrong_value_region'):
            post_resource = '/db_create'
            post_url = ConnectionData.base_url + post_resource
            body = {"dbtype": 3, "dbversion": 5, "env": 3, "region": random.randint(4, 100)}
            with allure.step(f'POST {post_url}, body: {body}'):
                result_post = HttpMethods.post(post_url, body, token=token)
            with allure.step(f'Response JSON: {result_post.text}'):
                return result_post

    @staticmethod
    def post_create_docker_container(token):
        with allure.step('post_create_docker_container'):
            post_resource = '/container_create'
            post_url = ConnectionData.base_url + post_resource
            body = {"docker_image": "nginx", "int_ports": "80", "env": 3, "region": 3}
            with allure.step(f'POST {post_url}, body: {body}'):
                result_post = HttpMethods.post(post_url, body, token=token)
            with allure.step(f'Response JSON: {result_post.text}'):
                return result_post

    @staticmethod
    def post_create_docker_container_with_defunct_image(token):
        with allure.step('post_create_docker_container_with_defunct_image'):
            post_resource = '/container_create'
            post_url = ConnectionData.base_url + post_resource
            body = {"docker_image": "", "int_ports": "80", "env": 3, "region": 3}
            with allure.step(f'POST {post_url}, body: {body}'):
                result_post = HttpMethods.post(post_url, body, token=token)
            with allure.step(f'Response JSON: {result_post.text}'):
                return result_post

    @staticmethod
    def post_delete_docker_container(token, list_index: int):
        with allure.step('post_delete_docker_container'):
            post_resource = '/container_delete'
            post_url = ConnectionData.base_url + post_resource
            result_list = API.post_container_list(token)
            docker_uuid = list(result_list.json()['data'])[list_index]
            print('Selected uuid for delete:', docker_uuid)
            body = {'docker_uuid': f'{docker_uuid}'}
            with allure.step(f'POST {post_url}, body: {body}'):
                result_post = HttpMethods.post(post_url, body, token=token)
            with allure.step(f'Response JSON: {result_post.text}'):
                return result_post

    @staticmethod
    def delete_db(uuid, token):
        """
        :param uuid:
        :param token:
        :return: Response
        """
        with allure.step('delete_db'):
            delete_resource = '/db_delete'
            delete_url = ConnectionData.base_url + delete_resource
            with allure.step(f'DELETE {delete_url}'):
                db_uuid = {"db_uuid": f"{uuid}"}
            with allure.step(f'Db uuid is: {db_uuid}'):
                pass
            json_db_uuid = db_uuid
            result_delete = HttpMethods.post(delete_url, json_db_uuid, token=token)
            with allure.step(f'Response JSON: {result_delete.text}'):
                return result_delete

    @staticmethod
    def delete_all_created_db():
        start = datetime.now().time().strftime('%H:%M')
        print('Start', start)
        while True:
            finish = datetime.now().time().strftime('%H:%M')
            print('Finish', finish)
            list_db = API.post_db_list(ConnectionData.token)
            json_list_db = list_db.json()['data']
            if json_list_db == {}:
                break
            else:
                first_db_uuid = list(json_list_db)[0]
                result_post_db_delete = API.delete_db(first_db_uuid, ConnectionData.token)
                with allure.step(f'Response JSON: {result_post_db_delete.text}'):
                    print(result_post_db_delete.text)
                time.sleep(5)
                if start != finish:
                    break
        list_db = API.post_db_list(ConnectionData.token)
        json_list_db = list_db.json()['data']
        return json_list_db

    @staticmethod
    def check_full_cycle(token):
        with allure.step('check_full_cycle'):
            print('\nCheck Time: ', str(datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            start_value_db_list = API.post_db_list(token)
            API.get_profile(token)
            API.post_db_list(token)
            result_db_create = API.post_db_create(token)
            db_uuid = result_db_create.json()["db_uuid"]
            result_db_delete = API.delete_db(db_uuid, token)
            assert result_db_delete.status_code == 400
            Checking.check_json_search_word_in_value(result_db_delete, "content",
                                                     "msg[18]: error: can't delete a db while it's creating")
            while True:
                result_db_list = API.post_db_list_with_filter(token, db_uuid)
                print('#' * 50, result_db_list.text)
                message = result_db_list.json()['data'][db_uuid][2]
                if message == 'created':
                    break
                else:
                    time.sleep(10)
                    continue
            assert message == 'created'
            API.get_profile(token)
            assert API.delete_db(db_uuid, token).status_code == 200
            result_db_delete = API.delete_db(db_uuid, token)
            assert result_db_delete.status_code == 400
            Checking.check_json_search_word_in_value(result_db_delete, 'content',
                                                     "error: can't delete a db while it's deleting")
            while True:
                current_value_db_list = API.post_db_list(token)
                if start_value_db_list.text == current_value_db_list.text:
                    break
                else:
                    time.sleep(10)
                    continue
            last_db_delete = API.delete_db(db_uuid, token)
            assert last_db_delete.status_code == 400
            Checking.check_json_search_word_in_value(last_db_delete, 'content', 'requested database is not found')

    @allure.step('load_db')
    def load_db(self):
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
