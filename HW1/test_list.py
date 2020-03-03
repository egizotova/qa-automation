import pytest


def test_list(list_data_fixture):
    """
    тестирования длинны list
    :param list_data_fixture:
    :return:
    """
    assert len(list_data_fixture) == 3


def test_list_count(list_data_fixture):
    """
    сколько раз число 3
    :param list_data_fixture:
    :return:
    """
    assert list_data_fixture.count(3) == 1


def test_list_insert(list_data_fixture):
    """
    вставили значение, проверили длину
    :param list_data_fixture:
    :return:
    """
    test_insert_list = list_data_fixture
    test_insert_list.insert(0, 100)
    assert len(test_insert_list) == 4


def test_list_sum(list_data_fixture):
    """
    сумма сзначений
    :param list_data_fixture:
    :return:
    """
    sum = list_data_fixture[1] + list_data_fixture[2]
    assert sum == 5


def test_list_new_list(list_data_fixture):
    """
    добавляем новый список, обьединяем списки
    :param list_data_fixture:
    :return:
    """
    data_list = list_data_fixture
    list_two = [10, 20, 30]
    data_list.extend(list_two)
    assert len(data_list) == 6


@pytest.mark.parametrize("test_input", [4, 5, 6])
def test_list_param1(fixture_with_params, test_input):
    print("fixture: " + str(fixture_with_params) + " param: " + str(test_input))

    assert fixture_with_params != test_input


result = 0


def test_list_param1(fixture_with_params, list_data_fixture):
    global result
    result = result + list_data_fixture[1] + fixture_with_params
    print("fixture value: " + str(fixture_with_params) + " list fixture: " + str(
        list_data_fixture[1]) + " result: " + str(result))

    assert result < 100


def test_age_is_low_then_18(age_fixture):
    assert age_fixture < 18
