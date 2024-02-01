import allure
import requests

from utils.logger import Logger

'''List http methods'''


class HttpMethods:
    headers = {'Content-Type': 'application/json'}
    cookie = ''

    @staticmethod
    # @allure.step('Method GET')
    def get(url):
        """
        :param url:
        :return:
        """
        Logger.add_request(url, method='GET')
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        with allure.step(f'Status code: {result.status_code}'):
            pass
        with allure.step(f'Response: {result.text}'):
            pass
        Logger.add_response(result)
        return result

    @staticmethod
    # @allure.step('Method GET')
    def get_with_cookie(url: str, body: dict, cookie: dict):
        """
        :param url:
        :param body:
        :param cookie:
        :return: result
        """
        Logger.add_request(url, method='GET')
        result = requests.get(url, cookies=cookie, json=body)
        with allure.step(f'Status code: {result.status_code}'):
            pass
        with allure.step(f'Params url: {url}\n'
                         f'Cookies: {cookie}\n'
                         f'Body: {body}'):
            pass
        with allure.step(f'Response: {result.text}'):
            pass
        Logger.add_response(result)
        return result

    @staticmethod
    # @allure.step('Method POST')
    def post(url, body):
        Logger.add_request(url, method='POST')
        result = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        with allure.step(f'Status code: {result.status_code}'):
            pass
        with allure.step(f'Params url: {url}\n'
                         f'Body: {body}'):
            pass
        with allure.step(f'Response: {result.text}'):
            pass
        Logger.add_response(result)
        return result

    @staticmethod
    # @allure.step('Method POST')
    def post_with_cookie(url: str, body: dict, cookie: dict):
        """
        :param url:
        :param body:
        :param cookie:
        :return: result
        """
        Logger.add_request(url, method='POST')
        result = requests.post(url, cookies=cookie, json=body)
        with allure.step(f'Status code: {result.status_code}'):
            pass
        with allure.step(f'Params url: {url}\n'
                         f'Cookies: {cookie}\n'
                         f'Body: {body}'):
            pass
        with allure.step(f'Response: {result.text}'):
            pass
        Logger.add_response(result)
        return result

    @staticmethod
    # @allure.step('Method POST')
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
        with allure.step(f'Params url: {url}\n'
                         f'Db uuid: {db_uuid}\n'
                         f'Sid: {sid}'):
            pass
        with allure.step(f'Response: {result.text}'):
            pass
        Logger.add_response(result)
        return result

    @staticmethod
    # @allure.step('Method POST')
    def post_with_cookie_without_body(url: str, cookie: dict, body: dict):
        """
        :param url:
        :param cookie:
        :param body:
        :return:
        """
        Logger.add_request(url, method='POST')
        result = requests.post(url, cookies=cookie, json=body)
        with allure.step(f'Status code: {result.status_code}'):
            pass
        with allure.step(f'Params url: {url}\n'
                         f'Cookies: {cookie}\n'
                         f'Body: {body}'):
            pass
        with allure.step(f'Response: {result.text}'):
            pass
        Logger.add_response(result)
        return result

    @staticmethod
    @allure.step('Method PUT')
    def put(url, body):
        """
        :param url:
        :param body:
        :return:
        """
        Logger.add_request(url, method='PUT')
        result = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    @allure.step('Method DELETE')
    def delete(url, body):
        """
        :param url:
        :param body:
        :return:
        """
        Logger.add_request(url, method='DELETE')
        result = requests.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        Logger.add_response(result)
        return result
