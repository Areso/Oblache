import random
import time
from datetime import datetime
from pprint import pprint
from string import ascii_letters

import allure
import pytest
import requests

from conftest_api import TestData
from .data import data
from .utils.checking import Checking
from .utils.request import API


@allure.epic('Connection DB')
@allure.suite('Test Connection DB')
class TestConnectionDB:
    @allure.title('Complex')
    def test_complex(self):
        API.check_full_cycle(TestData.token)


@allure.epic('Performance DB')
@allure.suite('Test Performance DB')
class TestCapacity:
    @allure.title('test_capacity_db')
    def test_capacity_db(self):
        start_mb_value = API.get_profile(TestData.token).json()['data']["content"][4][1]
        print('Db size mb:', start_mb_value)
        result_db_create = API.post_db_create(TestData.token)
        print('Status db is :', result_db_create.json())
        db_uuid = result_db_create.json()["db_uuid"]
        print("db_uuid", db_uuid)
        time.sleep(20)
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
            db.commit()
        cursor.execute('''select * from accounts''')
        # res = cursor.fetchall()
        # print(res)
        time.sleep(40)
        finish_mb_value = API.get_profile(TestData.token).json()['data']["content"][4][1]
        req = requests.post('http://cisdb1.areso.pro:9090/list', json={"token": "SuperSecret"})
        pprint(req.text)
        print('Db size mb after insert:', finish_mb_value)
        create_new_db = API.post_db_create(TestData.token)
        print(create_new_db.status_code)
        assert int(finish_mb_value) > 0, 'Value db_size should be more than 0.'
        result_post_db_delete = API.delete_db(f"{db_uuid}", TestData.token)
        Checking.check_status_code(result_post_db_delete, 200)


@allure.epic('GET REQUESTS')
@allure.suite('GET')
class TestGET:
    @allure.title('Test tos.')
    def test_tos(self):
        result_get = API.get_tos()
        Checking.check_status_code(result_get, 200)

    @allure.title('Get profile information.')
    def test_get_profile(self):
        result_get = API.get_profile(TestData.token)
        Checking.check_status_code(result_get, 200)

    @allure.title('List db_types.')
    def test_get_list_db_types(self):
        result_get = API.get_list_db_types()
        Checking.check_status_code(result_get, 200)

    @allure.title('List db_versions.')
    def test_get_list_db_versions(self):
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

    @allure.title('Bad request.')
    def test_get_with_bad_request(self):
        result_get = API.get_bad_request()
        Checking.check_status_code(result_get, 404)

    @allure.title('Get profile status.')
    def test_get_status(self):
        result_get = API.get_status()
        Checking.check_status_code(result_get, 200)


@allure.epic('POST REQUESTS')
@allure.suite('POST')
class TestPOST:
    @pytest.mark.xfail()
    @allure.title('Post registration')
    def test_post_registration(self):
        result_post = API.post_registration()
        status_code = result_post
        Checking.check_status_code(status_code, 201)

    @allure.title('Post registration mail any countries')
    def test_post_registration_with_variety_mail(self):
        result_post = API.post_registration_variety_email(random.choice(['gmail', 'mail', 'yandex']),
                                                          random.choice(['com', 'ru', 'by']))
        status_code = result_post
        Checking.check_status_code(status_code, 201)
        Checking.check_json_search_word_in_value(result_post, 'content', 'msg[1]: registered successfully')

    @allure.title('Post registration mail bg')
    def test_post_registration_for_bulgaria(self):
        result_post = API.post_registration_variety_email(random.choice(['gmail', 'mail', 'yandex']), 'bg')
        status_code = result_post
        Checking.check_status_code(status_code, 201)
        Checking.check_json_search_word_in_value(result_post, 'content', 'msg[1]: registered successfully')

    @allure.title('Post registration email is taken')
    def test_post_registration_email_is_taken(self):
        result_post = API.post_registration()
        status_code = result_post
        Checking.check_status_code(status_code, 400)
        Checking.check_json_search_word_in_value(result_post, 'content',
                                                 'msg[3]: registration failed, this email is taken')

    @allure.title('Post login')
    def test_post_login(self):
        result_post = API.post_login(TestData.body)
        Checking.check_status_code(result_post, 200)

    @allure.title('test_post_is_logged')
    def test_post_is_logged(self):
        result_post = API.post_is_logged(TestData.token)
        print(result_post.json())
        Checking.check_status_code(result_post, 200)

    @allure.title('test_post_is_logged_with_wrong_token')
    def test_post_is_logged_with_wrong_token(self):
        result_post = API.post_is_logged_with_wrong_token()
        Checking.check_status_code(result_post, 401)

    @allure.title('Post db_create')
    def test_post_db_create(self):
        result_post_db_list = API.post_db_create(TestData.token)
        Checking.check_status_code(result_post_db_list, 201)

    @allure.title('Post db_create with wrong db_type.')
    def test_post_db_create_with_wrong_values_dbtype(self):
        result_post_db_list = API.post_db_create_wrong_value_db_type(TestData.token)
        Checking.check_status_code(result_post_db_list, 400)
        Checking.check_json_search_word_in_value(result_post_db_list, "content",
                                                 "error: DB type isn't found or isn't available for order")

    @allure.title('Post db_create with wrong db_version.')
    def test_post_db_create_with_wrong_values_db_version(self):
        result_post_db_list = API.post_db_create_wrong_value_db_version(TestData.token)
        Checking.check_status_code(result_post_db_list, 400)
        Checking.check_json_search_word_in_value(result_post_db_list, "content",
                                                 "error: DB version isn't found or isn't available for order")

    @allure.title('Post db_create with wrong env.')
    def test_post_db_create_with_wrong_values_env(self):
        result_post_db_list = API.post_db_create_wrong_value_env(TestData.token)
        Checking.check_status_code(result_post_db_list, 400)
        Checking.check_json_search_word_in_value(result_post_db_list, "content",
                                                 "error: DB environment isn't found or isn't available for order")

    @allure.title('Post db_create with wrong region.')
    def test_post_db_create_with_wrong_values_region(self):
        result_post_db_list = API.post_db_create_wrong_value_region(TestData.token)
        Checking.check_status_code(result_post_db_list, 400)
        Checking.check_json_search_word_in_value(result_post_db_list, "content",
                                                 "error: region isn't found or isn't available for order")

    @allure.title('Post db_list')
    def test_post_db_list(self):
        result_post_db_list = API.post_db_list(TestData.token)
        print(result_post_db_list.json())
        Checking.check_status_code(result_post_db_list, 200)

    @allure.title('Post db list with filter')
    @pytest.mark.xfail(reason='There are databases that need to be deleted manually.')
    def test_post_db_list_with_filter(self):
        list_db = API.post_db_list(TestData.token)
        json_list_db = list_db.json()
        try:
            first_db_uuid = list(json_list_db['data'])[-1]
            result_post_db_list = API.delete_db(first_db_uuid, TestData.token)
            print(result_post_db_list.json())
            Checking.check_status_code(result_post_db_list, 200)
        except IndexError as ex:
            print(ex)
            assert str(ex) == 'list index out of range', 'Db list is empty.'

    @allure.title('Post change password')
    def test_post_change_password(self):
        new_password = TestData.new_password
        result_post_change_password = API.post_change_password(TestData.token, TestData.old_password, new_password)
        Checking.check_status_code(result_post_change_password, 200)
        Checking.check_json_search_word_in_value(result_post_change_password, "content",
                                                 "msg[31]: password successfully updated")
        result_post_change_password = API.post_change_password(TestData.token, new_password, TestData.old_password)
        Checking.check_status_code(result_post_change_password, 200)
        Checking.check_json_search_word_in_value(result_post_change_password, "content",
                                                 "msg[31]: password successfully updated")

    @allure.title('delete_db')
    @pytest.mark.xfail(reason='When using this method during a test run, the database may be in deleting status.')
    def test_delete_db(self):
        list_db = API.post_db_list(TestData.token)
        json_list_db = list_db.json()
        try:
            first_db_uuid = list(json_list_db['data'])[0]
            print(first_db_uuid)
            result_post_db_delete = API.delete_db(first_db_uuid, TestData.token)
            print(result_post_db_delete.json())
            Checking.check_status_code(result_post_db_delete, 200)
        except IndexError as ex:
            print(ex)
            assert str(ex) == 'list index out of range', 'Db list is empty.'
        '''
        list(json_list_db['content'].keys())[0] #"065a5b36-e472-7398-8000-7ce3e7219464"
        '''
    @allure.title('test_delete_all_created_db')
    def test_delete_all_created_db(self):
        start = datetime.now().time().strftime('%H:%M')
        print('Start', start)
        while True:
            finish = datetime.now().time().strftime('%H:%M')
            print('Finish', finish)
            list_db = API.post_db_list(TestData.token)
            json_list_db = list_db.json()['data']
            if json_list_db == {}:
                break
            else:
                first_db_uuid = list(json_list_db)[0]
                result_post_db_delete = API.delete_db(first_db_uuid, TestData.token)
                print(result_post_db_delete.json())
                time.sleep(5)
                if start != finish:
                    break
        list_db = API.post_db_list(TestData.token)
        json_list_db = list_db.json()['data']
        assert json_list_db == {}




