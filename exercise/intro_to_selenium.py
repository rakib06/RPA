from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# imports for wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# ---- X ---------- 
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.techwithtim.net")


print(driver.title)

## Username & Password for exam player 
# uname: test, pw: test@123

## Test site: https://www.techwithtim.net/


# id/name/class to access input field 
search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

# print(driver.page_source)
try:
    # main = driver.find_element_by_id("main")
    # Here main means the elements 
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-summary") 
        print(header.text)
finally:
    driver.quit()
# except:
#     driver.quit()

# print(main.text)

# time.sleep(5)

# driver.quit()