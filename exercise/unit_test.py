# importing packages
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# imports for wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Action Chains 
from selenium.webdriver.common.action_chains import ActionChains
# ---- X ---------- 




# web driver initializations (Set path and others)
target_site = ["https://www.techwithtim.net",\
     "https://mail.google.com/", \
     "https://orteil.dashnet.org/cookieclicker/"]
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get(target_site[1])

# working with targets (Functionalities)

email_id = driver.find_element_by_id("identifierId")
email_id.send_keys("test.rakib789@gmail.com")
email_id.send_keys(Keys.RETURN)
time.sleep(2)
pwd = driver.find_element_by_name("password")
pwd.send_keys("selenium@789")
pwd.send_keys(Keys.RETURN)


time.sleep(10)

# link = driver.find_elements_by_class_name("T-I T-I-KE L3")
# print(link)
# print(link.text)
# link[0].click()
compose = driver.find_element_by_id(":36")
actions = ActionChains(driver)
actions.click(compose)
actions.perform()

time.sleep(2)

email_to = driver.find_element_by_id(":90") 
email_to.send_keys("rakibul.hsn47@gmail.com")
email_to.send_keys(Keys.RETURN)
time.sleep(2)
subject = driver.find_element_by_id(":8i")
subject.send_keys("This is a test email ")
subject.send_keys(Keys.RETURN)
time.sleep(2)

email_text = driver.find_element_by_id(":9o")
email_text.send_keys(my_email)
email_text.send_keys(Keys.RETURN)
time.sleep(5)

compose = driver.find_element_by_id(":88")
actions = ActionChains(driver)
actions.click(compose)
actions.perform()

time.sleep(10)
    # driver.quit()
# driver.quit()