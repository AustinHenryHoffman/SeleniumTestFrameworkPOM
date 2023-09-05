# tests/test_login.py
import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from locators.login_page_locators import LoginPageLocators


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://example.com")
        self.login_page = LoginPage(self.driver)

    def test_successful_login(self):
        self.login_page.enter_username("your_username")
        self.login_page.enter_password("your_password")
        self.login_page.click_login_button()

        # Add assertions to verify the login was successful

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
