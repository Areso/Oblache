from selenium.webdriver.common.by import By


class Locators:
    IDS = (By.XPATH, "//*[@id]")

    # Main page
    LINKS = (By.XPATH, '//a[@href]')
    SCRIPT = (By.XPATH, '')
    TOS_BUTTON = (By.XPATH, '//a[@id="ahref_tos"]')
    MAIN_BUTTON = (By.XPATH, '//a[@id="ahref_index"]')

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
    STATIC_BUTTON = (By.XPATH, '//button[@id="menu_button_webpages"]')
    WEBPAGES_BLOCK = (By.XPATH, '//div[@id="webpages"]')
    TITLES_OF_STATIC_TABLE = (By.XPATH, '//table[@id="table_webpages"]//tr/td')

    CREATE_DATABASE_BUTTON = (By.XPATH, '//button[@id="btn_new_db"]')
    CREATE_NEW_DATABASE_BUTTON = (By.XPATH, '//button[@id="btn_create_db"]')
    SELECT_DB_REGION = (By.XPATH, '//select[@id="selectDBRegion"]')
    DB_REGION_CIS = (By.XPATH, '//select[@id="selectDBRegion"] /option[@value="3"]')
    SELECT_DOCKER_REGION = (By.XPATH, '//select[@id="selectDockerRegion"]')
    DOCKER_REGION_CIS = (By.XPATH, '//select[@id="selectDockerRegion"] /option[@value="3"]')

    LIST_DATABASES = (By.XPATH, f'//tbody[@id="tbody_dbs"]/tr')
    LEN_TABLE_STRINGS = (By.XPATH, '//tbody[@id="tbody_status"]/tr')

    MSG_COPYPASTE = (By.XPATH, '//div[@id="msg_copypaste"]')
    MSG_FROM_SERVER = (By.XPATH, '//div[@id="msg_from_server"]')

    # Docker container page
    BUTTON_DOCKER_CONTAINER = (By.XPATH, '//button[@id="menu_button_containers"]')
    BUTTON_CREATE_DOCKER_CONTAINER = (By.XPATH, '//button[@id="btn_new_docker_container"]')
    BUTTON_CREATE = (By.XPATH, '//button[@id="btn_create_docker"]')
    LIST_DOCKER_CONTAINERS = (By.XPATH, '//table[@id="table_containers"]/tbody/tr')
