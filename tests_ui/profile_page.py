import time
from pprint import pprint

import allure
from selenium.webdriver.common.by import By

from tests_ui.base_page import BasePage
from tests_ui.login_page_locators import Locators


class ProfilePage(BasePage):
    locators = Locators()

    @allure.step('Click button Status.')
    def click_button_status(self):
        return self.element_is_present_and_clickable(self.locators.STATUS_BUTTON).click()

    @allure.step('get_status_data')
    def get_status_data(self):
        amount_string = len(self.elements_are_visible(self.locators.LEN_TABLE_STRINGS))
        status_dict = {}
        for i in range(1, amount_string):
            status_dict[self.element_is_present(
                (By.XPATH, f'//tbody[@id="tbody_status"]/tr[{i}]/td[1]')).text] = self.element_is_present(
                (By.XPATH, f'//tbody[@id="tbody_status"]/tr[{i}]/td[2]')).text
        with allure.step('Get status data.'):
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
            # time.sleep(1)
        with allure.step('Click "Create new DB" button.'):
            self.element_is_clickable(self.locators.CREATE_NEW_DATABASE_BUTTON).click()
            print(f'Click {self.locators.CREATE_NEW_DATABASE_BUTTON}')
            time.sleep(1)

    @allure.step('get_amount_databases')
    def get_amount_databases(self):
        self.click_button_databases()
        amount = len(self.elements_are_present((By.XPATH, '//tbody[@id="tbody_dbs"]/tr')))
        return amount