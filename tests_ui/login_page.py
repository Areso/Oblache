from pprint import pprint

import allure

from conftest_api import TestData
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
        for ids in list_ids:
            if ids not in second_list:
                second_list.append(ids)
            else:
                with allure.step(f'{ids} is repeated.'):
                    assert ids is False, f'{ids} is repeated!'
        # [second_list.append(ids) for ids in list_ids if ids not in second_list]
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

    @allure.step('login_user')
    def login_user(self):
        with allure.step('Enter email.'):
            self.element_is_present(self.locators.INPUT_LOGIN).send_keys(TestData.email)
        with allure.step('Enter password.'):
            self.element_is_present(self.locators.INPUT_PASSWORD).send_keys(TestData.old_password)
        with allure.step('Click button "Login"'):
            self.element_is_present_and_clickable(self.locators.SIGN_IN_BUTTON).click()
        assert self.check_expected_link('https://oblache.areso.pro/profile.html'
                                        ), 'https://oblache.areso.pro/profile.html is not open.'
