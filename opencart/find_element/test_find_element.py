from opencart.locators import AdminPage
from opencart.locators import CategoryPage
from opencart.locators import MainPage
from opencart.locators import ProductPage
from opencart.locators import SearchPage


def test_element_MP(browser):
    b = browser
    b.find_element_by_id(MainPage.top_link).click()

def test_element_MP1(browser):
    bro = browser
    bro.find_element_by_class_name(MainPage.featured)

def test_element_MP2(browser):
    bro = browser
    bro.find_element_by_id(MainPage.go_home)

def test_element_MP4(browser):
    bro = browser
    bro.find_element_by_class_name(MainPage.footer)

def test_element_MP5(browser):
    bro = browser
    bro.find_element_by_class_name(MainPage.next)

def test_elevent_AP1(browser):
    bro = browser
    browser.get("https://demo.opencart.com/admin")
    bro.find_elements_by_css_selector(AdminPage.logo)

def test_elevent_AP2(browser):
    bro = browser
    browser.get("https://demo.opencart.com/admin")
    bro.find_elements_by_id(AdminPage.user_name)

def test_elevent_AP3(browser):
    bro = browser
    browser.get("https://demo.opencart.com/admin")
    bro.find_elements_by_id(AdminPage.password)

def test_elevent_AP4(browser):
    bro = browser
    browser.get("https://demo.opencart.com/admin")
    bro.find_elements_by_class_name(AdminPage.forget_password)

def test_elevent_AP5(browser):
    bro = browser
    browser.get("https://demo.opencart.com/admin")
    bro.find_element_by_class_name(AdminPage.login)

def test_elevent_CP1(browser):
    bro = browser
    browser.get("https://demo.opencart.com/index.php?route=product/category")
    bro.find_element_by_class_name(CategoryPage.contin)

def test_elevent_CP2(browser):
    bro = browser
    browser.get("https://demo.opencart.com/index.php?route=product/category")
    bro.find_element_by_css_selector(CategoryPage.pre_img)

def test_elevent_CP3(browser):
    bro = browser
    browser.get("https://demo.opencart.com/index.php?route=product/category")
    bro.find_elements_by_css_selector(CategoryPage.desktop)

def test_elevent_CP4(browser):
    bro = browser
    browser.get("https://demo.opencart.com/index.php?route=product/category")
    bro.find_elements_by_css_selector(CategoryPage.laptops)

def test_elevent_CP5(browser):
    bro = browser
    browser.get("https://demo.opencart.com/index.php?route=product/category")
    bro.find_elements_by_css_selector(CategoryPage.tablets)

def test_el_PP1(browser):
    bro = browser
    browser.get("https://demo.opencart.com/index.php?route=product/product&path=20_27&product_id=41")
    bro.find_elements_by_css_selector(ProductPage.add_to_card)

def test_el_PP2(browser):
    bro = browser
    browser.get("https://demo.opencart.com/index.php?route=product/product&path=20_27&product_id=41")
    bro.find_elements_by_class_name(ProductPage.img_prod)

def test_el_PP3(browser):
    bro = browser
    browser.get("https://demo.opencart.com/index.php?route=product/product&path=20_27&product_id=41")
    bro.find_elements_by_class_name(ProductPage.big_img)

def test_el_PP4(browser):
    bro = browser
    browser.get("https://demo.opencart.com/index.php?route=product/product&path=20_27&product_id=41")
    bro.find_elements_by_css_selector(ProductPage.cost)

def test_el_PP4(browser):
    bro = browser
    browser.get("https://demo.opencart.com/index.php?route=product/product&path=20_27&product_id=41")
    bro.find_elements_by_css_selector(ProductPage.cost)

def test_el_PP5(browser):
    bro = browser
    browser.get("https://demo.opencart.com/index.php?route=product/product&path=20_27&product_id=41")
    bro.find_elements_by_id(ProductPage.quantity)

def test_el_SP1(browser):
    bro = browser
    bro.find_elements_by_class_name(SearchPage.in_put)

def test_el_SP2(browser):
    bro = browser
    bro.find_elements_by_class_name(SearchPage.button_search)

def test_el_SP3(browser):
    bro = browser
    browser.get("https://demo.opencart.com/index.php?route=product/search")
    bro.find_elements_by_class_name(SearchPage.search_criteria)

def test_el_SP4(browser):
    bro = browser
    browser.get("https://demo.opencart.com/index.php?route=product/search")
    bro.find_elements_by_class_name(SearchPage.search_category)

def test_el_SP5(browser):
    bro = browser
    browser.get("https://demo.opencart.com/index.php?route=product/search")
    bro.find_elements_by_id(SearchPage.blue_button)








