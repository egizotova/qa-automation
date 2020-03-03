def test_dict1(dict_data_fixture):
    """
    проверяем значение в словаре
    :param dict_data_fixture:
    :return:
    """
    test_dict1 = dict_data_fixture
    assert test_dict1['age'] > 14


def test_dict2(dict_data_fixture):
    """
    проверяем количество значений ==не пустой
    :param dict_data_fixture: 
    :return: 
    """
    test_dict2 = dict_data_fixture
    assert len(test_dict2) > 0


def test_dict3(dict_data_fixture):
    """
    сравнение словарей
    :param dict_data_fixture:
    :return:
    """
    test_dict = dict_data_fixture
    my_dict = {
        'name': 'Иван',
        'fname': 'Иванов',
        'age': 18
    }
    assert test_dict != my_dict


def test_dict4(dict_data_fixture):
    """
    добавление значения
    :param dict_data_fixture:
    :return:
    """
    test_dict4 = dict_data_fixture
    test_dict4.update({
        'sex': 'M',
        'type': 'cons',
        'number': 1567
    })
    print(dict_data_fixture)
    assert len(test_dict4) > 3


def test_dict_from_params(fixture_dict_with_params):
    """
    имя в словаре состоит из цифр
    :param fixture_dict_with_params:
    :return:
    """
    assert str(fixture_dict_with_params['name']).isnumeric()
