import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="http://localhost", help="choose your browser")


@pytest.fixture(params=["chrome"])
def parametrize_browser_for_allure(request):
    browser_param = request.param
    if browser_param == "chrome":
        driver = webdriver.Chrome()
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.implicitly_wait(20)
    request.addfinalizer(driver.quit)
    url = request.config.getoption("--url")
    driver.get(url)

    return driver
