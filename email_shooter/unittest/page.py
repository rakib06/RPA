from locator import *
from element import BasePageElement

class EmailTextElement(BasePageElement):
    locator = "identifier" # name = "q"

class PwdTextElement(BasePageElement):
    locator = "password" # name = "q"

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    
    email_text_element = EmailTextElement() 
    pwd_text_element = PwdTextElement()

    def click_next_button(self):
        element = self.driver.find_element(*EmailPageLocator.NEXT_BUTTON) # Unpack
        element.click()
        