import time
from pageobject.Common import Common
from pageobject.MainPage import MainPage
from pageobject.MainPage import MainPageLocators
from pageobject.SearchPage import SearchPage
from pageobject.WishlistPage import WishlistPage

def test_add_to_cart(browser):
    main_page = MainPage(browser)  # открываем браузер
    main_page.go_to_site()  # переходим на сайт
    main_page.add_to_cart
    time.sleep(2)
    main_page.checkout_click()
    time.sleep(4)
    main_page.check_cart()


def test_delete_out_cart(browser):
    main_page = MainPage(browser)  # открываем браузер
    main_page.go_to_site()  # переходим на сайт
    main_page.add_to_cart
    main_page.checkout_click()
    main_page.check_cart()
    main_page.delete()
    main_page.find_element(MainPageLocators.EMPTY)

def test_add_to_wishlist(browser):
    search_page = SearchPage(browser)
    search_page.go_to_site()
    search_page.enter_word("mac")
    search_page.click_on_the_search_button()
    search_page.add_to_wish()
    common = Common(browser)
    common.click_wishlist


def test_add_to_cart_from_wish(browser):
    search_page = SearchPage(browser)
    search_page.go_to_site()
    search_page.enter_word("mac")
    search_page.click_on_the_search_button()
    search_page.add_to_wish()
    common = Common(browser)
    time.sleep(4)
    common.click_wishlist
    time.sleep(4)
    common.enter_email()
    common.enter_password()
    common.login()
    wishlist = WishlistPage(browser)
    time.sleep(2)
    wishlist.add()

def test_add_to_cart_delete(browser):
    search_page = SearchPage(browser)
    search_page.go_to_site()
    search_page.enter_word("mac")
    search_page.click_on_the_search_button()
    search_page.add_to_wish()
    common = Common(browser)
    time.sleep(9)
    common.click_wishlist
    time.sleep(4)
    common.enter_email()
    common.enter_password()
    common.login()
    wishlist = WishlistPage(browser)
    time.sleep(2)
    wishlist.add()
    main_page = MainPage(browser)
    main_page.checkout_click()
    main_page.check_cart()
    main_page.delete()
    time.sleep(3)
    main_page.find_element(MainPageLocators.EMPTY)

def test_ppc(browser):
    main_page = MainPage(browser)
    main_page.go_to_site()
    main_page.dropdown_cart()