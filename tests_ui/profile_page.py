import time

import allure
from selenium.webdriver.common.by import By

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
                ...
                # pprint(status_dict)
        return status_dict

    @allure.step('Click "Databases" button.')
    def click_button_databases(self):
        return self.element_is_present_and_clickable(self.locators.DATABASE_BUTTON).click()

    @allure.step('Click "Static site" button.')
    def click_static_site_button(self):
        return self.element_is_present_and_clickable(self.locators.STATIC_BUTTON).click()

    @allure.step('Check webpages block is visible.')
    def check_webpages_block_is_visible(self):
        return self.check_element_is_visible(self.locators.WEBPAGES_BLOCK)

    @allure.step('Check titles of static table .')
    def check_titles_of_static_table(self):
        titles_list = [title.text for title in self.elements_are_visible(self.locators.TITLES_OF_STATIC_TABLE)]
        return titles_list

    @allure.step('Click "Docker containers" button.')
    def click_button_docker_containers(self):
        return self.element_is_present_and_clickable(self.locators.BUTTON_DOCKER_CONTAINER).click()

    @allure.step('click_buttons_create_new_db')
    def click_buttons_create_new_db(self):
        with allure.step('Click "Create new DB" button.'):
            self.element_is_present_and_clickable(self.locators.CREATE_DATABASE_BUTTON).click()

    @allure.step('click_buttons_create')
    def click_buttons_create(self):
        with allure.step('Click "Create" button.'):
            self.element_is_clickable(self.locators.CREATE_NEW_DATABASE_BUTTON).click()
            # print(f'Click {self.locators.CREATE_NEW_DATABASE_BUTTON}')

    @allure.step('Select region "CIS".')
    def select_db_region_cis(self):
        self.element_is_present_and_clickable(self.locators.SELECT_DB_REGION).click()
        self.element_is_present_and_clickable(self.locators.DB_REGION_CIS).click()

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
        list_databases = self.elements_are_present(self.locators.LIST_DATABASES)
        list_db = [list_databases[i].text for i in range(len(list_databases))]
        if len(list_db) != 0:
            button = self.element_is_visible((By.XPATH, f'//tbody[@id="tbody_dbs"] /tr[1]/td[10] /button'))
            button.click()
            server_msg = self.element_is_visible(self.locators.MSG_FROM_SERVER).text
            with allure.step(f'Check server answer is: {server_msg}'):
                assert server_msg == 'server is set for deleting', 'Wrong answer from server or need manual deleting!!!'
            with allure.step(f'Clicked button: {button.text} on the first database in the list.'):
                time.sleep(20)
        else:
            msg = 'No database for deleting.'
            with allure.step(f'{msg}'):
                return msg

    @allure.step('check_clipboard')
    def check_clipboard(self, table_xpath, token: str):
        databases_list = self.elements_are_present((By.XPATH, f'{table_xpath}//tr'))
        list_db = [databases_list[i].text for i in range(len(databases_list))]
        if len(list_db) != 0:
            button = self.element_is_visible((By.XPATH, f'{table_xpath} //tr[1]/td[3] /button'))
            button.click()
            table_line = self.element_is_visible((By.XPATH, f'{table_xpath} //tr[1]')).text
            with allure.step(f'Clicked button {button.text} in database:{table_line}, for copy uuid.'):
                pass

            result = API.post_db_list(token)
            full_uuid = list(result.json()['data'])[0]
            short_uuid = self.element_is_visible((By.XPATH, f'{table_xpath} //tr[1]/td[2]')).text
            assert self.element_is_visible(self.locators.MSG_COPYPASTE)
            msg = self.element_is_visible(self.locators.MSG_COPYPASTE).text
            # print(msg)
            with allure.step(f'Check message after UUID copy. MSG: {msg}'):
                pass
            with allure.step(f'Checked that {short_uuid} is included into {full_uuid}'):
                pass
            assert msg == 'copied to clipboard', 'Message is not present.'
        else:
            assert False, 'No database in the table.'

    @allure.step('check_clipboard_jdbc')
    def check_clipboard_jdbc(self, token: str):
        databases_list = self.elements_are_present(self.locators.LIST_DATABASES)
        list_db = [databases_list[i].text for i in range(len(databases_list))]
        if len(list_db) != 0:
            button = self.element_is_visible((By.XPATH, '//tbody[@id="tbody_dbs"] /tr[1]/td[7] /button'))
            button.click()
            table_line = self.element_is_visible((By.XPATH, '//tbody[@id="tbody_dbs"] /tr[1]')).text
            with allure.step(f'Clicked button {button.text} in database:{table_line}, for copy uuid.'):
                pass
            result = API.post_db_list(token)
            uuid = list(result.json()['data'])[0]
            # print('UUID: ', uuid)
            jdbc = result.json()['data'][f'{uuid}'][3]
            # print('JDBC', jdbc)
            assert self.element_is_visible(self.locators.MSG_COPYPASTE)
            msg = self.element_is_visible(self.locators.MSG_COPYPASTE).text
            # print(msg)
            with allure.step(f'Check message after JDBC copy. MSG: {msg}'):
                pass
            assert msg == 'copied to clipboard', 'Message is not present.'
        else:
            assert False, 'No database in the table.'

    @allure.step('compare_database_status')
    def compare_database_status(self):
        self.click_button_status()
        amount_databases = self.get_status_data()['db qty used']
        self.click_button_databases()
        self.click_buttons_create_new_db()
        self.select_db_region_cis()
        self.click_buttons_create()
        msg = self.element_is_visible(self.locators.MSG_FROM_SERVER).text
        # print(msg)
        with allure.step(f'Check the message after clicking the create database button. MSG: {msg}'):
            pass
        assert msg == 'Order for the new DB accepted', 'Message is not present.'
        self.click_button_status()
        amount_after_create = self.get_status_data()['db qty used']
        assert int(amount_databases) + 1 == int(amount_after_create)

    @allure.step('create_docker_container')
    def create_docker_container(self):
        with allure.step('Click button "Docker Containers".'):
            self.element_is_present_and_clickable(self.locators.BUTTON_DOCKER_CONTAINER).click()
        before = self.elements_are_visible((By.XPATH, '//table[@id="table_containers"]/tbody/tr'))
        list_before = [i.text for i in before]
        with allure.step(f'Check containers list before creation: {list_before}'):
            pass
        with allure.step('Click button "Create new Docker Container".'):
            self.element_is_present_and_clickable(self.locators.BUTTON_CREATE_DOCKER_CONTAINER).click()
        with allure.step('Select region "CIS".'):
            self.element_is_present_and_clickable(self.locators.SELECT_DOCKER_REGION).click()
            self.element_is_visible(self.locators.DOCKER_REGION_CIS).click()
        with allure.step('Click button "Create".'):
            self.element_is_present_and_clickable(self.locators.BUTTON_CREATE).click()
        with allure.step('Click button "Docker Containers".'):
            self.element_is_present_and_clickable(self.locators.BUTTON_DOCKER_CONTAINER).click()
        server_msg = self.element_is_visible(self.locators.MSG_FROM_SERVER).text
        with allure.step(f'Check message from server: "{server_msg}"'):
            assert server_msg == 'Order for the new Container accepted', 'Error creating container!!!'
        self.element_is_present_and_clickable(self.locators.BUTTON_DOCKER_CONTAINER).click()
        self.element_is_visible((By.XPATH, f'//table[@id="table_containers"]/tbody/tr[{len(list_before) + 1}]'))
        after = self.elements_are_visible((By.XPATH, f'//table[@id="table_containers"]/tbody/tr'))
        list_after = [i.text for i in after]
        with allure.step(f'Check containers list after creation: {list_after}'):
            pass
        assert len(list_before) + 1 == len(list_after)

    @allure.step('get_containers_list')
    def get_containers_list(self):
        containers_data = self.elements_are_visible((By.XPATH, '//table[@id="table_containers"]/tbody/tr'))
        containers_list = [i.text for i in containers_data]
        with allure.step(f'Check containers list before creation: {containers_list}'):
            ...
            # pprint(containers_list)
        return containers_list

    @allure.step('delete_first_container')
    def delete_first_container(self):
        amount_containers = self.get_containers_list()
        if len(amount_containers) != 0:
            self.element_is_present_and_clickable((By.XPATH,
                                                   '//tbody[@id="tbody_containers"] /tr[1]/td[10] /button')).click()
            server_msg = self.element_is_visible(self.locators.MSG_FROM_SERVER).text
            assert server_msg == 'container is set for deleting'
        else:
            assert False, 'No containers in the table.'
