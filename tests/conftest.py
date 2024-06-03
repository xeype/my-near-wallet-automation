import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use for tests: chrome or firefox")


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(options=chrome_options)
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
