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
driver.maximize_window() 
# ---- X ---------- 

to_email_text = "rakibul.hsn47@gmail.com rakib.unibit@gmail.com"
cc_email_text = "rakibul.hasan@bracits.com"
bcc_email_text = "six.rakib@gmail.com rakib.hsn32@gmail.com"

subject_text = "Robotic Process Automation "

my_email = '''

Dear Vaia,

Good morning.


https://devhints.io/xpath

Have a good day. RPA testing. RPA full form is Robotic Process Automation .


Thanks and Regards, 
MD. RAKIBUL HASAN MOLLA 
Software Engineer 
BRAC IT Services Limited 
Cell: +8801322875296 
'''


email_id = driver.find_element_by_id("identifierId")
email_id.send_keys("test.rakib789@gmail.com")
email_id.send_keys(Keys.RETURN)
time.sleep(5)

pwd = driver.find_element_by_name("password")
pwd.send_keys("selenium@789")
pwd.send_keys(Keys.RETURN)
time.sleep(10)

compose = driver.find_element_by_xpath("//*[contains(text(),'Compose')]")
actions = ActionChains(driver)
actions.click(compose)
actions.perform()
time.sleep(2)

driver.find_element(By.NAME,'to').send_keys("rakibul.hsn47@gmail.com")
ActionChains(driver).send_keys(Keys.TAB * 1).perform()


driver.find_element_by_xpath("//span[text()='Cc']").click()
cc = driver.find_element_by_css_selector("textarea[aria-label='Cc']")
cc.send_keys("six.rakib@gmail.com")
cc.send_keys(Keys.RETURN)


driver.find_element_by_xpath("//span[text()='Bcc']").click()
bcc = driver.find_element_by_css_selector("textarea[aria-label='Bcc']")
bcc.send_keys("rakib.hsn32@gmail.com")
bcc.send_keys(Keys.RETURN)

driver.find_element(By.NAME,'subjectbox').send_keys("This email is using selenium")


message_body = driver.find_element_by_css_selector("div[aria-label='Message Body']")
message_body.send_keys(my_email)
message_body.send_keys(Keys.RETURN)

sendElem = driver.find_element_by_xpath("//div[text()='Send']")
sendElem.click()

time.sleep(10)
driver.quit()
