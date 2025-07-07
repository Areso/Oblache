import json
import random
import time
from datetime import datetime

import allure
import pytest

from .loading_report_dir.loading_report_path import LOADING_REPORT_DIR
from .utils.checking import Checking
from .utils.request import API


@allure.epic('Connection DB')
@allure.suite('Test Connection DB')
@allure.severity(allure.severity_level.CRITICAL)

@allure.suite('GET')
class TestGET:
    token = None

    @allure.title('Get token.')
    def test_get_token(self, get_token):
        TestGET.token = get_token[0]
        assert TestGET.token is not None, 'Token is None.'

    @allure.title('GET tos.')
    def test_tos(self):
        response = API.get_tos(token=TestGET.token)
        file_name = LOADING_REPORT_DIR / 'my_report1.html'
        attach = file_name
        allure.attach.file(attach, name=f"Report {datetime.today()}", attachment_type=allure.attachment_type.HTML)
        Checking.check_status_code(response, 200)

#    @allure.title('GET profile information.')
#    def test_get_profile(self):
#        response = API.get_profile(token=TestGET.token)
#        Checking.check_status_code(response, 200)

    @allure.title('GET list list_dbtypes.')
    def test_get_list_db_types(self):
        response = API.get_list_db_types()
        Checking.check_status_code(response, 200)

    @allure.title('GET list db_versions.')
    def test_get_list_db_versions(self):
        response = API.get_list_dbversions()
        Checking.check_status_code(response, 200)

    @allure.title('GET list list_dbenvs.')
    def test_get_list_envs(self):
        response = API.get_list_envs()
        Checking.check_status_code(response, 200)

    @allure.title('GET list list_regions.')
    def test_get_list_regions(self):
        response = API.get_list_regions()
        Checking.check_status_code(response, 200)

    @allure.title('GET bad_request.')
    def test_get_with_bad_request(self):
        response = API.get_bad_request()
        Checking.check_status_code(response, 404)

    @allure.title('GET probe.')
    def test_get_probe(self):
        response = API.get_probe()
        Checking.check_status_code(response, 200)

    @allure.title('GET qstatus.')
    def test_get_qstatus(self):
        response = API.get_qstatus()
        Checking.check_status_code(response, 200)
