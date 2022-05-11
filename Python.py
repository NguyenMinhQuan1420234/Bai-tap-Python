from selenium.webdriver import Chrome
import time
import matplotlib
driver = Chrome("C:\Program Files (x86)\chromedriver")

driver.set_page_load_timeout(3000)
time.sleep(30)
driver.__exit__
