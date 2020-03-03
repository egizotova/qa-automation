import pytest


@pytest.fixture()
def list_data_fixture():
    """
    fixture для создания тестовых данных для list
    список обьявляется в квадратных скобках!
    :return:
    """
    my_list = [1, 2, 3]
    return my_list


@pytest.fixture(params=[1, 2, 3, 4, 5])
def fixture_with_params(request):
    return request.param


@pytest.fixture(params=[{"name": "123"}, {"name": "321"}, {"name": "213"}, {"name": "21773"}])
def fixture_dict_with_params(request):
    return request.param


@pytest.fixture(params=[(1, 2, 30, 4, 5), (1, 2, 3, 4, 30), (30, 2, 3, 4, 5)])
def fixture_set_with_params(request):
    return request.param


@pytest.fixture(params=["qwerty", "rfvtgb", "zaqxsw"])
def fixture_string_with_params(request):
    return request.param


@pytest.fixture(params=[16, 14, 12, 1, 5])
def age_fixture(request):
    return request.param


@pytest.fixture()
def set_data_fixture():
    """
    fixture для создания тестовых данных для set
    :return:
    """
    my_set = {10, 20, 30, 40, 50}
    return my_set


@pytest.fixture()
def dict_data_fixture():
    """
    fixture для создания тестовых данных для dictionary
    :return:
    """
    my_dictionary = {
        'name': 'Ivan',
        'fname': 'Ivanov',
        'age': 18
    }
    return my_dictionary


@pytest.fixture()
def string_data_fixture():
    """
    создание новых данных для String
    :return:
    """
    my_string = 'string'
    return my_string
