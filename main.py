from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.maximize_window()

driver.get('https://www.python.org/')
sleep(1)

driver.find_element_by_id("id-search-field").send_keys('python')

driver.find_element_by_id("submit").click()

btn = driver.find_element_by_id('submit').text

print(btn)
