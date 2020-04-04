import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="http://localhost", help="choose your browser")


@pytest.fixture
def browser(request):
    browser_param = request.config.getoption("--browser")
    if browser_param == "chrome":
        driver = webdriver.Chrome()
    elif browser_param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.implicitly_wait(10)
    request.addfinalizer(driver.close)
    url = request.config.getoption("--url")
    driver.get(url)

    return driver


@pytest.fixture(params=["chrome", "firefox"])
def parametrize_browser(request):
    browser_param = request.param
    if browser_param == "chrome":
        driver = webdriver.Chrome()
    elif browser_param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.implicitly_wait(20)
    request.addfinalizer(driver.quit)
    url = request.config.getoption("--url")
    driver.get(url)

    return driver


def sum_a_b(a: int, b: int):
    # c = a + b
    return a + b


def print_sum():
    a = 5
    b = 10
    # c = sum_a_b(a, b)
    print(str(sum_a_b(a, b)))


if __name__ == '__main__':
    print_sum()

