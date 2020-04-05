import pytest
from selenium import webdriver


def pytest_addoption(parser):
    """
    parser.addoption
    :param parser:
    :return:
    """
    parser.addoption("--browser", action="store", default="chrome", help="browser: chrome or firefox")
    parser.addoption("--selenoid", action="store", default=True, help="run selenoid or local")
    parser.addoption("--executor", action="store", default="http://localhost", help="url of executor")


@pytest.fixture()
def remote(request):
    browser = request.config.getoption("--browser")
    selenoid = request.config.getoption("--selenoid")
    executor = request.config.getoption("--executor")
    caps = {
        "browserName": browser,
        "enableVideo": True,
        "enableLog": True,
        "version": "56.0"
    }

    if selenoid:
        url = f"{executor}:4444/wd/hub"
        wd = webdriver.Remote(command_executor=url, desired_capabilities=caps)
    else:
        if 'chrome' == browser:
            wd = webdriver.Chrome('chromedriver')
        elif 'firefox' == browser:
            wd = webdriver.Chrome('geckodriver')

    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd
