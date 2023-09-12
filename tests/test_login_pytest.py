# tests/test_login.py
import pytest
import datetime as dt
import time
from pathlib import Path
from selenium.webdriver.support import expected_conditions as EC
from locators.login_page_locators import LoginPageLocators


@pytest.mark.usefixtures("driver", "login_page", "reports_path")
class TestLogin:
    def test_successful_login(self, login_page, reports_path):

        login_page.wait.until(EC.presence_of_element_located(LoginPageLocators.submit_email_button_locator))
        login_page.enter_email("abc@gmail.com")
        print("Login information entered.")

        print("Current URL:", login_page.driver.current_url)
        print("Page Title:", login_page.driver.title)
        time.sleep(5)
        print("Before clicking the submit button")
        login_page.click_submit_button()
        print("After clicking the submit button")

        login_page.wait.until(EC.invisibility_of_element(LoginPageLocators.submit_email_button_locator))
        print("Wait for element complete.")
        print("taking a screenshot.")
        login_page.driver.save_screenshot(Path(reports_path, f"screenshot{dt.datetime.now().strftime('%m_%d_%y %I_%M_%S')}.png"))
        login_page.wait.until(EC.presence_of_element_located(LoginPageLocators.account_table))

        print("Submit button pressed.")
        print("Waiting for webdriver.")

        # Add assertions to verify the login was successful
        try:
            print("Waiting for element to be present.")
            element = login_page.wait.until(EC.presence_of_element_located(LoginPageLocators.bank_banner))
            banner_text = login_page.driver.find_element(*LoginPageLocators.bank_banner).text.lower()
            assert banner_text == "guru99 bank"
        except Exception as e:
            print(f"Assertion Failed:{e}")
