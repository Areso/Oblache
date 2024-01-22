import json
import random
from string import ascii_letters

import allure
import pytest

from utils.checking import Checking
# from utils.config_my_sql import DataMySql
from utils.request import API
from .conftest import TestData


@allure.epic('GET REQUESTS')
@allure.suite('REQUESTS GET')
class TestGET:
    @allure.sub_suite('GET')
    @allure.title('test tos')
    def test_tos(self):
        result_get = API.get_tos()
        Checking.check_status_code(result_get, 200)

    @allure.sub_suite('GET')
    @allure.title('List dbtypes')
    def test_list_dbtypes(self):
        result_get = API.get_list_dbtypes()
        Checking.check_status_code(result_get, 200)

    @allure.sub_suite('GET')
    @allure.title('List dbversions')
    def test_list_dbversions(self):
        result_get = API.get_list_dbversions()
        Checking.check_status_code(result_get, 200)

    @allure.sub_suite('GET')
    @allure.title('List envs')
    def test_list_envs(self):
        result_get = API.get_list_envs()
        Checking.check_status_code(result_get, 200)

    @allure.sub_suite('GET')
    @allure.title('List regions')
    def test_list_regions(self):
        result_get = API.get_list_regions()
        Checking.check_status_code(result_get, 200)


@allure.epic('POST REQUESTS')
@allure.suite('REQUESTS POST')
class TestPOST:
    @pytest.mark.xfail()
    @allure.sub_suite('POST')
    @allure.title('Post registration')
    def test_post_registration(self):
        print('\n\nMethod POST: registration')
        result_post = API.post_registration()
        status_code = result_post.status_code
        Checking.check_status_code(status_code, 200)

    @allure.sub_suite('POST')
    @allure.title('Post login')
    def test_post_login(self):
        print('\n\nMethod POST: login')
        result_post = API.post_login(TestData.body)
        status_code, sid = result_post
        Checking.check_status_code(status_code, 200)

    # @allure.sub_suite('POST')
    # @allure.title('Post db create')
    # def test_post_db_create(self):
    #     print('\n\nMethod POST: db_create')
    #     result_post_db_list = API.post_db_create(TestData.sid)
    #     # print(result_post_db_list)
    #     print(result_post_db_list.json()["db_uuid"])
    #     Checking.check_status_code(result_post_db_list, 201)

    @allure.sub_suite('POST')
    @allure.title('Post db list')
    def test_post_db_list(self):
        print('\n\nMethod POST: db_list')
        result_post_db_list = API.post_db_list(TestData.sid)
        Checking.check_status_code(result_post_db_list, 200)

    @allure.sub_suite('DELETE')
    @allure.title('delete db')
    @pytest.mark.xfail()
    def test_delete_db(self):
        print('\n\nMethod DELETE: delete_db')
        list_db = API.post_db_list(TestData.sid)
        json_list_db = json.loads(list_db.text)
        first_db_uuid = list(json_list_db['content'].keys())[0]
        '''
        list(json_list_db['content'].keys())[0] #"065a5b36-e472-7398-8000-7ce3e7219464"
        '''
        # print(first_db_uuid)
        result_post_db_list = API.delete_db(first_db_uuid, TestData.sid)
        Checking.check_status_code(result_post_db_list, 200)


@allure.epic('Connection DB')
@allure.suite('Test Connection DB')
class TestConnectionDB:
    @allure.sub_suite('Complex')
    def test_complex(self):
        API.check_full_cycle(TestData.sid)


class TestLoadDB:
    def test_create_table(self):
        """
        :return:
        """
        query = '''
        CREATE TABLE IF NOT EXISTS accounts(
        userid INT PRIMARY KEY AUTO_INCREMENT,
        name varchar(128),
        date_of_birth datetime NULL,
        text varchar(4096),
        email varchar(128) NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
        '''
        db = TestData.connection("065a5c25-6bd0-7a6e-8000-a9830730182e")
        cursor = db.cursor()
        cursor.execute(query)
        db.commit()

    def test_load_table2(self):
        """
        :return:
        """
        db = TestData.connection("065a5c25-6bd0-7a6e-8000-a9830730182e")
        letters = ascii_letters
        cursor = db.cursor()
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
        cursor.execute('''select * from accounts''')
        res = cursor.fetchall()
        print(res)
