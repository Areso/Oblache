from selenium.webdriver.common.by import By


class Locators:
    IDS = (By.XPATH, "//*[@id]")

    # Login page
    LOGIN_BUTTON = (By.XPATH, '//button[@id="btn_opentab_login"]')
    REGISTER_BUTTON = (By.XPATH, '//button[@id="btn_opentab_register"]')
    INPUT_LOGIN_BUTTON = (By.XPATH, '//input[@id="inp_regform_login_submit"]')
    INPUT_REGISTER_BUTTON = (By.XPATH, '//input[@id="inp_regform_register_submit"]')
    SIGN_IN_BUTTON = (By.XPATH, '//input[@id="inp_regform_login_submit"]')

    INPUT_LOGIN = (By.XPATH, '//input[@id="inp_loginform_email"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@id="inp_loginform_password"]')

