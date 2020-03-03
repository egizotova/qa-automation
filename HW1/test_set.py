def test_set1(set_data_fixture):
    """
    тестирования длинны list
    :param set_data_fixture:
    :return:
    """
    set1 = set_data_fixture
    assert len(set1) == 5


def test_set_count(fixture_set_with_params):
    """
    число 30 принадлежит заданному множеству
    :param fixture_set_with_params:
    :return:
    """
    assert 30 in fixture_set_with_params


def test_set_insert(set_data_fixture):
    """
    вставили значение, проверили длину
    :param set_data_fixture:
    :return:
    """
    set_insert = set_data_fixture
    set_insert.add(100)
    assert len(set_insert) == 6


def test_set_remove(set_data_fixture):
    """
    удаляем эоемент, проверяем на количество элеменов
    :param set_data_fixture:
    :return:
    """
    set_remove = set_data_fixture
    set_remove.remove(30)
    assert len(set_remove) == 4
