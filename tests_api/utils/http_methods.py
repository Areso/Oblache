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
        result = requests.get(url, headers=HttpMethods.headers | {'Authorization': f'{token}'},
                              cookies=HttpMethods.cookie)

        with allure.step(f'Status code: {result.status_code}'):
            pass
        with allure.step(f'Response: {result.text}'):
            pass
        Logger.add_response(result)
        return result

    @staticmethod
    def post(url, body=None, token=None, data=None, cookie=None):
        """
        :param url:
        :param body:
        :param token:
        :param data:
        :param cookie:
        :return:
        """
        Logger.add_request(url, method='POST')
        # HttpMethods.headers['Authorization'] = token
        result = requests.post(url, json=body,
                               headers=HttpMethods.headers | {'Authorization': f'{token}'})
        with allure.step(f'Status code: {result.status_code}'):
            pass
        with allure.step(f'Params url: {url}'):
            pass
        with allure.step(f'Response: {result}'):
            pass
        Logger.add_response(result)
        return result

    @staticmethod
    def post_for_delete_db(url, db_uuid, sid):
        """
        :param url:
        :param db_uuid:
        :param sid:
        :return:
        """
        Logger.add_request(url, method='POST')
        result = requests.post(url, data=db_uuid, cookies=sid)
        with allure.step(f'Status code: {result.status_code}'):
            pass
        with allure.step(f'Params url: {url}'):
            pass
        with allure.step(f'Response: {result}'):
            pass
        Logger.add_response(result)
        return result
