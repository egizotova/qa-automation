import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from opencart.locators import ProductPage



def test_add_to_bask(parametrize_browser):
    """
    кликаем по элементу с ожиданием 5сек до появления
    добавляем  в карзину, проверяем что в корзине верное значение
    :param parametrize_browser:
    :return:
    """
    browser = parametrize_browser
    WebDriverWait(browser, 3)  # seconds
    try:
        element = WebDriverWait(browser, 5).until(
           EC.presence_of_element_located((By.ID, ProductPage.add_to_card)))
        element.click()
    finally:
        time.sleep(3)
    basket = browser.find_element_by_id(ProductPage.basket).text
    assert basket == "1 item(s) - $122.00"



def test_quantity(parametrize_browser):
    """
    находим поле, очищаем, вводим значение, добавляем в карзину
    :param parametrize_browser:
    :return:
    """
    browser = parametrize_browser
    WebDriverWait(browser, 3)  # seconds
    in_put_q = browser.find_element_by_id(ProductPage.quantity)
    in_put_q.clear()
    in_put_q.click()
    in_put_q.send_keys(3)
    add_to_bask = browser.find_element_by_id(ProductPage.add_to_card)
    add_to_bask.send_keys(Keys.ENTER)
    time.sleep(3)
    basket = browser.find_element_by_id(ProductPage.basket).text
    assert basket == "3 item(s) - $366.00"
    time.sleep(3)
