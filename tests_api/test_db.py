import json
import random
import time
from datetime import datetime

import allure
import pytest

from .loading_report_dir.loading_report_path import LOADING_REPORT_DIR
from .utils.checking import Checking
from .utils.request import API


@allure.suite('smoke_databases')
class TestPOST:
    token = None
    body = None
    new_password = None
    old_password = None
    email = None

    @allure.title('POST get token and other params.')
    def test_get_token_and_body(self, get_token):
        TestPOST.token, TestPOST.body, TestPOST.new_password, TestPOST.old_password, TestPOST.email = get_token[0], \
            get_token[1], get_token[2], get_token[3], get_token[4]

    
    @allure.title('POST db_create')
    def test_post_db_create(self, get_token):
        TestPOST.token, TestPOST.body = get_token[0], get_token[1]
        response_login = API.post_login(body=TestPOST.body)
        Checking.check_status_code(response_login, 200)
        response = API.post_db_create(token=TestPOST.token)
        print(response.text)
        Checking.check_status_code(response, 201)

    @allure.title('POST db_create_with_wrong_db_type.')
    def test_post_db_create_with_wrong_values_dbtype(self):
        response_db_list = API.post_db_create_wrong_value_db_type(token=TestPOST.token)
        Checking.check_status_code(response_db_list, 400)
        Checking.check_json_search_word_in_value(
            response_db_list, "content",
            "error: DB type isn't found or isn't available for order")

    @allure.title('POST db_create_with_wrong_db_version.')
    def test_post_db_create_with_wrong_values_db_version(self):
        response_db_list = API.post_db_create_wrong_value_db_version(token=TestPOST.token)
        Checking.check_status_code(response_db_list, 400)
        Checking.check_json_search_word_in_value(
            response_db_list, "content",
            "error: DB version isn't found or isn't available for order")

    @allure.title('POST db_create_with_wrong_env.')
    def test_post_db_create_with_wrong_values_env(self):
        response_db_list = API.post_db_create_wrong_value_env(token=TestPOST.token)
        Checking.check_status_code(response_db_list, 400)
        Checking.check_json_search_word_in_value(
            response_db_list, "content",
            "error: DB environment isn't found or isn't available for order")

    @allure.title('POST db_create_with_wrong_region.')
    def test_post_db_create_with_wrong_values_region(self):
        response_db_list = API.post_db_create_wrong_value_region(token=TestPOST.token)
        Checking.check_status_code(response_db_list, 400)
        Checking.check_json_search_word_in_value(
            response_db_list, "content",
            "error: region isn't found or isn't available for order")

    @allure.title('POST db_list')
    def test_post_db_list(self):
        response_db_list = API.post_db_list(token=TestPOST.token)
        Checking.check_status_code(response_db_list, 200)


    @allure.title('POST db_list_with_filter')
    def test_post_db_list_with_filter(self):
        time.sleep(15)
        list_db       = API.post_db_list(token=TestPOST.token)
        json_list_db  = json.loads(list_db.text)
        first_db_uuid = list(json_list_db['data'])[-1]
        print(f"first_db_uuid is {first_db_uuid}")
        response_db_list =API.post_db_list_with_filter(
            token=TestPOST.token,
            db_uuid=first_db_uuid)
        Checking.check_status_code(response_db_list, 200)


    @allure.title('POST delete_db')
    def test_delete_db(self):
        time.sleep(60) 
        list_db       = API.post_db_list(token=TestPOST.token)
        json_list_db  = json.loads(list_db.text)
        first_db_uuid = list(json_list_db['data'])[-1]
        print(f"first_db_uuid is {first_db_uuid}")
        response_db_deleted =API.post_db_delete(
            token=TestPOST.token,
            db_uuid=first_db_uuid)
        Checking.check_status_code(response_db_deleted, 200)
