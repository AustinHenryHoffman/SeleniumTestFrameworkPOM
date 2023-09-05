# pages/login_page.py
from locators.login_page_locators import LoginPageLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(*LoginPageLocators.emailID_locator).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*LoginPageLocators.password_locator).send_keys(password)

    def click_submit_button(self):
        self.driver.find_element(*LoginPageLocators.submit_email_button_locator).click()
