import random
import time
from datetime import datetime
from string import ascii_letters

import allure

import tests_api
from tests_api.data import data
from .checking import Checking
from .http_methods import HttpMethods
import mysql.connector


class API:
    base_url = 'https://dbend.areso.pro'

    @staticmethod
    def get_tos(token: str):
        """
        Get information about databases limit.
        :return: Response
        """
        get_resource = '/tos'
        get_url = API.base_url + get_resource
        response = HttpMethods.get(url=get_url)
        with allure.step('Endpoint: /tos'):
            ...
        with allure.step('Request:'):
            with allure.step(f'Url: {get_url}'):
                ...
            with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{token}'} }'):
                ...
            with allure.step(f'Body: {None}'):
                ...
        with allure.step('Response:'):
            with allure.step(f'Status code: {response.status_code}'):
                ...
            with allure.step(f'JSON: {response.text}'):
                ...
        return response

    @staticmethod
    def get_profile(token: str):
        """
        Get profile information.
        :param token:
        :return: Response
        """

        get_resource = '/get_profile'
        get_url = API.base_url + get_resource
        response = HttpMethods.get(
            url=get_url,
            token=token)
        with allure.step('Endpoint: /get_profile'):
            ...
        with allure.step('Request:'):
            with allure.step(f'Url: {get_url}'):
                ...
            with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{token}'} }'):
                ...
            with allure.step(f'Body: {None}'):
                ...
        with allure.step('Response:'):
            with allure.step(f'Status code: {response.status_code}'):
                ...
            with allure.step(f'JSON: {response.text}'):
                ...
        return response

    @staticmethod
    def get_status(token: str):
        """
        Get profile status.
        :return: Response
        """
        get_resource = '/get_profile'  # Resource for method
        get_url = API.base_url + get_resource
        response = HttpMethods.get(
            url=get_url,
            body={"queue_db_create_orders": 3,
                  "queue_db_delete_orders": 1,
                  "number_of_stuck_tasks": 0},
            token=token)
        with allure.step('Endpoint: /get_profile'):
            ...
        with allure.step('Request:'):
            with allure.step(f'Url: {get_url}'):
                ...
            with allure.step(f"Headers: {HttpMethods.headers | {'Authorization': f'{token}'} }"):
                ...
            with allure.step("""
            Body: {
            "queue_db_create_orders": 3,
            "queue_db_delete_orders": 1,
            "number_of_stuck_tasks": 0
           }"""):
                ...
        with allure.step('Response:'):
            with allure.step(f'Status code: {response.status_code}'):
                ...
            with allure.step(f'JSON: {response.text}'):
                ...
        return response

    @staticmethod
    def get_list_db_types():
        """
        Get databases type list.
        :return: Response
        """
        get_resource = '/list_dbtypes'  # Resource for method GET
        get_url = API.base_url + get_resource
        response = HttpMethods.get(url=get_url)
        with allure.step('Endpoint: /list_dbtypes'):
            ...
        with allure.step('Request:'):
            with allure.step(f'Url: {get_url}'):
                ...
            with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{None}'} }'):
                ...
            with allure.step(f'Body: {None}'):
                ...
        with allure.step('Response:'):
            with allure.step(f'Status code: {response.status_code}'):
                ...
            with allure.step(f'JSON: {response.text()}'):
                ...
        return response

    @staticmethod
    def get_list_dbversions():
        """
        Get list databases versions.
        :return: Response
        """
        get_resource = '/list_dbversions'  # Resource for method GET
        get_url = API.base_url + get_resource
        response = HttpMethods.get(url=get_url)
        with allure.step('Endpoint: /list_dbversions'):
            ...
        with allure.step('Request:'):
            with allure.step(f'Url: {get_url}'):
                ...
            with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{None}'} }'):
                ...
            with allure.step(f'Body: {None}'):
                ...
        with allure.step('Response:'):
            with allure.step(f'Status code: {response.status_code}'):
                ...
            with allure.step(f'JSON: {response.text()}'):
                ...
        return response

    @staticmethod
    def get_list_envs():
        """
        Get list environments.
        :return: Response
        """
        get_resource = '/list_dbenvs'  # Resource for method GET
        get_url = API.base_url + get_resource
        response = HttpMethods.get(url=get_url)
        with allure.step('Endpoint: /list_dbenvs'):
            ...
        with allure.step('Request:'):
            with allure.step(f'Url: {get_url}'):
                ...
            with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{None}'} }'):
                ...
            with allure.step(f'Body: {None}'):
                ...
        with allure.step('Response:'):
            with allure.step(f'Status code: {response.status_code}'):
                ...
            with allure.step(f'JSON: {response.text}'):
                ...
        return response

    @staticmethod
    def get_list_regions():
        """
        Get list regions.
        :return: Response
        """
        get_resource = '/list_regions'  # Resource for method GET
        get_url = API.base_url + get_resource
        response = HttpMethods.get(url=get_url)
        with allure.step('Endpoint: /list_regions'):
            ...
        with allure.step('Request:'):
            with allure.step(f'Url: {get_url}'):
                ...
            with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{None}'} }'):
                ...
            with allure.step(f'Body: {None}'):
                ...
        with allure.step('Response:'):
            with allure.step(f'Status code: {response.status_code}'):
                ...
            with allure.step(f'JSON: {response.text()}'):
                ...
        return response

    @staticmethod
    def get_bad_request():
        """
        Send bad request.
        :return: Response
        """
        get_resource = '/bad_request'  # Resource for method GET
        get_url = API.base_url + get_resource
        response = HttpMethods.get(url=get_url)
        with allure.step('Endpoint: /bad_request'):
            ...
        with allure.step('Request:'):
            with allure.step(f'Url: {get_url}'):
                ...
            with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{None}'} }'):
                ...
            with allure.step(f'Body: {None}'):
                ...
        with allure.step('Response:'):
            with allure.step(f'Status code: {response.status_code}'):
                ...
            with allure.step(f'JSON: {response.text}'):
                ...
        return response

    @staticmethod
    def get_check_downloading_backup():
        """
        Send bad request.
        :return: Response
        """
        db_name = 'db_cen6maxr'  # backup_2 user
        get_url = f'http://cis_db1.areso.pro/backups/{db_name}.sql'
        response = HttpMethods.get(url=get_url)
        with allure.step('Try to download backup:'):
            with allure.step(f'Url: {get_url}'):
                ...
            with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f''}}'):
                ...
            with allure.step(f'Body: {None}'):
                ...
        with allure.step('Response:'):
            with allure.step(f'Status code: {response.status_code}'):
                ...
            with allure.step(f'JSON: {response.text}'):
                ...
        return response

    @staticmethod
    def post_db_backup_create(token, db_uuid=None):
        """
        Create DB backup.
        :param token:
        :param db_uuid:
        :return: Response
        """
        post_resource = '/db_backup_create'  # Resource for method GET
        post_url = API.base_url + post_resource
        response = HttpMethods.post(
            url=post_url,
            body={"db_uuid": db_uuid},
            token=token)
        with allure.step('Endpoint: /db_backup_create'):
            ...
        with allure.step('Request:'):
            with allure.step(f'Url: {post_url}'):
                ...
            with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{token}'} }'):
                ...
            with allure.step("""Body: {"email": email, "password": password}"""):
                ...
        with allure.step('Response:'):
            with allure.step(f'Status code: {response.status_code}'):
                ...
            with allure.step(f'JSON: {response.text}'):
                ...
        return response

    @staticmethod
    def post_registration(email: str, old_password: str, language: str, tos_agree: bool):
        """
        Method for create new user.
        :param old_password:
        :param email:
        :param language:
        :param tos_agree:
        :return: Response
        """
        json_for_create_new_user = {"email": email,
                                    "password": old_password,
                                    "tos_agree": tos_agree,
                                    'language': language}

        post_resource = '/register'  # Resource for method POST
        post_url = API.base_url + post_resource
        response = HttpMethods.post(
            url=post_url,
            body=json_for_create_new_user)
        with allure.step('Endpoint: /bad_request'):
            ...
        with allure.step('Request:'):
            with allure.step(f'Url: {post_url}'):
                ...
            with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{None}'} }'):
                ...
            with allure.step(
                    f"""Body: 
                            {{
                            "email": email,
                            "password": password,
                            "tos_agree": {tos_agree},
                            "language": {language}
                           }}"""):
                ...
        with allure.step('Response:'):
            with allure.step(f'Status code: {response.status_code}'):
                ...
            with allure.step(f'JSON: {response.text()}'):
                ...
        return response

    @staticmethod
    def post_registration_variety_email(mail: str, old_password, prefix: str, language: str, tos_agree: bool):
        """
        Method for create new user.
        :param old_password:
        :type old_password:
        :param mail:
        :param prefix:
        :param language:
        :param tos_agree:
        :return: Response
        """
        with allure.step('post_registration_variety_email'):
            json_for_create_new_user = {"email": f'aqa{tests_api.data.data.time}@{mail}.{prefix}',
                                        "password": old_password,
                                        "tos_agree": tos_agree,
                                        "language": language}
            post_resource = '/register'
            post_url = API.base_url + post_resource
            response = HttpMethods.post(
                url=post_url,
                body=json_for_create_new_user)
            with allure.step('Endpoint: /register'):
                ...
            with allure.step('Request:'):
                with allure.step(f'Url: {post_url}'):
                    ...
                with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{None}'} }'):
                    ...
                with allure.step(
                        f"""Body: 
                                {{
                                "email": f'aqa{tests_api.data.data.time}@{mail}.{prefix}',
                                "password": password,
                                "tos_agree": {tos_agree},
                                "language": {language}
                               }}"""):
                    ...
            with allure.step('Response:'):
                with allure.step(f'Status code: {response.status_code}'):
                    ...
                with allure.step(f'JSON: {response.text()}'):
                    ...
            return response

    @staticmethod
    def post_login(body):
        """
        Method for login user.
        :param body:
        :return: Response
        """
        with allure.step('post_login'):
            post_resource = '/login'
            post_url = API.base_url + post_resource
            response = HttpMethods.post(
                url=post_url,
                body=body)
            with allure.step('Endpoint: /login'):
                ...
            with allure.step('Request:'):
                with allure.step(f'Url: {post_url}'):
                    ...
                with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{None}'} }'):
                    ...
                with allure.step("""Body: {"email": email, "password": password}"""):
                    ...
            with allure.step('Response:'):
                with allure.step(f'Status code: {response.status_code}'):
                    ...
                with allure.step(f'JSON: {response.text}'):
                    ...
            return response

    @staticmethod
    def post_is_logged(token):
        """
        :param token:
        :return: Response
        """
        with allure.step('post_is_logged'):
            post_resource = '/is_logged'
            post_url = API.base_url + post_resource
            response = HttpMethods.post(
                url=post_url,
                token=token)
            with allure.step('Endpoint: /is_logged'):
                ...
            with allure.step('Request:'):
                with allure.step(f'Url: {post_url}'):
                    ...
                with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{token}'} }'):
                    ...
                with allure.step(f"""Body: {None}"""):
                    ...
            with allure.step('Response:'):
                with allure.step(f'Status code: {response.status_code}'):
                    ...
                with allure.step(f'JSON: {response.text()}'):
                    ...
            return response

    @staticmethod
    def post_is_logged_with_wrong_token():
        """
        :return: Response
        """
        with allure.step('post_is_logged'):
            post_resource = '/is_logged'
            post_url = API.base_url + post_resource
            response = HttpMethods.post(
                url=post_url,
                token=1)
            with allure.step('Endpoint: /is_logged'):
                ...
            with allure.step('Request:'):
                with allure.step(f'Url: {post_url}'):
                    ...
                with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{1}'} }'):
                    ...
                with allure.step(f"""Body: {None}"""):
                    ...
            with allure.step('Response:'):
                with allure.step(f'Status code: {response.status_code}'):
                    ...
                with allure.step(f'JSON: {response.text()}'):
                    ...
            return response

    @staticmethod
    def post_logout(token):
        """
        :return: Response
        """
        with allure.step('post_is_logged'):
            post_resource = '/logout'
            post_url = API.base_url + post_resource
            response = HttpMethods.post(
                url=post_url,
                token=token)
            with allure.step('Endpoint: /logout'):
                ...
            with allure.step('Request:'):
                with allure.step(f'Url: {post_url}'):
                    ...
                with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{token}'} }'):
                    ...
                with allure.step(f"""Body: {None}"""):
                    ...
            with allure.step('Response:'):
                with allure.step(f'Status code: {response.status_code}'):
                    ...
                with allure.step(f'JSON: {response.text()}'):
                    ...
            return response

    @staticmethod
    def post_db_list(token: str):
        """
        :param token:
        :return: Response
        """
        with allure.step('post_db_list'):
            post_resource = '/db_list'  # Resource for method
            post_url = API.base_url + post_resource
            response = HttpMethods.post(
                url=post_url,
                token=token)
            with allure.step('Endpoint: /db_list'):
                ...
            with allure.step('Request:'):
                with allure.step(f'Url: {post_url}'):
                    ...
                with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{token}'} }'):
                    ...
                with allure.step(f"""Body: {None}"""):
                    ...
            with allure.step('Response:'):
                with allure.step(f'Status code: {response.status_code}'):
                    ...
                with allure.step(f'JSON: {response.text}'):
                    ...
            return response

    @staticmethod
    def post_container_list(token: str):
        """
        :param token:
        :return: Response
        """
        with allure.step('post_container_list'):
            post_resource = '/container_list'  # Resource for method
            post_url = API.base_url + post_resource
            response = HttpMethods.post(
                url=post_url,
                token=token)
            with allure.step('Endpoint: /container_list'):
                ...
            with allure.step('Request:'):
                with allure.step(f'Url: {post_url}'):
                    ...
                with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{token}'} }'):
                    ...
                with allure.step(f"""Body: {None}"""):
                    ...
            with allure.step('Response:'):
                with allure.step(f'Status code: {response.status_code}'):
                    ...
                with allure.step(f'JSON: {response.text()}'):
                    ...
            return response

    @staticmethod
    def post_change_password(token: str, old_password: str, new_password: str):
        """
        Body example {"current_password":"", "new_password":""}.
        :param token:
        :param old_password:
        :param new_password:
        :return: Response
        """
        with allure.step('post_change_password'):
            post_resource = '/password_update'  # Resource for method
            post_url = API.base_url + post_resource
            response = HttpMethods.post(
                url=post_url,
                body={"current_password": old_password, "new_password": new_password},
                token=token)
            with allure.step('Endpoint: /password_update'):
                ...
            with allure.step('Request:'):
                with allure.step(f'Url: {post_url}'):
                    ...
                with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{token}'} }'):
                    ...
                with allure.step("""Body: {"current_password": old_password, "new_password": new_password}"""):
                    ...
            with allure.step('Response:'):
                with allure.step(f'Status code: {response.status_code}'):
                    ...
                with allure.step(f'JSON: {response.text()}'):
                    ...
            return response

    @staticmethod
    def post_db_list_with_filter(token: str, db_uuid: str):
        """
        Getting information about bd by uuid
        :param token: dict
        :param db_uuid: str
        :return: Response
        """
        with allure.step('post_db_list_with_filter'):
            post_resource = '/db_list'  # Resource for method
            post_url = API.base_url + post_resource
            response = HttpMethods.post(
                url=post_url,
                body={"db_uuid": db_uuid},
                token=token)
            with allure.step('Endpoint: /db_list'):
                ...
            with allure.step('Request:'):
                with allure.step(f'Url: {post_url}'):
                    ...
                with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{token}'} }'):
                    ...
                with allure.step("""Body: {"db_uuid": db_uuid}"""):
                    ...
            with allure.step('Response:'):
                with allure.step(f'Status code: {response.status_code}'):
                    ...
                with allure.step(f'JSON: {response.text}'):
                    ...
            return response

    @staticmethod
    def post_db_create(token: str):
        """
        :param token:
        :return: Response
        """
        with allure.step('post_db_create'):
            post_resource = '/db_create'  # Resource for method
            post_url = API.base_url + post_resource
            body = {"dbtype": 3, "dbversion": 5, "env": 3, "region": 3}
            response = HttpMethods.post(
                url=post_url,
                body=body,
                token=token)
            with allure.step('Endpoint: /db_create'):
                ...
            with allure.step('Request:'):
                with allure.step(f'Url: {post_url}'):
                    ...
                with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{token}'} }'):
                    ...
                with allure.step("""Body: {"dbtype": 3, "dbversion": 5, "env": 3, "region": 3}"""):
                    ...
            with allure.step('Response:'):
                with allure.step(f'Status code: {response.status_code}'):
                    ...
                with allure.step(f'JSON: {response.text}'):
                    ...
            return response

    @staticmethod
    def post_db_create_wrong_value_db_type(token: str):
        """
        :param token:
        :return: Response
        """
        with allure.step('post_db_create_wrong_value_db_type'):
            post_resource = '/db_create'  # Resource for method
            post_url = API.base_url + post_resource
            random_value = random.randint(4, 100)
            body = {"dbtype": random_value, "dbversion": 5, "env": 3, "region": 3}
            response = HttpMethods.post(
                url=post_url,
                body=body,
                token=token)
            with allure.step('Endpoint: /db_create'):
                ...
            with allure.step('Request:'):
                with allure.step(f'Url: {post_url}'):
                    ...
                with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{token}'} }'):
                    ...
                with allure.step(f"""Body: {{"dbtype": f'{random_value}', "dbversion": 5, "env": 3, "region": 3}}"""):
                    ...
            with allure.step('Response:'):
                with allure.step(f'Status code: {response.status_code}'):
                    ...
                with allure.step(f'JSON: {response.text()}'):
                    ...
            return response

    @staticmethod
    def post_db_create_wrong_value_db_version(token: str):
        """
        :param token:
        :return: Response
        """
        with allure.step('post_db_create_wrong_value_db_version'):
            post_resource = '/db_create'  # Resource for method
            post_url = API.base_url + post_resource
            random_value = random.randint(6, 100)
            body = {"dbtype": 3, "dbversion": random_value, "env": 3, "region": 3}
            response = HttpMethods.post(
                url=post_url,
                body=body,
                token=token)
            with allure.step('Endpoint: /db_create'):
                ...
            with allure.step('Request:'):
                with allure.step(f'Url: {post_url}'):
                    ...
                with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{token}'} }'):
                    ...
                with allure.step(f"""Body: {{"dbtype": 3, "dbversion": {random_value}, "env": 3, "region": 3}}"""):
                    ...
            with allure.step('Response:'):
                with allure.step(f'Status code: {response.status_code}'):
                    ...
                with allure.step(f'JSON: {response.text()}'):
                    ...
            return response

    @staticmethod
    def post_db_create_wrong_value_env(token: str):
        """
        :param token:
        :return: Response
        """
        with allure.step('post_db_create_wrong_value_env'):
            post_resource = '/db_create'
            post_url = API.base_url + post_resource
            random_value = random.randint(4, 100)
            body = {"dbtype": 3, "dbversion": 5, "env": random_value, "region": 3}
            response = HttpMethods.post(
                url=post_url,
                body=body,
                token=token)
            with allure.step('Endpoint: /db_create'):
                ...
            with allure.step('Request:'):
                with allure.step(f'Url: {post_url}'):
                    ...
                with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{token}'} }'):
                    ...
                with allure.step(f"""Body: {{"dbtype": 3, "dbversion": 5, "env": {random_value}, "region": 3}}"""):
                    ...
            with allure.step('Response:'):
                with allure.step(f'Status code: {response.status_code}'):
                    ...
                with allure.step(f'JSON: {response.text()}'):
                    ...
            return response

    @staticmethod
    def post_db_create_wrong_value_region(token: str):
        """
        :param token:
        :return: Response
        """
        with allure.step('post_db_create_wrong_value_region'):
            post_resource = '/db_create'
            post_url = API.base_url + post_resource
            random_value = random.randint(4, 100)
            body = {"dbtype": 3, "dbversion": 5, "env": 3, "region": random_value}
            response = HttpMethods.post(
                url=post_url,
                body=body,
                token=token)
            with allure.step('Endpoint: /db_create'):
                ...
            with allure.step('Request:'):
                with allure.step(f'Url: {post_url}'):
                    ...
                with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{token}'} }'):
                    ...
                with allure.step(f"""Body: {{"dbtype": 3, "dbversion": 5, "env": 3, "region": {random_value}}}"""):
                    ...
            with allure.step('Response:'):
                with allure.step(f'Status code: {response.status_code}'):
                    ...
                with allure.step(f'JSON: {response.text()}'):
                    ...
            return response

    @staticmethod
    def post_create_docker_container(token):
        with allure.step('post_create_docker_container'):
            post_resource = '/container_create'
            post_url = API.base_url + post_resource
            body = {"docker_image": "nginx", "int_ports": "80", "env": 3, "region": 3}
            response = HttpMethods.post(
                url=post_url,
                body=body,
                token=token)
            with allure.step('Endpoint: /container_create'):
                ...
            with allure.step('Request:'):
                with allure.step(f'Url: {post_url}'):
                    ...
                with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{token}'} }'):
                    ...
                with allure.step(f"""Body: {{"docker_image": "nginx", "int_ports": "80", "env": 3, "region": 3}}"""):
                    ...
            with allure.step('Response:'):
                with allure.step(f'Status code: {response.status_code}'):
                    ...
                with allure.step(f'JSON: {response.text()}'):
                    ...
            return response

    @staticmethod
    def post_create_docker_container_checking_ports(token, port_len):
        with allure.step('post_create_docker_container'):
            post_resource = '/container_create'
            post_url = API.base_url + post_resource
            body = {"docker_image": "nginx", "int_ports": f"{port_len}", "env": 3, "region": 3}
            response = HttpMethods.post(
                url=post_url,
                body=body,
                token=token)
            with allure.step('Endpoint: /container_create'):
                ...
            with allure.step('Request:'):
                with allure.step(f'Url: {post_url}'):
                    ...
                with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{token}'} }'):
                    ...
                with allure.step(
                        f"""Body: {{"docker_image": "nginx", "int_ports": f"{port_len}", "env": 3, "region": 3}}"""):
                    ...
            with allure.step('Response:'):
                with allure.step(f'Status code: {response.status_code}'):
                    ...
                with allure.step(f'JSON: {response.text()}'):
                    ...
            return response

    @staticmethod
    def post_create_docker_container_with_defunct_image(token):
        with allure.step('post_create_docker_container_with_defunct_image'):
            post_resource = '/container_create'
            post_url = API.base_url + post_resource
            body = {"docker_image": "", "int_ports": "80", "env": 3, "region": 3}
            response = HttpMethods.post(
                url=post_url,
                body=body,
                token=token)
            with allure.step('Endpoint: /container_create'):
                ...
            with allure.step('Request:'):
                with allure.step(f'Url: {post_url}'):
                    ...
                with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{token}'} }'):
                    ...
                with allure.step(
                        f"""Body: {{"docker_image": "", "int_ports": "80", "env": 3, "region": 3}}"""):
                    ...
            with allure.step('Response:'):
                with allure.step(f'Status code: {response.status_code}'):
                    ...
                with allure.step(f'JSON: {response.text()}'):
                    ...
            return response

    @staticmethod
    def post_delete_docker_container(token, list_index: int):
        with allure.step('post_delete_docker_container'):
            post_resource = '/container_delete'
            post_url = API.base_url + post_resource
            result_list = API.post_container_list(token)
            docker_uuid = list(result_list.json()['data'])[list_index]
            body = {'docker_uuid': f'{docker_uuid}'}
            time.sleep(20)
            response = HttpMethods.post(
                url=post_url,
                body=body,
                token=token)
            with allure.step('Endpoint: /container_delete'):
                ...
            with allure.step('Request:'):
                with allure.step(f'Url: {post_url}'):
                    ...
                with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{token}'} }'):
                    ...
                with allure.step(
                        f"""Body: {{'docker_uuid': f'{docker_uuid}'}}"""):
                    ...
            with allure.step('Response:'):
                with allure.step(f'Status code: {response.status_code}'):
                    ...
                with allure.step(f'JSON: {response.text()}'):
                    ...
            return response

    @staticmethod
    def delete_db(db_uuid, token):
        """
        :param db_uuid:
        :param token:
        :return: Response
        """
        with allure.step('delete_db'):
            delete_resource = '/db_delete'
            delete_url = API.base_url + delete_resource
            db_uuid = {"db_uuid": f"{db_uuid}"}
            json_db_uuid = db_uuid
            response = HttpMethods.post(
                url=delete_url,
                body=json_db_uuid,
                token=token)
            with allure.step('Endpoint: /container_delete'):
                ...
            with allure.step('Request:'):
                with allure.step(f'Url: {delete_url}'):
                    ...
                with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{token}'} }'):
                    ...
                with allure.step(f"""Body: {{"db_uuid": f"{db_uuid}"}}"""):
                    ...
            with allure.step('Response:'):
                with allure.step(f'Status code: {response.status_code}'):
                    ...
                with allure.step(f'JSON: {response.text}'):
                    ...
            return response

    @staticmethod
    def delete_all_created_db(token):
        start = datetime.now().time().strftime('%H:%M')
        print('Start', start)
        while True:
            finish = datetime.now().time().strftime('%H:%M')
            print('Finish', finish)
            list_db = API.post_db_list(token)
            json_list_db = list_db.json()['data']
            if json_list_db == {}:
                break
            else:
                first_db_uuid = list(json_list_db)[-1]
                API.delete_db(first_db_uuid, token)
                time.sleep(5)
                if start != finish:
                    break
        list_db = API.post_db_list(token)
        json_list_db = list_db.json()['data']
        return json_list_db

    @staticmethod
    def post_static_webpages(token):
        with allure.step('webpage_list'):
            post_resource = '/webpage_list'
            post_url = API.base_url + post_resource
            response = HttpMethods.post(
                url=post_url,
                token=token)
            with allure.step('Endpoint: /webpage_list'):
                ...
            with allure.step('Request:'):
                with allure.step(f'Url: {post_url}'):
                    ...
                with allure.step(f'Headers: {HttpMethods.headers | {'Authorization': f'{None}'} }'):
                    ...
            with allure.step('Response:'):
                with allure.step(f'Status code: {response.status_code}'):
                    ...
                with allure.step(f'JSON: {response.text}'):
                    ...
            return response

    @staticmethod
    def check_full_cycle(token):
        with allure.step('check_full_cycle'):
            print('\nCheck Time: ', str(datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
            start_value_db_list = API.post_db_list(token)
            # API.get_profile(token)
            # API.post_db_list(token)
            result_db_create = API.post_db_create(token)
            Checking.check_status_code(result_db_create, 201)
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

    @staticmethod
    def create_table():
        time.sleep(20)
        with allure.step('Create table.'):
            query = '''
                    CREATE TABLE IF NOT EXISTS accounts(
                    userid INT PRIMARY KEY AUTO_INCREMENT,
                    name varchar(128),
                    date_of_birth datetime NULL,
                    text varchar(4096),
                    email varchar(128) NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
                    '''
            return query

    @staticmethod
    def load_db(db):
        letters = ascii_letters
        cursor = db.cursor()
        with allure.step('Insert records to the database'):
            for x in range(10):
                for i in range(10):
                    my_string = "".join(random.choice(letters) for _ in range(4096))
                    cursor.execute("""
                                            INSERT INTO accounts (name, text)
                                            VALUES (
                                            'lambotik',
                                            %(my_string)s);""",
                                   {'my_string': my_string})
                    db.commit()
                db.commit()
            cursor.execute('''select * from accounts''')
            # res = cursor.fetchall()
            # print(res)
            time.sleep(40)

    @staticmethod
    def connection(db_uuid, token, body):
        post_resource = '/db_list'
        post_url = API.base_url + post_resource
        result_post = HttpMethods.post(post_url, token=token, body=body)
        json_list_db = result_post.json()
        db_name = json_list_db['data'][db_uuid][0]
        user_name = json_list_db['data'][db_uuid][3].split(':')[1].replace('//', '')
        host = json_list_db['data'][db_uuid][3].split(':')[2].partition('@')[2]
        password_db = json_list_db['data'][db_uuid][3].split(':')[2].partition('@')[0]
        print('\nConnecting to DB...')
        db = mysql.connector.connect(host=host,
                                     port=3306,
                                     user=user_name,
                                     database=db_name,
                                     password=password_db,
                                     autocommit=True
                                     )
        print('Successfully connected...')
        assert db.is_connected() is True
        return db

    @staticmethod
    def delete_db_by_index_list(token: str, json_list_db: dict, list_db_index: int):
        try:
            first_db_uuid = list(json_list_db['data'])[list_db_index]
            response_db_delete = API.delete_db(
                db_uuid=first_db_uuid,
                token=token)
            Checking.check_status_code(response_db_delete, 200)
        except IndexError as ex:
            print(ex)
            assert str(ex) == 'list index out of range', 'Db list is empty.'
