from locator import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
    # locator = (By.NAME, "q") # name = "q"
    # locator = (By.XPATH, '//*[@id="id-search-field"]')
    locator = (By.CSS_SELECTOR, '#id-search-field')

# class GoButtonEment(BasePageElement):
#     locator = "go"

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "Python" in self.driver.title
    
    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON) # Unpack
        element.click()


class SearchResultPage(BasePage):
    
    def is_results_found(self):
        return "No results found" not in self.driver.page_source
