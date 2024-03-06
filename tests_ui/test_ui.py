from pprint import pprint

import allure
import requests

from tests_ui.data import TestDataLinks
from tests_ui.login_page import LoginPage
from tests_ui.main_page import MainPage
from tests_ui.profile_page import ProfilePage


@allure.epic('UI Tests')
class TestUI:
    @allure.suite('Test Main Page.')
    class TestMainPage:
        @allure.title('test_ids_is_not_repeated_on_main_page')
        def test_ids_is_not_repeated_on_main_page(self, driver):
            page = LoginPage(driver, TestDataLinks.main_page)
            page.open()
            page.get_all_ids()

        @allure.title('test_links')
        def test_links(self, driver):
            page = MainPage(driver, TestDataLinks.main_page)
            page.open()
            page.check_links()

    @allure.suite('Test Login Page.')
    class TestLoginPage:
        @allure.title('test_ids_is_not_repeated_on_login_page')
        def test_ids_is_not_repeated_on_login_page(self, driver):
            page = LoginPage(driver, TestDataLinks.register_page)
            page.open()
            page.get_all_ids()

        @allure.title('test_ids_is_not_repeated_on_login_page')
        def test_buttons_are_clickable(self, driver):
            page = LoginPage(driver, TestDataLinks.register_page)
            page.open()
            page.check_buttons()

        @allure.title('test_login')
        def test_login(self, driver):
            page = LoginPage(driver, TestDataLinks.register_page)
            page.open()
            page.login_user()

    @allure.suite('Test Profile Page.')
    class TestProfilePage:
        @allure.title('test_ids_is_not_repeated_on_login_page')
        def test_ids_is_not_repeated_on_profile_page(self, driver):
            page = LoginPage(driver, TestDataLinks.profile_page)
            page.open()
            page.get_all_ids()

        @allure.title('test_create_database')
        def test_create_database(self, driver):
            page = LoginPage(driver, TestDataLinks.register_page)
            page.open()
            page.login_user()
            page = ProfilePage(driver)
            page.click_button_status()
            amount_databases = page.get_status_data()['db qty used']

            page.click_button_databases()
            page.click_buttons_create_new_db()

            page.click_button_status()
            amount_after_create = page.get_status_data()['db qty used']
            assert int(amount_databases) + 1 == int(amount_after_create)

    def test_source_v1(self):
        source = requests.get('https://oblache.areso.pro/tos.html')
        data = []
        data_vac = {}
        for i in source.text.split('\n'):
            if 'locObj' in i.split('=')[0]:
                data_vac.setdefault(i.split('=')[0].strip(), i.split('=')[1])
            if 'locObj' in i.split('=')[0] and i.split('=')[0] not in data:
                data.append(i.split('=')[0])

        pprint(data_vac)
        print(len(data_vac.keys()))
        print(len(data))
        print(data_vac['locObj.en_us.div_limits'])
