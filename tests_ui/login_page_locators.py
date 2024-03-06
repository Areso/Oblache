from selenium.webdriver.common.by import By


class Locators:
    IDS = (By.XPATH, "//*[@id]")

    # Main page
    LINKS = (By.XPATH, '//a[@href]')
    SCRIPT = (By.XPATH, '')

    # Login page
    LOGIN_BUTTON = (By.XPATH, '//button[@id="btn_opentab_login"]')
    REGISTER_BUTTON = (By.XPATH, '//button[@id="btn_opentab_register"]')
    INPUT_LOGIN_BUTTON = (By.XPATH, '//input[@id="inp_regform_login_submit"]')
    INPUT_REGISTER_BUTTON = (By.XPATH, '//input[@id="inp_regform_register_submit"]')
    SIGN_IN_BUTTON = (By.XPATH, '//input[@id="inp_regform_login_submit"]')

    INPUT_LOGIN = (By.XPATH, '//input[@id="inp_loginform_email"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@id="inp_loginform_password"]')

    # Profile page
    DATABASE_BUTTON = (By.XPATH, '//button[@id = "menu_button_databases"]')
    STATUS_BUTTON = (By.XPATH, '//button[@id="menu_button_status"]')

    CREATE_DATABASE_BUTTON = (By.XPATH, '//button[@id="btn_new_db"]')
    CREATE_NEW_DATABASE_BUTTON = (By.XPATH, '//button[@id="btn_create_db"]')

    LIST_DATABASES = (By.XPATH, '//tbody[@id="tbody_dbs"]/tr')
    LEN_TABLE_STRINGS = (By.XPATH, '//tbody[@id="tbody_status"]/tr')
