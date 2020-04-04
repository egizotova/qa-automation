import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from opencart.locators import AdminPage
from opencart.locators import ProductPage


def test_add_prod(parametrize_browser):
    """
    :param parametrize_browser:
    :return:
    """

    driver = parametrize_browser
    driver.get(parametrize_browser.current_url + "/admin/")
    username = driver.find_element_by_id(AdminPage.user_name)
    username.clear()
    username.click()
    username.send_keys("admin")
    password = driver.find_element_by_id(AdminPage.password)
    password.clear()
    password.click()
    password.send_keys("admin")
    login_button = driver.find_element_by_css_selector(AdminPage.login)
    login_button.click()
    catal = driver.find_element_by_id(AdminPage.catalog)
    catal.click()
    product = driver.find_element_by_css_selector(AdminPage.product_menu)
    product.click()
    button_add = driver.find_element_by_css_selector(AdminPage.add_product)
    button_add.click()
    name_product = driver.find_element_by_id(ProductPage.name_product)
    name_product.send_keys("test")
    descript = driver.find_element_by_css_selector(ProductPage.description)
    descript.click()
    descript.send_keys("test")
    tag = driver.find_element_by_id(ProductPage.tag_input)
    tag.click()
    tag.send_keys("test")
    page_model = driver.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'ProductPage.model_aria')))
    page_model.click()
    model = driver.find_element_by_css_selector(ProductPage.model_input)
    model.click()
    model.send_keys("test")
    save = driver.find_element_by_css_selector(ProductPage.save)
    save.click()
    time.sleep(9)
