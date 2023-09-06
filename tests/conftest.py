import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.login_page import LoginPage


@pytest.fixture(scope="class")
def driver(request):
    selected_browser = request.config.getoption("--browser", default="chrome")

    if selected_browser == "chrome":
        chromedriver_path = "C:\\Users\\Dr.Tautology\\PycharmProjects\\SeleniumTestFrameworkPOM\\drivers" \
                           "\\chromedriver_116.exe"
        service = ChromeService(executable_path=chromedriver_path)
        options = ChromeOptions()
        driver_instance = webdriver.Chrome(service=service, options=options)
    elif selected_browser == "firefox":
        geckodriver_path = "C:\\Users\\Dr.Tautology\\PycharmProjects\\SeleniumTestFrameworkPOM\\drivers" \
                          "\\geckodriver.exe"
        service = FirefoxService(executable_path=geckodriver_path)
        options = FirefoxOptions()
        driver_instance = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError("Invalid browser choice")

    yield driver_instance
    driver_instance.quit()


@pytest.fixture(scope="class")
def login_page(driver):
    driver.get("https://demo.guru99.com")
    return LoginPage(driver)


def pytest_addoption(parser):
    parser.addoption("--browser", choices=["chrome", "firefox"], default="chrome", help="Specify the browser to use for tests (e.g., --browser chrome)")
