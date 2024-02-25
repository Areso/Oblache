import allure

from tests_ui.data import TestDataLinks
from tests_ui.login_page import LoginPage


@allure.epic('UI Tests')
class TestLoginPage:

    def test_fo(self):
        print('*' * 50, '*' * 50)
        assert 1 == 1

    @allure.title('test_ids_is_not_repeated_on_main_page')
    def test_ids_is_not_repeated_on_main_page(self, driver):
        page = LoginPage(driver, TestDataLinks.profile_page)
        page.open()
        page.get_all_ids()

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
