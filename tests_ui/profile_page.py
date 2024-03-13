import time
from pprint import pprint

import allure
from selenium.webdriver.common.by import By

from connection_data import ConnectionData
from tests_api.utils.request import API
from tests_ui.base_page import BasePage
from tests_ui.login_page_locators import Locators


@allure.suite('Profile Page')
class ProfilePage(BasePage):
    locators = Locators()

    @allure.step('Click button Status.')
    def click_button_status(self):
        time.sleep(1)
        return self.element_is_present_and_clickable(self.locators.STATUS_BUTTON).click()

    @allure.step('get_status_data')
    def get_status_data(self):
        amount_string = len(self.elements_are_visible(self.locators.LEN_TABLE_STRINGS))
        status_dict = {}
        for i in range(1, amount_string):
            status_dict[self.element_is_present(
                (By.XPATH, f'//tbody[@id="tbody_status"]/tr[{i}]/td[1]')).text] = self.element_is_present(
                (By.XPATH, f'//tbody[@id="tbody_status"]/tr[{i}]/td[2]')).text
        with allure.step(f'Get status data.'):
            pass
            with allure.step(f'Status data is: {status_dict}'):
                pprint(status_dict)
        return status_dict

    @allure.step('Click "Databases" button.')
    def click_button_databases(self):
        return self.element_is_present_and_clickable(self.locators.DATABASE_BUTTON).click()

    @allure.step('click_buttons_create_new_db')
    def click_buttons_create_new_db(self):
        with allure.step('Click "Create new DB" button.'):
            self.element_is_present_and_clickable(self.locators.CREATE_DATABASE_BUTTON).click()
        with allure.step('Click "Create new DB" button.'):
            self.element_is_clickable(self.locators.CREATE_NEW_DATABASE_BUTTON).click()
            print(f'Click {self.locators.CREATE_NEW_DATABASE_BUTTON}')
            time.sleep(1.5)

    @allure.step('get_amount_databases')
    def get_amount_databases(self):
        self.click_button_databases()
        amount = len(self.elements_are_present((By.XPATH, '//tbody[@id="tbody_dbs"]/tr')))
        return amount

    @allure.step('delete_database')
    def delete_database(self):
        self.click_button_databases()
        self.click_buttons_create_new_db()
        self.click_button_databases()
        time.sleep(1)
        x = self.elements_are_present(self.locators.LIST_DATABASES)
        list_db = [x[i].text for i in range(len(x))]
        print(list_db)
        if len(list_db) != 0:
            button = self.element_is_visible((By.XPATH, '//tbody[@id="tbody_dbs"] /tr[1]/td[10] /button'))
            button.click()
            with allure.step(f'Click button: {button.text}'):
                time.sleep(20)
        else:
            msg = 'No database for deleting.'
            with allure.step(f'{msg}'):
                return msg

    @allure.step('check_clipboard')
    def check_clipboard(self):
        self.click_button_databases()
        databases_list = self.elements_are_present(self.locators.LIST_DATABASES)
        list_db = [databases_list[i].text for i in range(len(databases_list))]
        if len(list_db) != 0:
            button = self.element_is_visible((By.XPATH, '//tbody[@id="tbody_dbs"] /tr[1]/td[3] /button'))
            button.click()
            table_line = self.element_is_visible((By.XPATH, '//tbody[@id="tbody_dbs"] /tr[1]')).text
            with allure.step(f'Click button {button.text} in database:{table_line}, for copy uuid.'):
                pass

            result = API.post_db_list(ConnectionData.token)
            full_uuid = list(result.json()['data'])[0]
            short_uuid = self.element_is_visible((By.XPATH, '//tbody[@id="tbody_dbs"] /tr[1]/td[2]')).text
            assert self.element_is_visible(self.locators.MSG_FROM_SERVER)
            with allure.step('Check msg after copy uuid is present'):
                msg = self.element_is_visible(self.locators.MSG_FROM_SERVER).text
                print(msg)
            with allure.step(f'Checked that {short_uuid} is included into {full_uuid}'):
                pass
            assert short_uuid in msg
        else:
            assert False, 'No database in the table.'

    @allure.step('check_clipboard_jdbc')
    def check_clipboard_jdbc(self):
        self.click_button_databases()
        databases_list = self.elements_are_present(self.locators.LIST_DATABASES)
        list_db = [databases_list[i].text for i in range(len(databases_list))]
        if len(list_db) != 0:
            button = self.element_is_visible((By.XPATH, '//tbody[@id="tbody_dbs"] /tr[1]/td[7] /button'))
            button.click()
            table_line = self.element_is_visible((By.XPATH, '//tbody[@id="tbody_dbs"] /tr[1]')).text
            with allure.step(f'Click button {button.text} in database:{table_line}, for copy uuid.'):
                pass

            result = API.post_db_list(ConnectionData.token)
            uuid = list(result.json()['data'])[0]
            print('UUID: ', uuid)
            jdbc = result.json()['data'][f'{uuid}'][3]
            print('JDBC', jdbc)
            assert self.element_is_visible(self.locators.MSG_FROM_SERVER)
            with allure.step('Check msg after copy JDBC is present'):
                msg = self.element_is_visible(self.locators.MSG_FROM_SERVER).text
                print(msg)
            assert msg in jdbc
        else:
            assert False, 'No database in the table.'

    @allure.step('compare_database_status')
    def compare_database_status(self):
        self.click_button_status()
        amount_databases = self.get_status_data()['db qty used']
        self.click_button_databases()
        self.click_buttons_create_new_db()
        self.click_button_status()
        amount_after_create = self.get_status_data()['db qty used']
        assert int(amount_databases) + 1 == int(amount_after_create)
