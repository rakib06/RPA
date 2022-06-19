from selenium.webdriver.support.ui import WebDriverWait

class BasePageElement:
    
    # locator = "q"
    
    def __init__(cls, method='name'):
        cls.method = method
    
    def find_element(self, driver):
        if self.method == 'name':
            WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_name(self.locator))
            return driver.find_element_by_name(self.locator)
        if self.method == 'xpath':
            WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_xpath(self.locator))
            return driver.find_element_by_xpath(self.locator)
        if self.method == 'id':
            WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_id(self.locator))
            return driver.find_element_by_id(self.locator)

    def __set__(self, obj, value):
        driver = obj.driver
        element = self.find_element(driver)
        element.clear()
        element.send_keys(value)

    
    def __get__(self, obj):
        driver = obj.driver
        
        element = self.find_element(driver)
        return element.get_attribute("value")
    

class BasePageElement_by_NAME(BasePageElement):
    def __init__(cls, method='name'):
        super().__init__(method)

class BasePageElement_by_ID(BasePageElement):
    def __init__(cls, method='name'):
        super().__init__(method)
class BasePageElement_by_XPATH(BasePageElement):
    def __init__(cls, method='xpath'):
        super().__init__(method)
