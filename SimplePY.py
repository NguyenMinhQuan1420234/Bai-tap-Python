from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

Path = "C:\Program Files (x86)\chromedriver"
driver = webdriver.Chrome(Path)

driver.get("https://techwithtim.net")
print(driver.title)


driver.quit()
'''
import time

# driver = webdriver.
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver")

driver.implicitly_wait(30)
driver.set_page_load_timeout(50)
driver.get("https://qavbox.github.io/demo")
assert "QAVBOX" in driver.title
driver.find_element(By.LINK_TEXT, "SignUp Form").click()

driver.save_screenshot("Downloads/test.png")
time.sleep(3)
driver.quit()
'''