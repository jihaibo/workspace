from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://saas.mei1.com")
driver.implicitly_wait(8)
driver.maximize_window()

driver.find_element_by_id("userName").send_keys("18721527961")
driver.find_element_by_id("password").send_keys("jhb104674")
driver.find_element_by_id("loginBtn").click()

time.sleep(3)
strlong = driver.title
print strlong

driver.quit()