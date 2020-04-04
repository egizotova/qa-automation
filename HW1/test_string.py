def test_str1(fixture_string_with_params):
    """
    тестирования длинны  cстроки
    :param fixture_string_with_params:
    :return:
    """
    assert len(fixture_string_with_params) == 6


def test_str2(string_data_fixture):
    """
    сложение строк
    :param string_data_fixture:
    :return:
    """
    test_str = 'number 111'
    s = string_data_fixture + test_str
    print(s)
    assert len(s) > 6


def test_str3(string_data_fixture):
    """
    состоит ли из буков
    :param string_data_fixture:
    :return:
    """
    assert string_data_fixture.isalpha


def test_str4(string_data_fixture):
    """
    состоит ли из буков
    :param string_data_fixture:
    :return:
    """
    assert string_data_fixture.isdigit

x=2
def f():
    return x+3

x=5
print(f(), x)
