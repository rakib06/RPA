# importing packages
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# imports for wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# ---- X ---------- 

# web driver initializations (Set path and others)
target_site = ["https://www.techwithtim.net", "https://mail.google.com/"]
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
compose = driver.find_elements_by_xpath("//div[contains(text(),'COMPOSE')]")
print(compose)
compose.click()

time.sleep(20)
# driver.quit()
# explicit waits 
try:
    compose = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(By.XPATH, "//div[contains(text(),'COMPOSE')]")
    )
    compose.click()


except:
    print("Hi")
    # driver.quit()
# driver.quit()