# locators/tricentis_login_page_locators.py
from selenium.webdriver.common.by import By


class LoginPageLocators:
    email_locator = (By.XPATH, "//input[@class='email']")
    password_locator = (By.XPATH, "//input[@class='password']")
    login_button_locator = (By.XPATH, "//a[@class='ico-login'][ text()='Log in']")
    submit_button_locator = (By.XPATH, "//div[@class='buttons']/input[@type='submit']")
    row_topper = (By.XPATH, "//div[@class='row topper']")

