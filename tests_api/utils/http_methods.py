import allure
import requests

from tests_api.utils.logger import Logger


class HttpMethods:
    headers = {'Content-Type': 'application/json'}
    cookie = ''

    @staticmethod
    def get(url, body=None, token=None):
        """
        :param url:
        :param body:
        :param token:
        :return:
        """
        Logger.add_request(url, method='GET')
        response = requests.get(
            url=url,
            headers=HttpMethods.headers | {'Authorization': f'{token}'},
            cookies=HttpMethods.cookie,
            json=body)
        Logger.add_response(response)
        return response

    @staticmethod
    def post(url, body=None, token=None, data=None, cookie=None, json=None):
        """
        :param url:
        :param body:
        :param token:
        :param data:
        :param cookie:
        :param json
        :return:
        """
        Logger.add_request(
            url=url,
            method='POST')
        # HttpMethods.headers['Authorization'] = token
        response = requests.post(
            url=url,
            json=body,
            headers=HttpMethods.headers | {'Authorization': f'{token}'})
        Logger.add_response(response)
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
