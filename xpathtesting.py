
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as action
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


import time
import random

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('-incognito')
driver = webdriver.Chrome(r"C:\drivers\chromedriver.exe", options=chrome_options)

driver.get("https://www.united.com/")

#test_button = wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='oneway' or @for='award']")))
test_button = driver.find_element_by_xpath("//*[@id='oneway']" or "//input[@id='award']")
test_button.click()
print('Clicked No button to Survey Splash Screen.')
