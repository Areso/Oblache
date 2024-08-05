"""Methods for checking requests"""
import json

import allure
import requests


class Checking:

    def __init__(self):
        pass

    @staticmethod
    def check_status_code(result: requests.models.Response, status_code: int):
        """
        Method check status code
        :param result: Response
        :param status_code:
        """
        with allure.step(f'Assert status code: {status_code} == Response status code: {result.status_code}'):
            assert status_code == result.status_code, 'Incorrect status code'
            print(f'Assert expected status code: {status_code} == Response status code: {result.status_code}')

    """Method for validating fields in a response"""

    @staticmethod
    def check_json_token(result: requests.models.Response, expected_value: list):
        """
        Method check key in body
        :param result: requests.models.Response
        :param expected_value: list of the keys
        """
        token = json.loads(result.text)
        """list(token) generated list of keys from json"""
        assert list(token) == expected_value, 'Not all fields are presented'
        print(f'All body keys is present: {list(token)}')

    @staticmethod
    def check_json_many_tokens(result: requests.models.Response, first_key: str, expected_value: list):
        """
        The method gets a list of nested dictionary keys by the parent dictionary key
        :param result: requests.models.Response
        :param first_key: str
        :param expected_value: list of the keys
        """
        token = json.loads(result.text)
        token = token[first_key]
        """list(token) generated list of keys from json"""
        assert list(token) == expected_value, 'Not all fields are presented'
        print(f'All body keys is present: {list(token)}')

    """Method for checking values of required fields in response"""

    @staticmethod
    def check_json_value(response: requests.models.Response, field_name: str, expected_value):
        """
        :param response: requests.models.Response
        :param field_name:
        :param expected_value:
        """
        check = response.json()
        check_info = check.get(field_name)
        with allure.step(
                f'Compare result request with expected value:'
                f'\nResponse: {response}\nField name: {field_name}\nValue: {expected_value}'):
            assert check_info == expected_value, 'Result is not equal expected value'
            print(f'{field_name}: {expected_value}: is correct')

    @staticmethod
    def check_json_search_word_in_value(response, key, search_word):
        """
        Checks if the required string is in the response JSON by key
        :param response: requests.models.Response
        :param key: str()
        :param search_word: str()
        :return: answer
        """
        check = response.json()
        check_info = check.get(key)
        with allure.step(
                f'Check and compare result request with expected value by key:'
                f'\nResponse: {response}\nKey: {key}\nValue: {search_word}'):
            assert search_word in check_info, f'{check_info} is not presence'
            print(f'Value: {search_word}\nis presence in key: {key}')

    @staticmethod
    def check_json_search_word_in_values(response, key, search_word):
        """
        Checks if the required string is in the dictionary by key
        :param response: requests.models.Response
        :param key:
        :param search_word:
        :return: answer
        """
        with allure.step(
                f'Check and compare that expected value is presence in response:'
                f'\nResponse: {response}\nKey: {key}\nValue: {search_word}'):
            assert str(search_word) in str(response[key]), f'{str(key)} is not presence'
            print(f'Value: {search_word}, is presence in: {key}')
