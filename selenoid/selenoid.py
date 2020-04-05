import time


def test_selenoid(remote):
    wd = remote
    wd.get("https://otus.ru")
    time.sleep(5)
