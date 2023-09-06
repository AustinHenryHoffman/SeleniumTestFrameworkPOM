from locators.login_page_locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # Initialize WebDriverWait here

    def enter_email(self, email):
        self.driver.find_element(*LoginPageLocators.emailID_locator).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*LoginPageLocators.password_locator).send_keys(password)

    def click_submit_button(self):
        self.driver.find_element(*LoginPageLocators.submit_email_button_locator).click()
