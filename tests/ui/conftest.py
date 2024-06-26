from datetime import datetime

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use for tests: chrome or firefox")


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        service = Service("/usr/local/bin/chromedriver")
        driver = webdriver.Chrome(service=service, options=chrome_options)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function", autouse=True)
def browser(driver):
    driver.get("https://testnet.mynearwallet.com/")
    yield driver


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "login: mark test to run with a logged in driver"
    )


def pytest_runtest_setup(item):
    if 'login' in item.keywords and 'browser' not in item.fixturenames:
        pytest.skip('test requires the \'browser\' fixture')


@pytest.fixture(autouse=True)
def capture_screenshot_on_failure(request, browser):
    yield
    if request.node.rep_call.failed:
        allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        item.rep_call = rep
