from pprint import pprint

import allure

from tests_ui.base_page import BasePage
from tests_ui.login_page_locators import Locators


class LoginPage(BasePage):
    locators = Locators()

    @allure.step('get_all_ids')
    def get_all_ids(self):
        web_ids = self.elements_are_present(self.locators.IDS)
        list_ids = [i.get_attribute('id') for i in web_ids]
        with allure.step(f'First list is: {list_ids}'):
            pass
        second_list = []
        [second_list.append(ids) for ids in list_ids if ids not in second_list]
        with allure.step(f'If id not in first list second_list.append. Second list is: {second_list}'):
            pass
        pprint(list_ids)
        pprint(second_list)
        assert second_list == list_ids, "ID's are repeated."

    @allure.step('Check buttons.')
    def check_buttons(self):
        with allure.step('Check LOGIN button is clickable.'):
            assert self.element_is_present_and_clickable(
                self.locators.LOGIN_BUTTON), 'Login button is not present or clickable.'
        with allure.step('Check REGISTER button is clickable.'):
            assert self.element_is_present_and_clickable(
                self.locators.REGISTER_BUTTON), 'Register button is not present or clickable.'
        with allure.step('Check SIGN IN button is clickable.'):
            assert self.element_is_present_and_clickable(
                self.locators.INPUT_LOGIN_BUTTON), 'Sign in button is not present or clickable.'
        with allure.step('Click Register button.'):
            self.element_is_present_and_clickable(self.locators.REGISTER_BUTTON).click()
        with allure.step('Check Register(input) button is clickable.'):
            assert self.element_is_present_and_clickable(
                self.locators.INPUT_REGISTER_BUTTON), 'Register(input) button is not present or clickable.'
