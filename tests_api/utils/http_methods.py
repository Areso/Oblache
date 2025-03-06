import allure
import requests

from tests_api.utils.logger import Logger
import logging


class HttpMethods:
    base_url = 'https://dbend.areso.pro'
    headers = {'Content-Type': 'application/json'}
    cookie = ''

    @staticmethod
    def get(endpoint: str, body=None, token=None) -> requests.Response:
        """
        :param endpoint:
        :param body:
        :param token:
        :return:
        """
        response = requests.get(
            url=HttpMethods.base_url + endpoint,
            headers=HttpMethods.headers | {'Authorization': f'{token}'},
            cookies=HttpMethods.cookie,
            json=body)
        logging.info(f'GET запрос на {HttpMethods.base_url + endpoint}.\nКод ответа: {response.status_code}')
        logging.info(response.text)
        return response

    @staticmethod
    def post(endpoint: str, body=None, token=None, data=None, cookie=None, json=None):
        """
        :param endpoint:
        :param body:
        :param token:
        :param data:
        :param cookie:
        :param json
        :return:
        """
        response = requests.post(
            url=HttpMethods.base_url + endpoint,
            json=body,
            headers=HttpMethods.headers | {'Authorization': f'{token}'})
        logging.info(
            f'POST запрос на {HttpMethods.base_url + endpoint} c данными\nbody:{body}\njson:{json}\ndata:{data}.\n'
            f'Код ответа: {response.status_code}')
        logging.info(response.text)
        return response

    @staticmethod
    def post_for_delete_db(url, db_uuid, sid):
        """
        :param url:
        :param db_uuid:
        :param sid:
        :return:
        """
        Logger.add_request(url, method='POST')
        response = requests.post(url, data=db_uuid, cookies=sid)
        with allure.step(f'Status code: {response.status_code}'):
            pass
        with allure.step(f'Params url: {url}'):
            pass
        with allure.step(f'Response: {response.json()}'):
            pass
        Logger.add_response(response)
        return response
