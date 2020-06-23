import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from opencart.locators import AdminPage
from opencart.locators import ProductPage
import allure


def test_add_prod(parametrize_browser):
    """
    :param parametrize_browser:
    :return:
    """

    driver = parametrize_browser
    driver.get(driver.current_url + "/admin/")
    allure.step("открыть сайт админ")
    username = driver.find_element_by_id(AdminPage.user_name)
    username.clear()
    username.click()
    allure.step("ввести имя")
    username.send_keys("user")
    password = driver.find_element_by_id(AdminPage.password)
    password.clear()
    password.click()
    password.send_keys("bitnami1")
    allure.step("ввести пароль")
    login_button = driver.find_element_by_css_selector(AdminPage.login)
    login_button.click()
    allure.step("логинимся")
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
    page_model = driver.find_element_by_css_selector(ProductPage.model_aria)
    page_model.click()
    model = driver.find_element_by_id(ProductPage.model_input)
    model.click()
    model.send_keys("test")
    save = driver.find_element_by_css_selector(ProductPage.save)
    save.click()
    driver.find_elements_by_css_selector(ProductPage.success)

def test_edit_prod(parametrize_browser):
    driver = parametrize_browser
    driver.get(driver.current_url + "/admin/")
    username = driver.find_element_by_id(AdminPage.user_name)
    username.clear()
    username.click()
    username.send_keys("user")
    password = driver.find_element_by_id(AdminPage.password)
    password.clear()
    password.click()
    password.send_keys("bitnami1")
    login_button = driver.find_element_by_css_selector(AdminPage.login)
    login_button.click()
    catal = driver.find_element_by_id(AdminPage.catalog)
    catal.click()
    product = driver.find_element_by_css_selector(AdminPage.product_menu)
    product.click()
    edit_but = driver.find_element_by_css_selector(ProductPage.edit)
    edit_but.click()
    descript = driver.find_element_by_css_selector(ProductPage.description)
    descript.click()
    descript.send_keys("test")
    save = driver.find_element_by_css_selector(ProductPage.save)
    save.click()
    driver.find_elements_by_css_selector(ProductPage.success)

def test_del_prod(parametrize_browser):
    driver = parametrize_browser
    driver.get(driver.current_url + "/admin/")
    username = driver.find_element_by_id(AdminPage.user_name)
    username.clear()
    username.click()
    username.send_keys("user")
    password = driver.find_element_by_id(AdminPage.password)
    password.clear()
    password.click()
    password.send_keys("bitnami1")
    login_button = driver.find_element_by_css_selector(AdminPage.login)
    login_button.click()
    catal = driver.find_element_by_id(AdminPage.catalog)
    catal.click()
    product = driver.find_element_by_css_selector(AdminPage.product_menu)
    product.click()
    select = driver.find_element_by_css_selector(ProductPage.chekbox_select)
    select.click()
    delit = driver.find_element_by_css_selector(ProductPage.delit)
    delit.click()
    alert_obj = driver.switch_to.alert
    alert_obj.accept()
    driver.find_elements_by_css_selector(ProductPage.success)



