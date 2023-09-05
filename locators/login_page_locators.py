# locators/login_page_locators.py
from selenium.webdriver.common.by import By


class LoginPageLocators:
    emailID_locator = (By.NAME, "emailid")
    password_locator = (By.ID, "password")
    submit_email_button_locator = (By.XPATH, "//input[@name='btnLogin']")
    bank_banner = (By.XPATH, "/html/body/div[2]/h2")
    account_table = (By.XPATH, "/html/body/table")

