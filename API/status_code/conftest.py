import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     choices=["firefox", "safari"])
    parser.addoption("--code", action="store", default="400",
                     choices=["200", "500", "400", "404"])
    parser.addoption("--url", action="store", default="http//ya.ru")


@pytest.fixture()
def params_fixture(request):
    result_dict = {
        'url': request.config.getoption("--url"),
        'code': request.config.getoption("--code")
    }
    return  result_dict
