# pages/login_page.py
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username_locator = (By.ID, "username")
    password_locator = (By.ID, "password")
    login_button_locator = (By.ID, "login-button")

    def enter_username(self, username):
        self.driver.find_element(*self.username_locator).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_locator).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button_locator).click()
