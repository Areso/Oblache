import allure
import requests

from utils.logger import Logger

'''List http methods'''


class HttpMethods:
    headers = {'Content-Type': 'application/json'}
    cookie = ''

    @staticmethod
    @allure.step('Method GET')
    def get(url):
        Logger.add_request(url, method='GET')
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    @allure.step('Method POST')
    def post(url, body):
        Logger.add_request(url, method='POST')
        result = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    @allure.step('Method POST')
    def post_set_cookie(url: str, body: dict, cookie: dict):
        Logger.add_request(url, method='POST')
        result = requests.post(url, cookies=cookie, json=body)
        Logger.add_response(result)
        return result

    @staticmethod
    @allure.step('Method POST')
    def post_for_delete_db(url, db_uuid, sid):
        Logger.add_request(url, method='POST')
        result = requests.post(url, data=db_uuid, cookies=sid)
        Logger.add_response(result)
        return result

    @staticmethod
    @allure.step('Method POST')
    def post_set_cookie_without_body(url: str, cookie: dict, body: dict):
        Logger.add_request(url, method='POST')
        result = requests.post(url, cookies=cookie, json=body)
        Logger.add_response(result)
        return result

    @staticmethod
    @allure.step('Method PUT')
    def put(url, body):
        Logger.add_request(url, method='PUT')
        result = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    @allure.step('Method DELETE')
    def delete(url, body):
        Logger.add_request(url, method='DELETE')
        result = requests.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        Logger.add_response(result)
        return result
