# Реализуйте в отдельном модуле (файле) тестовую функцию которая будет принимать 2 параетра:
# url - должно быть значение по умолчанию https://ya.ru (будем надеяться яндекс выдержит!)
# status_code - значение по уполчанию 200
# Параметры должны быть реализованы через pytest.addoption.
# Можно положить фиктуру и тестовую фунцию в один файл.
# Основная задача чтобы ваш тест проверял что по переданному урлу статус ответа тот который передали, т.е. по адресу https://ya.ru/sfhfhfhfhfhfhfhfh должен быть валидным ответ 404

# пример запуска pytest test_module.py --url=https://mail.ru --status_code=200

import requests


def test_status(params_fixture):
    code = params_fixture['code']
    url = params_fixture['url']

    http_response = requests.get(url)

    assert str(http_response.status_code) == code
