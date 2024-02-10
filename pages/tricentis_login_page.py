from locators.tricentis_login_page_locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
import json


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # Initialize WebDriverWait here
        with open("../config/logins_config.json", 'r') as config_file:
            self.config = json.load(config_file)

    def enter_email(self):
        username = self.config["Tricentis_Demo"]['username']
        self.driver.find_element(*LoginPageLocators.email_locator).send_keys(username)

    def enter_password(self):
        password = self.config["Tricentis_Demo"]['password']
        self.driver.find_element(*LoginPageLocators.password_locator).send_keys(password)

    def click_submit_button(self):
        self.driver.find_element(*LoginPageLocators.submit_button_locator).click()

    def login(self):
        base_url = self.config["Tricentis_Demo"]['url']
        self.driver.get(base_url)
        return LoginPage(self.driver)
