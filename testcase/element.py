from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement:
    # locator = (By.CSS_SELECTOR, '#id-search-field')
    def __set__(self, obj, value):
        driver = obj.driver
        element = WebDriverWait(driver, 100).until(lambda driver: driver.find_element(*self.locator))   
        element.clear()
        element.send_keys(value)

    def __get__(self, obj):
        driver = obj.driver
        element =  WebDriverWait(driver, 100).until(lambda driver: driver.find_element(*self.locator))
        return element.get_attribute("value")
  
