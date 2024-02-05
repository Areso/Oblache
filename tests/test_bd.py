import json
import random
import time
from string import ascii_letters

import allure
import pytest

from utils.checking import Checking
from utils.request import API
from .conftest import TestData


@allure.epic('GET REQUESTS')
@allure.suite('GET')
class TestGET:
    @allure.title('Test tos.')
    def test_tos(self):
        result_get = API.get_tos()
        Checking.check_status_code(result_get, 200)

    @allure.title('Get profile information.')
    def test_get_profile(self):
        result_get = API.get_profile()
        Checking.check_status_code(result_get, 200)

    @allure.title('List dbtypes.')
    def test_get_list_dbtypes(self):
        result_get = API.get_list_dbtypes()
        Checking.check_status_code(result_get, 200)

    @allure.title('List dbversions.')
    def test_get_list_dbversions(self):
        result_get = API.get_list_dbversions()
        Checking.check_status_code(result_get, 200)

    @allure.title('List envs.')
    def test_get_list_envs(self):
        result_get = API.get_list_envs()
        Checking.check_status_code(result_get, 200)

    @allure.title('List regions.')
    def test_get_list_regions(self):
        result_get = API.get_list_regions()
        Checking.check_status_code(result_get, 200)

    @allure.title('List regions.')
    def test_get_with_bad_request(self):
        result_get = API.get_bad_request()
        Checking.check_status_code(result_get, 404)

    @allure.title('Get profile information.')
    def test_get_status(self):
        result_get = API.get_status()
        Checking.check_status_code(result_get, 200)


@allure.epic('POST REQUESTS')
@allure.suite('POST')
class TestPOST:
    @pytest.mark.xfail()
    @allure.title('Post registration')
    def test_post_registration(self):
        print('\n\nMethod POST: registration')
        result_post = API.post_registration()
        status_code = result_post
        Checking.check_status_code(status_code, 201)

    @allure.title('Post registration mail any counties')
    def test_post_registration_with_variety_mail(self):
        print('\n\nMethod POST: registration')
        result_post = API.post_registration_variety_email(random.choice(['gmail', 'mail', 'yandex']),
                                                          random.choice(['com', 'ru', 'by']))
        status_code = result_post
        Checking.check_status_code(status_code, 201)
        Checking.check_json_search_word_in_value(result_post, 'content', 'msg[1]: registered successfully')

    @allure.title('Post registration mail bg')
    def test_post_registration_for_bulgaria(self):
        print('\n\nMethod POST: registration')
        result_post = API.post_registration_variety_email(random.choice(['gmail', 'mail', 'yandex']), 'bg')
        status_code = result_post
        Checking.check_status_code(status_code, 201)
        Checking.check_json_search_word_in_value(result_post, 'content', 'msg[1]: registered successfully')

    @allure.title('Post registration email is taken')
    def test_post_registration_email_is_taken(self):
        print('\n\nMethod POST: registration')
        result_post = API.post_registration()
        status_code = result_post
        Checking.check_status_code(status_code, 400)
        Checking.check_json_search_word_in_value(result_post, 'content',
                                                 'msg[3]: registration failed, this email is taken')

    @allure.title('Post login')
    def test_post_login(self):
        print('\n\nMethod POST: login')
        result_post = API.post_login(TestData.body)
        status_code, sid = result_post
        Checking.check_status_code(status_code, 200)

    @allure.title('Post db create')
    def test_post_db_create(self):
        print('\n\nMethod POST: db_create')
        result_post_db_list = API.post_db_create(TestData.sid)
        print(result_post_db_list.json()["db_uuid"])
        Checking.check_status_code(result_post_db_list, 201)

    @allure.title('Post db_create with wrong dbtype.')
    def test_post_db_create_with_wrong_values_dbtype(self):
        print('\n\nMethod POST: post_db_create_wrong_value_dbtype')
        result_post_db_list = API.post_db_create_wrong_value_dbtype(TestData.sid)
        print(result_post_db_list.json())
        Checking.check_status_code(result_post_db_list, 400)
        Checking.check_json_search_word_in_value(result_post_db_list, "content",
                                                 "error: DB type isn't found or isn't available for order")

    @allure.title('Post db_create with wrong dbversion.')
    def test_post_db_create_with_wrong_values_dbversion(self):
        print('\n\nMethod POST: post_db_create_wrong_value_dbversione')
        result_post_db_list = API.post_db_create_wrong_value_dbversion(TestData.sid)
        print(result_post_db_list.json())
        Checking.check_status_code(result_post_db_list, 400)
        Checking.check_json_search_word_in_value(result_post_db_list, "content",
                                                 "error: DB version isn't found or isn't available for order")

    @allure.title('Post db_create with wrong env.')
    def test_post_db_create_with_wrong_values_env(self):
        print('\n\nMethod POST: post_db_create_wrong_value_env')
        result_post_db_list = API.post_db_create_wrong_value_env(TestData.sid)
        print(result_post_db_list.json())
        Checking.check_status_code(result_post_db_list, 400)
        Checking.check_json_search_word_in_value(result_post_db_list, "content",
                                                 "error: DB environment isn't found or isn't available for order")

    @allure.title('Post db_create with wrong region.')
    def test_post_db_create_with_wrong_values_region(self):
        print('\n\nMethod POST: post_db_create_wrong_value_region')
        result_post_db_list = API.post_db_create_wrong_value_region(TestData.sid)
        print(result_post_db_list.json())
        Checking.check_status_code(result_post_db_list, 400)
        Checking.check_json_search_word_in_value(result_post_db_list, "content",
                                                 "error: region isn't found or isn't available for order")

    @allure.title('Post db list')
    def test_post_db_list(self):
        print('\n\nMethod POST: db_list')
        result_post_db_list = API.post_db_list(TestData.sid)
        Checking.check_status_code(result_post_db_list, 200)

    @allure.title('Post db list with filter')
    def test_post_db_list_with_filter(self):
        print('\n\nMethod POST: db_list_with_filter')
        list_db = API.post_db_list(TestData.sid)
        json_list_db = json.loads(list_db.text)
        try:
            first_db_uuid = list(json_list_db['content'].keys())[0]
            result_post_db_list = API.post_db_list_with_filter(TestData.sid, first_db_uuid)
            Checking.check_status_code(result_post_db_list, 200)
        except IndexError as ex:
            print(ex)
            assert str(ex) == 'list index out of range', 'Db list is empty.'

    @allure.title('delete db')
    @pytest.mark.xfail()
    def test_delete_db(self):
        print('\n\nMethod DELETE: delete_db')
        list_db = API.post_db_list(TestData.sid)
        json_list_db = json.loads(list_db.text)
        try:
            first_db_uuid = list(json_list_db['content'].keys())[0]
            result_post_db_delete = API.delete_db(first_db_uuid, TestData.sid)
            Checking.check_status_code(result_post_db_delete, 200)
        except IndexError as ex:
            print(ex)
            assert str(ex) == 'list index out of range', 'Db list is empty.'
        '''
        list(json_list_db['content'].keys())[0] #"065a5b36-e472-7398-8000-7ce3e7219464"
        '''


@allure.epic('Connection DB')
@allure.suite('Test Connection DB')
class TestConnectionDB:
    # @allure.sub_suite('Complex')
    # def test_complex(self):
    #     time.sleep(30)
    #     API.check_full_cycle(TestData.sid)

    @allure.title('Complex 2')
    def test_complex2(self):
        API.check_full_cycle2(TestData.sid)


@allure.epic('Performance DB')
@allure.suite('Test Performance DB')
class TestCapacity:
    @allure.title('test_capacity_db')
    def test_capacity_db(self):
        result_db_create = API.post_db_create(TestData.sid)
        print('Status db is :', result_db_create.json())
        db_uuid = result_db_create.json()["db_uuid"]
        print("db_uuid", db_uuid)
        time.sleep(40)
        query = '''
        CREATE TABLE IF NOT EXISTS accounts(
        userid INT PRIMARY KEY AUTO_INCREMENT,
        name varchar(128),
        date_of_birth datetime NULL,
        text varchar(4096),
        email varchar(128) NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
        '''
        db = TestData.connection(f"{db_uuid}")
        cursor = db.cursor()
        cursor.execute(query)
        db.commit()

        db = TestData.connection(f"{db_uuid}")
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
        result_post_db_delete = API.delete_db(f"{db_uuid}", TestData.sid)
        Checking.check_status_code(result_post_db_delete, 200)
