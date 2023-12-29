"""Methods for checking requests"""
import json

import requests


class Checking:

    @staticmethod
    def check_status_code(result: requests.models.Response, status_code: int):
        """
        Method check status code
        :param result: Response JSON
        :param status_code:
        :return: int
        """
        assert status_code == result.status_code, 'Incorrect status code'
        print(f'Status code is: {result.status_code}')

    """Method for validating fields in a response"""

    @staticmethod
    def check_json_token(result: requests.models.Response, expected_value: list):
        """
        Method check key in body
        :param result: Response JSON
        :param expected_value: list of the keys
        :return: assert
        """
        token = json.loads(result.text)
        """list(token) generated list of keys from json"""
        assert list(token) == expected_value, 'Not all fields are presented'
        print(f'All body keys is present: {list(token)}')

    @staticmethod
    def check_json_many_tokens(result: requests.models.Response, first_key: str, expected_value: list):
        """
        The method gets a list of nested dictionary keys by the parent dictionary key
        :param result: Response JSON
        :param first_key: str
        :param expected_value: list of the keys
        :return: assert
        """
        token = json.loads(result.text)
        token = token[first_key]
        """list(token) generated list of keys from json"""
        assert list(token) == expected_value, 'Not all fields are presented'
        print(f'All body keys is present: {list(token)}')

    """Method for checking values of required fields in response"""

    @staticmethod
    def check_json_value(response: json, field_name: str, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, 'Result is not equal expected value'
        print(f'{field_name}: {expected_value}: is correct')

    @staticmethod
    def check_json_search_word_in_value(response, key, search_word):
        """
        Checks if the required string is in the response JSON by key
        :param response: JSON
        :param key: str()
        :param search_word: str()
        :return: answer
        """
        check = response.json()
        check_info = check.get(key)
        assert search_word in check_info, f'{check_info} is not presence'
        print(f'Value: {search_word}, is presence in: {key}')

    @staticmethod
    def check_json_search_word_in_values(response, key, search_word):
        """
        Checks if the required string is in the dictionary by key
        :param response:
        :param key:
        :param search_word:
        :return: answer
        """
        assert str(search_word) in str(response[key]), f'{str(key)} is not presence'
        print(f'Value: {search_word}, is presence in: {key}')
