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
# ---- X ---------- 

to_email_text = "rakibul.hsn47@gmail.com rakib.unibit@gmail.com"
cc_email_text = "rakibul.hasan@bracits.com"
bcc_email_text = "six.rakib@gmail.com rakib.hsn32@gmail.com"

subject_text = "Robotic Process Automation "

my_email = '''

Dear Vaia,

Good morning.

Have a good day. RPA testing. RPA full form is Robotic Process Automation .


Thanks and Regards, 
MD. RAKIBUL HASAN MOLLA 
Software Engineer 
BRAC IT Services Limited 
Cell: +8801322875296 
'''



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

email_to = driver.find_element_by_id(":ia") 
email_to.send_keys(to_email_text)
email_to.send_keys(Keys.RETURN)
time.sleep(2)

email_cc = driver.find_element_by_id(":ib") 
email_cc.send_keys(cc_email_text)
email_cc.send_keys(Keys.RETURN)
time.sleep(2)

email_bcc = driver.find_element_by_id(":ic")
email_bcc.send_keys(bcc_email_text)
email_bcc.send_keys(Keys.RETURN)
time.sleep(2)

subject = driver.find_element_by_id(":8i")
subject.send_keys(subject_text)
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
driver.quit()
# driver.quit()


# ## Email & Password
# # email: test.rakib789@gmail.com, pwd: selenium@789  

# # importing packages
# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# # imports for wait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# # ---- X ---------- 

# # web driver initializations (Set path and others)
# target_site = ["https://www.techwithtim.net", "https://mail.google.com/"]
# PATH = "C:\Program Files (x86)\chromedriver.exe"
# driver = webdriver.Chrome(PATH)
# driver.get(target_site[1])

# # working with targets (Functionalities)

# email_id = driver.find_element_by_id("identifierId")
# email_id.send_keys("test.rakib789@gmail.com")
# email_id.send_keys(Keys.RETURN)
# time.sleep(2)

# pwd = driver.find_element_by_name("password")
# pwd.send_keys("selenium@789")
# pwd.send_keys(Keys.RETURN)
# time.sleep(10)

# compose = driver.find_elements_by_xpath("//div[contains(text(),'Compose')]")
# print(compose)
# compose.click()


# # # explicit waits 
# # try:
# #     compose = WebDriverWait(driver, 10).until(
# #         EC.presence_of_element_located(By.LINK_TEXT, "COMPOSE")
# #     )
# #     compose.click()


# # except:
# #     print("Hi")
# #     # driver.quit()
# # driver.quit()