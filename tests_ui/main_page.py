import allure
import requests

from tests_ui.base_page import BasePage
from tests_ui.login_page_locators import Locators


@allure.suite('Main Page')
class MainPage(BasePage):
    locators = Locators()

    @allure.step('check_links')
    def check_links(self):
        links = self.elements_are_present(self.locators.LINKS)
        list_links = [link.get_attribute('href') for link in links]
        for link in list_links:
            with allure.step(f'{link} status code is: {requests.get(link).status_code}'):
                assert requests.get(link).status_code != 404, f'Link {link} is broken!'
