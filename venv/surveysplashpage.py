
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as action
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


import time
import random


'''Splash screen close button ID 'closeButton'
Text: Welcome to the Ford website.
We value your opinions!
Will you take a short survey AFTER your visit to tell us about your experience today?

Yes button = <a class="btn btn-yes"
    href="javascript:parent.ipe705.fOpen()"
No button = <a class="btn btn-no"
    href="javascript:void(0)"'''

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('-incognito')
driver = webdriver.Chrome(r"C:\drivers\chromedriver.exe", options=chrome_options)


driver.get("https://shop.ford.com/quote/mustang/?redirectpage=Bp2ChooseYourPath#/options/Config%5B%7CFord%7CMustang%7C2020%7C1%7C1.%7C100A.P8T.....COU.~YZKAA.EBST.LESS.%5D")
your_preferences_button = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Preferences')]")))
your_preferences_button.click()
button = driver.find_element_by_xpath('//div[starts-with(@aria-label, "6-Speed Manual Transmission")]')
time.sleep(4)
button.click()




