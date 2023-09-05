# tests/test_login.py
import pytest
import datetime as dt
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_page_locators import LoginPageLocators


@pytest.mark.usefixtures("driver", "login_page")
class TestLogin:
    def test_successful_login(self, login_page):

        login_page.wait.until(EC.presence_of_element_located((By.XPATH, LoginPageLocators.submit_email_button_locator[1])))
        login_page.enter_email("abc@gmail.com")
        print("Login information entered.")

        print("Current URL:", login_page.driver.current_url)
        print("Page Title:", login_page.driver.title)

        print("Before clicking the submit button")
        login_page.click_submit_button()
        print("After clicking the submit button")

        login_page.wait.until(EC.invisibility_of_element(LoginPageLocators.submit_email_button_locator))
        print("Wait for element complete.")
        print("taking a screenshot.")
        login_page.driver.save_screenshot(f"screenshot{dt.datetime.now().strftime('%m_%d_%y %I_%M_%S')}.png")
        login_page.wait.until(EC.presence_of_element_located((By.XPATH, LoginPageLocators.account_table[1])))

        print("Submit button pressed.")
        print("Waiting for webdriver.")

        # Add assertions to verify the login was successful
        try:
            print("Waiting for element to be present.")
            element = login_page.wait.until(EC.presence_of_element_located((By.XPATH, *LoginPageLocators.bank_banner)))
            # banner_text = login_page.driver.find_element(LoginPageLocators.bank_banner).get_attribute("text").lower()
            # assert banner_text == "guru99 bank"
        except Exception as e:
            print(f"Assertion Failed:{e}")
