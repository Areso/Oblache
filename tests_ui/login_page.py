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
        return second_list, list_ids
