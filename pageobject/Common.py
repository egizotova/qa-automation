from selenium.webdriver.common.by import By

from pageobject.BasePage import BasePage


class CommonLocators:
    WISH = (By.CSS_SELECTOR, "#wishlist-total > span")
    EMAIL = (By.ID, "input-email")
    PASSWORD = (By.ID, "input-password")
    LOGIN = (By.CSS_SELECTOR, "#content > div > div:nth-child(2) > div > form > input.btn.btn-primary")


class Common(BasePage):

    def click_wishlist(self):
        wishlist = self.find_element(CommonLocators.WISH).click()
        return wishlist

    def enter_email(self):
        email_to = self.find_element(CommonLocators.EMAIL)
        email_to.clear()
        email_to.click()
        email_to.send_keys("nnqnwmxm@supere.ml")
        return email_to

    def enter_password(self):
        passw_to = self.find_element(CommonLocators.PASSWORD)
        passw_to.clear()
        passw_to.click()
        passw_to.send_keys("Qq123456")
        return passw_to

    def login(self):
        button = self.find_element(CommonLocators.LOGIN).click()
        return button
