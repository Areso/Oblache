import allure
import requests

from tests_ui.login_page_locators import Locators
from tests_ui.base_page import BasePage


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

    @allure.step('check_main_button_is_visible')
    def check_main_button_is_visible(self):
        with allure.step('Click Terms of Use.'):
            self.element_is_present_and_clickable(self.locators.TOS_BUTTON).click()
        with allure.step('Check Main button  is visible.'):
            pass
        assert self.element_is_present_and_clickable(self.locators.MAIN_BUTTON)
