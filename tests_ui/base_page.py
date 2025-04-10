import allure
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:

    def __init__(self, driver, link=None):
        self.driver: WebDriver = driver
        self.link = link
        self.timeout = 5

    def open(self):
        with allure.step(f'Open page: {self.link}'):
            self.driver.get(self.link)

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url: ' + get_url)
        return get_url

    def element_is_present_and_clickable(self, locator):
        return (Wait(self.driver, self.timeout).until(
            ec.visibility_of_element_located(locator), message=f"Can't find element by locator {locator}") and
                self.element_is_clickable(locator))

    def element_is_visible(self, locator):
        self.go_to_element(self.element_is_present(locator))
        return Wait(self.driver, self.timeout).until(
            ec.visibility_of_element_located(locator), message=f"Can't find element by locator {locator}")

    def elements_are_visible(self, locator):
        return Wait(self.driver, self.timeout).until(
            ec.visibility_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}")

    def element_is_not_visible(self, locator):
        return Wait(self.driver, self.timeout).until(
            ec.invisibility_of_element_located(locator), message=f"The element located by {locator} is invisible")

    def element_is_present(self, locator):
        return Wait(self.driver, self.timeout).until(
            ec.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    def elements_are_present(self, locator):
        return Wait(self.driver, self.timeout).until(
            ec.presence_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}")

    def element_is_clickable(self, locator):
        return Wait(self.driver, self.timeout).until(
            ec.element_to_be_clickable(locator), message=f"Can't find element by locator {locator}")

    def go_to_element(self, element):
        return self.driver.execute_script("arguments[0].scrollIntoView({ block: 'center'});", element)

    def check_expected_link(self, url):
        with allure.step(f'Check url is present: {url}'):
            return Wait(self.driver, self.timeout).until(
                ec.url_to_be(url), message=f"Can't find element by locator {url}")

    def wait_changed_url(self, url):
        with allure.step(f'Wait until url: {url} will be changed.'):
            Wait(self.driver, self.timeout).until(
                ec.url_changes(url), message=f"Url: {url} has not been changed!!!")
            self.get_current_url()

    def check_element_is_visible(self, locator, timeout=15):
        try:
            Wait(self.driver, timeout).until(ec.visibility_of_element_located(locator),
                                             message=f"Can't find element by locator {locator}")
            return True
        except TimeoutException:
            return False
