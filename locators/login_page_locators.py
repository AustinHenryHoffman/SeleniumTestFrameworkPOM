# locators/login_page_locators.py
from selenium.webdriver.common.by import By


class LoginPageLocators:
    email_locator = (By.name, "emailid")
    # password_locator = (By.ID, "password")
    # login_button_locator = (By.ID, "login-button")
    submit_email_button_locator = (By.name, "btnLogin")
