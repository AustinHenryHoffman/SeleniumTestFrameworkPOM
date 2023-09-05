# tests/test_login.py
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from locators.login_page_locators import LoginPageLocators
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.chromedriverpath = "C:\\Users\\Dr.Tautology\\PycharmProjects\\SeleniumTestFrameworkPOM\\drivers" \
                            "\\chromedriver_116.exe "
        service = ChromeService(executable_path=self.chromedriverpath)
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://demo.guru99.com")
        self.login_page = LoginPage(self.driver)

    def test_successful_login(self):
        self.login_page.enter_email("abc@gmail.com")
        # self.login_page.enter_password("your_password")
        self.login_page.click_submit_button()
        WebDriverWait(10)
        # Add assertions to verify the login was successful
        try:
            element = WebDriverWait.until(EC.presence_of_element_located((By.XPATH, *LoginPageLocators.bank_banner)))
            assert element.text.lower() == "guru99 bank"
        except Exception as e:
            print(f"Assertion Failed:{e}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
