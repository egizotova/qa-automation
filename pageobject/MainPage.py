from selenium.webdriver.common.by import By

from pageobject.BasePage import BasePage


class MainPageLocators:
    TOP_LINK = "top-links"
    FEATURED = "img-responsive"
    ADD_TO_CART = (By.CSS_SELECTOR, "#content > div.row > div > div > div.button-group > button:nth-child(1) > span")
    GO_HOME = "common-home"
    FOOTER = "container"
    NEXT = "swiper-button-next"
    CHECKOUT = (By.CSS_SELECTOR, "#top-links > ul > li:nth-child(5) > a > span")
    CART_IN = (By.CSS_SELECTOR, "#top-links > ul > li:nth-child(4) > a > span")
    DROPDOWN_CART = (By.CSS_SELECTOR, "#cart > ul")
    BUTTON_CHECK = (By.CSS_SELECTOR, "# content > div.buttons.clearfix > div.pull-right > a")
    DELETE = (By.CSS_SELECTOR, "#content > form > div > table > tbody > tr > td:nth-child(4) > div > span > button.btn.btn-danger")
    EMPTY = (By.CSS_SELECTOR, "#content > p")


class MainPage(BasePage):

    def add_to_cart(self):
        search_cart = self.find_element(MainPageLocators.ADD_TO_CART)
        search_cart.click()
        return search_cart

    def checkout_click(self):
        check = self.find_element(MainPageLocators.CHECKOUT)
        check.click()
        return check

    def check_cart(self):
        cart = self.find_element(MainPageLocators.CART_IN)
        cart.click()
        return cart

    def dropdown_cart(self):
        dropdown = self.find_element(MainPageLocators.DROPDOWN_CART)
        return dropdown

    def delete(self):
        delete = self.find_element(MainPageLocators.DELETE).click()
        return delete
