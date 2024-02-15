import allure

from tests_ui.data import TestDataLinks
from tests_ui.login_page import LoginPage


@allure.epic('UI Tests')
class TestLoginPage:

    def test_fo(self):
        print('*' * 50, '*' * 50)
        assert 1 == 1

    @allure.title('test_ids_is_not_repeated')
    def test_ids_is_not_repeated(self, driver):
        page = LoginPage(driver, TestDataLinks.profile_page)
        page.open()
        first_list, second_list = page.get_all_ids()
        assert first_list == second_list
