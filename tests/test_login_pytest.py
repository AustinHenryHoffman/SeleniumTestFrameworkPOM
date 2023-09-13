# tests/test_login.py
import pytest
import datetime as dt
import time
from pathlib import Path
from selenium.webdriver.support import expected_conditions as EC
from locators.login_page_locators import LoginPageLocators
from conftest import configure_logger


@pytest.mark.usefixtures("driver", "login_page", "reports_path")
class TestLogin:
    def test_successful_login(self, login_page, reports_path):

        # Set up logging
        # Get the name of the test function
        test_name = self.__class__.__name__
        # Generate a timestamp for log
        timestamp = dt.datetime.now().strftime("%Y_%m_%d_%S")
        # Create the log file name
        log_file = Path(reports_path, f"{test_name}_{timestamp}.log")
        # Configure and create a logger for this test
        logger = configure_logger(test_name, log_file)

        #Starting the Test
        login_page.wait.until(EC.presence_of_element_located(LoginPageLocators.submit_email_button_locator))
        login_page.enter_email("abc@gmail.com")
        logger.info("Login information entered.")

        logger.info(f"Current URL: {login_page.driver.current_url}")
        logger.info(f"Page Title: {login_page.driver.title}")
        time.sleep(5)
        logger.info("Before clicking the submit button")
        login_page.click_submit_button()
        logger.info("After clicking the submit button")

        login_page.wait.until(EC.invisibility_of_element(LoginPageLocators.submit_email_button_locator))
        logger.info("Wait for element complete.")
        logger.info("taking a screenshot.")
        login_page.driver.save_screenshot(Path(reports_path, f"screenshot{dt.datetime.now().strftime('%m_%d_%y %I_%M_%S')}.png"))
        login_page.wait.until(EC.presence_of_element_located(LoginPageLocators.account_table))

        logger.info("Submit button pressed.")
        logger.info("Waiting for webdriver.")

        # Add assertions to verify the login was successful
        try:
            logger.info("Waiting for element to be present.")
            element = login_page.wait.until(EC.presence_of_element_located(LoginPageLocators.bank_banner))
            banner_text = login_page.driver.find_element(*LoginPageLocators.bank_banner).text.lower()
            logger.info(f"Banner Text:{banner_text}")
            assert banner_text == "guru99 bank"
        except Exception as e:
            logger.error(f"Assertion Failed:{e}")
