from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path="../driver/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("youtube krish naik")
driver.find_element_by_name("btnK").click()

driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("Anilkumar P")
driver.find_element_by_name("btnK").click()

driver.refresh()
time.sleep(5)
driver.quit()
