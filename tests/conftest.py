import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pathlib import Path
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import datetime as dt
import logging


@pytest.fixture(scope="function")
def driver(request):
    selected_browser = request.config.getoption("--browser", default="chrome")

    if selected_browser == "chrome":
        options = ChromeOptions()
        driver_instance = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif selected_browser == "firefox":
        options = FirefoxOptions()
        driver_instance = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    else:
        raise ValueError("Invalid browser choice")

    yield driver_instance
    driver_instance.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", choices=["chrome", "firefox"], default="chrome", help="Specify the browser to use for tests (e.g., --browser chrome)")


def configure_logger(test_name, log_file):
    logger = logging.getLogger(test_name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger


@pytest.fixture(scope="function")
def reports_path(request):
    # Get the name of the test function
    test_name = request.node.name

    # Generate a timestamp
    timestamp = dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create the subdirectory name by combining the test name and timestamp
    subdirectory_name = f"{test_name}_{timestamp}"

    # Define the path to the reports directory
    reports_dir = Path("../reports", subdirectory_name)  # Modify the path as needed
    reports_dir.mkdir(parents=True, exist_ok=True)

    yield reports_dir

