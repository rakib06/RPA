import time
import unittest
from selenium import webdriver
import page
import os


class GmailEmailShoot(unittest.TestCase):

    # Open the browser 
    def setUp(self):
        self.driver = webdriver.Chrome(os.environ.get('driver_os_path'))

        self.driver.get(os.environ.get('website'))
        self.driver.maximize_window() 

    # Test Login credentials 
    def test_test_login(self):
        mainPage = page.MainPage(self.driver)
        mainPage.email_text_element = os.environ.get('email')
        mainPage.click_next_button()
        time.sleep(4)
        mainPage.pwd_text_element = os.environ.get('pwd')
        mainPage.click_next_button()
        time.sleep(15)
 
    # Close the browser 
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()