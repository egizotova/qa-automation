from selenium.webdriver.common.by import By

from pageobject.BasePage import BasePage


class SeacrhLocators:

    IN_PUT = (By.CSS_SELECTOR, "#search > input")
    BUTTON_SEARCH = (By.CSS_SELECTOR, "#search > span > button")
    SEARCH_CRITERIA = "input-search"
    SEARCH_CATEGORY = "form-control"
    BLUE_BUTTON = "button-search"
    RESULT = (By.CSS_SELECTOR, "#content > div:nth-child(8) > div:nth-child(1)")
    ADD_TO_WISH = (By.CSS_SELECTOR, '#content > div:nth-child(8) > div:nth-child(1) > div > div:nth-child(2) > div.button-group > button:nth-child(2)')

class SearchPage(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(SeacrhLocators.IN_PUT)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(SeacrhLocators.BUTTON_SEARCH, time=2).click()

    def check_navigation(self):
        all_list = self.find_elements(SeacrhLocators.RESULT, time=2)
        result = [x.text for x in all_list if len(x.text) > 0]
        return result

    def add_to_wish(self):
        wish = self.find_element(SeacrhLocators.ADD_TO_WISH).click()
        return wish

