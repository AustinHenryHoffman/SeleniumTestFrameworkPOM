# tests/test_login.py
import unittest
import datetime as dt
from pathlib import Path
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

        self.chromedriver_path = "C:\\Users\\Dr.Tautology\\PycharmProjects\\SeleniumTestFrameworkPOM\\drivers" \
                            "\\chromedriver_116.exe "
        service = ChromeService(executable_path=self.chromedriver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://demo.guru99.com")
        self.login_page = LoginPage(self.driver)
        self.wait = WebDriverWait(self.driver, 20)
        self.report = Path("../reports")

    def test_successful_login(self):

        self.wait.until(EC.presence_of_element_located((By.XPATH, LoginPageLocators.submit_email_button_locator[1])))
        self.login_page.enter_email("abc@gmail.com")
        print("Login information entered.")

        print("Current URL:", self.driver.current_url)
        print("Page Title:", self.driver.title)

        print("Before clicking the submit button")
        self.login_page.click_submit_button()
        print("After clicking the submit button")

        self.wait.until(EC.invisibility_of_element(LoginPageLocators.submit_email_button_locator))
        print("Wait for element complete.")
        print("taking a screenshot.")
        self.driver.save_screenshot(f"screenshot{dt.datetime.now().strftime('%m_%d_%y %I_%M_%S')}.png")
        self.wait.until(EC.presence_of_element_located((By.XPATH, LoginPageLocators.account_table[1])))

        print("Submit button pressed.")
        print("Waiting for webdriver.")

        # Add assertions to verify the login was successful
        try:
            print("Waiting for element to be present.")
            element = self.wait.until(EC.presence_of_element_located((By.XPATH, *LoginPageLocators.bank_banner)))
            # banner_text = self.driver.find_element(LoginPageLocators.bank_banner).get_attribute("text").lower()
            # assert banner_text == "guru99 bank"
        except Exception as e:
            print(f"Assertion Failed:{e}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
