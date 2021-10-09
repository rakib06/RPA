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
driver.get(target_site[0])

# working with targets (Functionalities)
link = driver.find_element_by_link_text("")