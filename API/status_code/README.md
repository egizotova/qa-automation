пример запуска pytest API/status_code/test_status.py --url=https://ya.ru/404 --code=404 -v

проверяем, что assert str(http_response.status_code) == code
по указанному урлу приходит статус код и сравниваем его с тем который передали в параметре
