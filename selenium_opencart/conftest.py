import pytest
from selenium import webdriver


def pytest_addoption(parser):
    """
    parser.addoption
    :param parser:
    :return:
    """
    parser.addoption("--browser", action="store", default="chrome", help="browser: chrome or firefox")


@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")

    if 'chrome' == browser:
        driver = webdriver.Chrome('/Users/kate/tools/chromedriver')
    elif 'firefox' == browser:
        driver = webdriver.Firefox('/Users/kate/tools/geckodriver')

    yield driver
    driver.quit()
    return driver
