from selenium.webdriver.common.by import By

from pageobject.BasePage import BasePage


class WishlistPageLocators:
    ADD = (By.CSS_SELECTOR, "#content > div.table-responsive > table > tbody > tr > td:nth-child(6) > button > i")


class WishlistPage(BasePage):

    def add(self):
        button = self.find_element(WishlistPageLocators.ADD)
        button.click()
        return button
