import time

from tests_ui.base_page import BasePage
from tests_ui.data import TestDataLinks


class TestLoginPage:

    def test_fo(self):
        print('*' * 50, '*' * 50)
        assert 1 == 1

    def test_foss(self, driver):
        page = BasePage(driver, TestDataLinks.register_page)
        page.open()
        time.sleep(5)
