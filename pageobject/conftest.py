import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    # driver = webdriver.Chrome('chromedriver')
    # driver = webdriver.Firefox('geckodriver')
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
