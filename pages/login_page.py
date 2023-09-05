# pages/login_page.py
from selenium.webdriver.common.by import By
from locators.login_page_locators import LoginPageLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    emailID_locator = (By.name, "emailid")
    password_locator = (By.ID, "password")
    submit_button_locator = (By.name, "btnLogin")

    def enter_email(self, email):
        self.driver.find_element(*self.email_locator).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_locator).send_keys(password)

    def click_submit_button(self):
        self.driver.find_element(*self.submit_button_locator).click()
