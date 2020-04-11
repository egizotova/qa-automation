import allure

from opencart.locators import AdminPage
from opencart.locators import ProductPage


@allure.title("Добавление продукта")
@allure.description("Тест на добавление продукта")
def test_add_prod(parametrize_browser_for_allure):
    driver = parametrize_browser_for_allure

    open_admin_login_page(driver)
    enter_username(driver)
    enter_password(driver)
    click_login_button(driver)
    catallog(driver)
    product_click(driver)


@allure.story("Логин админа")
@allure.step("открыть страницу логина админа")
def open_admin_login_page(driver):
    driver.get(driver.current_url + "/admin/")


@allure.story("Логин админа")
@allure.step("ввести логин админа")
def enter_username(driver):
    username = driver.find_element_by_id(AdminPage.user_name)
    username.clear()
    username.click()
    username.send_keys("user")


@allure.story("Логин админа")
@allure.step("ввести пароль админа")
def enter_password(driver):
    password = driver.find_element_by_id(AdminPage.password)
    password.clear()
    password.click()
    password.send_keys("bitnami1")


@allure.story("Логин админа")
@allure.step("нажать кнопку логина")
def click_login_button(driver):
    login_button = driver.find_element_by_css_selector(AdminPage.login)
    login_button.click()

@allure.step("преейти в каталог")
def catallog(driver):
    catal = driver.find_element_by_id(AdminPage.catalog)
    catal.click()

@allure.step("перейти в продукт")
def product_click(driver):
    product = driver.find_element_by_css_selector(AdminPage.product_menu)
    product.click()

@allure.step("добавить продукт")
def add_product(driver):
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

@allure.step("проверить успех  добавления")
def success(driver):
    driver.find_elements_by_css_selector(ProductPage.success)

