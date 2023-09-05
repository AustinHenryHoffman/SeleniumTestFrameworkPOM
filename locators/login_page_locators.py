# locators/login_page_locators.py
from selenium.webdriver.common.by import By

class LoginPageLocators:
    username_locator = (By.ID, "username")
    password_locator = (By.ID, "password")
    login_button_locator = (By.ID, "login-button")
