import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):

    # Open the browser 
    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("http://www.python.org")
    
    # def test_example(self):
    #     print("Test")
    #     assert True, "This is a assert test"

    # def test_example_2(self):
    #     assert True 

    # def not_a_test(self):
    #     print("this wont print")
    
    # Close the browser 
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()