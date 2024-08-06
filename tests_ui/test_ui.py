import allure

from tests_ui.links import TestDataLinks
from tests_ui.login_page import LoginPage
from tests_ui.main_page import MainPage
from tests_ui.profile_page import ProfilePage


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

    @allure.title('test_main_button')
    def test_main_button(self, driver):
        page = MainPage(driver, TestDataLinks.main_page)
        page.open()
        page.check_main_button_is_visible()


@allure.suite('Test Login Page.')
class TestLoginPage:
    @allure.title('test_ids_is_not_repeated_on_login_page')
    def test_ids_is_not_repeated_on_login_page(self, driver):
        page = LoginPage(driver, TestDataLinks.register_page)
        page.open()
        page.get_all_ids()

    @allure.title('test_buttons_are_clickable')
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
    token = None

    @allure.title('Get token.')
    def test_get_token(self, get_token):
        TestProfilePage.token = get_token[0]
        assert TestProfilePage.token is not None, 'Token is None.'

    @allure.title('test_ids_is_not_repeated_on_profile_page')
    def test_ids_is_not_repeated_on_profile_page(self, driver):
        page = LoginPage(driver, TestDataLinks.profile_page)
        page.open()
        page.get_all_ids()

    @allure.title('test_create_database')
    def test_create_database(self, driver, authorization_user):
        page = ProfilePage(driver, authorization_user)
        page.compare_database_status()

    @allure.title('test_delete_database')
    def test_delete_database(self, driver, authorization_user):
        page = ProfilePage(driver, authorization_user)
        page.click_button_status()
        amount_databases = page.get_status_data()['db qty used']
        msg = page.delete_database()
        page.click_button_status()
        amount_after_create = page.get_status_data()['db qty used']
        assert amount_databases == amount_after_create or msg == 'No database for deleting.'

    @allure.title('test_clipboard')
    def test_clipboard_uuid_db(self, driver, authorization_user):
        page = ProfilePage(driver, authorization_user)
        page.click_button_databases()
        page.check_clipboard(
            table_xpath='//tbody[@id="tbody_dbs"]',
            token=TestProfilePage.token)

    @allure.title('test_clipboard_jdbc')
    def test_clipboard_jdbc(self, driver, authorization_user):
        page = ProfilePage(driver, authorization_user)
        page.click_button_databases()
        page.check_clipboard_jdbc(token=TestProfilePage.token)

    @allure.title('test_clipboard_uuid_docker')
    def test_clipboard_uuid_docker(self, driver, authorization_user):
        page = ProfilePage(driver, authorization_user)
        page.click_button_docker_containers()
        page.check_clipboard(
            table_xpath='//table[@id="table_containers"]',
            token=TestProfilePage.token)

    @allure.title('test_create_docker_container')
    def test_create_docker_container(self, driver, authorization_user):
        page = ProfilePage(driver, authorization_user)
        page.create_docker_container()

    # def test_check_port_lens_positive(self, driver, authorization_user):
    #     page = ProfilePage(driver)
    #     page.check_port_lens_positive()

    def test_delete_container(self, driver, authorization_user):
        page = ProfilePage(driver, authorization_user)
        page.click_button_docker_containers()
        page.get_containers_list()
        page.delete_first_container()
