'''
(PROJECTNAME)ItemSelectorClass Template

This is a template class for accessing and selecting elements on a web page.

METHOD ASSUMPTIONS:

THERE IS A TRY/EXCEPT CLAUSE FOR EVERY SINGLE METHOD!! THIS IS NOT SHOWN FOR EVERY ONE
BUT IT IS IMPLIED! A single function failure should not mean the whole class fails.

Confirmation messages are also implied

The methods are organized into how (I feel) they should be designed based on the element we are interacting with
(button, select, radio button, etc.)
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as action
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

import time
import random

class ItemSelectorClass:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('-icognito')
        self.driver = webdriver.Chrome(r"C:\drivers\chromedriver.exe", options=self.chrome_options)
        self.CurrentModule = "Initialization"
        self.ErrorCount = 0
        self.driver.get("https://www.ford.com/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(5)
        #self.driver.quit()

    def loadtime(self):
        navigationStart = self.driver.execute_script("return window.performance.timing.navigationStart")
        responseStart = self.driver.execute_script("return window.performance.timing.responseStart")
        domComplete = self.driver.execute_script("return window.performance.timing.domComplete")
        # Calculate the performance
        backendPerformance_calc = responseStart - navigationStart
        frontendPerformance_calc = domComplete - responseStart
        print("Back End: %s" % backendPerformance_calc)
        print("Front End: %s" % frontendPerformance_calc)
        return

    def close_browser(self):
        self.driver.quit()

#Selecting the buttons on the home page to initiate the customization process flow (Test Cases A01 - A06)
    def get_to_car_build(self):
        print("got here")
        time.sleep(3)
        print("waited")
        vehicles_home_page_button = self.driver.find_element_by_xpath("/html/body/header/div[5]/nav/div[2]/div[2]/ul[1]/li[1]/a")
        print("found vehicles")
        action(self.driver).move_to_element(vehicles_home_page_button).click().perform()
        print('\tvehicles button on home page has been found and selected')
        print('\t\tTest A01 has passed')

        time.sleep(3)

        cars_home_page_button = self.driver.find_element_by_xpath('/html/body/header/div[5]/nav/div[2]/div[2]/ul[1]/li[1]/div/nav/div/ul/li[3]/a')
        print("found cars")
        action(self.driver).move_to_element(cars_home_page_button).click().perform()
        print('\tcars button on home page has been found and selected')
        print('\t\tTest A02 has passed')

        time.sleep(3)

        mustang_button_2020 = self.driver.find_element_by_xpath('//*[@id="fgx-mainNavigation-tertiary_menu_2"]/li[3]/a/div/div[2]/span')
        print("found 2020 mustang")
        action(self.driver).move_to_element(mustang_button_2020).click().perform()
        print('\t2020 mustang button on home page has been found and selected')
        print('\t\tTest A03 has passed')

        time.sleep(3)

        build_and_price_button = self.driver.find_element_by_xpath('//*[@id="component01"]/div/div/div/div/div[1]/div[2]/div/div[2]/div/div[2]/p/a')
        print("found build & price")
        action(self.driver).move_to_element(build_and_price_button).click().perform()
        print('\tbuild & price button on home page has been found and selected')
        print('\t\tTest A04 has passed')

        time.sleep(3)

        select_zip_button = self.driver.find_element_by_xpath('/html/body/div[20]/div/div/form/div/div[3]/input')
        print("found enter zip field")
        action(self.driver).move_to_element(select_zip_button).click().send_keys('60448').perform()
        print('\tzip code field has been found, selected, and has had a zip code entered')

        time.sleep(2)

        enter_zip_button = self.driver.find_element_by_xpath('/html/body/div[20]/div/div/form/div/button')
        print("found enter")
        action(self.driver).move_to_element(enter_zip_button).click().perform()
        print('\tzip code enter button has been found and selected')
        print('\t\tTest A05 has passed')

        time.sleep(3)

        build_your_own_button = self.driver.find_element_by_xpath('/html/body/div[9]/div[7]/div/div/div/div/div/div[2]/div[1]/a')
        print("found bouild your own")
        action(self.driver).move_to_element(build_your_own_button).click().perform()
        print('\tbuild your own button has been found and selected')
        print('\t\tTest A06 has passed')
        return

#Setting up the mustang model to be tested, includes which model and which option of performance (Test Case B01)
    def choose_your_model_convertible(self):
        time.sleep(2)
        convertible_button = self.driver.find_element_by_xpath('//*[@id="tech-list-price-ecoboostconvertible"]')
        print("found convertible")
        action(self.driver).move_to_element(convertible_button).click().perform()
        print('\tconvertible button has been found and selected')

        time.sleep(2)

        convertible_image = self.driver.find_element_by_xpath('//*[@id="main-container"]/div/div/div[2]/div/div[2]/div[2]/div[3]/span/img')
        print("found configure")
        action(self.driver).move_to_element(convertible_image).click().perform()
        print('\tconfigure button has been found and selected')
        print('\t\tTest B01 has passed')
        return

    time.sleep(10)

#Selecting all possible paint options in the paint type category (Test Case C01)
    def paint_type(self):
        grabber_lime = self.driver.find_element_by_xpath('//*[@id="accordion-body-1"]/div/div[2]/div/div[2]/div[1]/ul/li[2]/div/div[1]/div')
        print("found grabber lime")
        action(self.driver).move_to_element(grabber_lime).click().perform()

        oxford_white = self.driver.find_element_by_xpath('//*[@id="accordion-body-1"]/div/div[2]/div/div[2]/div[1]/ul/li[3]/div/div[1]/div')
        print("found oxford white")
        action(self.driver).move_to_element(oxford_white).click().perform()

        velocity_blue = self.driver.find_element_by_xpath('//*[@id="accordion-body-1"]/div/div[2]/div/div[2]/div[1]/ul/li[4]/div/div[1]/div')
        print("found velocity blue")
        action(self.driver).move_to_element(velocity_blue).click().perform()

        iconic_silver = self.driver.find_element_by_xpath('//*[@id="accordion-body-1"]/div/div[2]/div/div[2]/div[1]/ul/li[5]/div/div[1]/div')
        print("found iconic silver")
        action(self.driver).move_to_element(iconic_silver).click().perform()

        magnetic = self.driver.find_element_by_xpath('//*[@id="accordion-body-1"]/div/div[2]/div/div[2]/div[1]/ul/li[6]/div/div[1]/div')
        print("found magnetic")
        action(self.driver).move_to_element(magnetic).click().perform()

        race_red = self.driver.find_element_by_xpath('//*[@id="accordion-body-1"]/div/div[2]/div/div[2]/div[1]/ul/li[7]/div/div[1]/div')
        print("found race red")
        action(self.driver).move_to_element(race_red).click().perform()

        rapid_red = self.driver.find_element_by_xpath('//*[@id="accordion-body-1"]/div/div[2]/div/div[2]/div[1]/ul/li[8]/div/div[1]/div')
        print("found rapid red")
        action(self.driver).move_to_element(rapid_red).click().perform()

        kona_blue = self.driver.find_element_by_xpath('//*[@id="accordion-body-1"]/div/div[2]/div/div[2]/div[1]/ul/li[8]/div/div[1]/div')
        print("found kona_blue")
        action(self.driver).move_to_element(kona_blue).click().perform()

        kona_blue = self.driver.find_element_by_xpath('//*[@id="accordion-body-1"]/div/div[2]/div/div[2]/div[1]/ul/li[9]/div/div[1]/div')
        print("found kona_blue")
        action(self.driver).move_to_element(kona_blue).click().perform()

        twister_orange = self.driver.find_element_by_xpath('//*[@id="accordion-body-1"]/div/div[2]/div/div[2]/div[1]/ul/li[10]/div/div[1]/div')
        print("found twister orange")
        action(self.driver).move_to_element(twister_orange).click().perform()

        shadow_black = self.driver.find_element_by_xpath('//*[@id="accordion-body-1"]/div/div[2]/div/div[2]/div[1]/ul/li[10]/div/div[1]/div')
        print("found shadow black")
        action(self.driver).move_to_element(shadow_black).click().perform()
        return

    def tape_stripe(self):
        silver_tape_stripe = self.driver.find_element_by_xpath('//*[@id="accordion-body-1"]/div/div[2]/div/div[2]/div[2]/ul/li[2]/div/div[1]/div')
        print("found silver tape stripe")
        action(self.driver).move_to_element(silver_tape_stripe).click().perform()
        change_requirement_yes = self.driver.find_element_by_xpath('/html/body/div[21]/div/div/div/div[8]/div[3]/a[2]')
        print("found and selected yes change button")
        action(self.driver).move_to_element(change_requirement_yes).click().perform()

        ebony_tape_stripe = self.driver.find_element_by_xpath('//*[@id="accordion-body-1"]/div/div[2]/div/div[2]/div[2]/ul/li[3]/div/div[1]/div')
        print("found ebony tape stripe")
        action(self.driver).move_to_element(ebony_tape_stripe).click().perform()
        change_requirement_yes = self.driver.find_element_by_xpath('/html/body/div[21]/div/div/div/div[8]/div[3]/a[2]')
        print("found and selected yes change button")
        action(self.driver).move_to_element(change_requirement_yes).click().perform()
        return

    def racing_stripe(self):
        ebony_racing_stripe = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div[4]/ul/li[2]/div/div[1]/div')
        print("found ebony racing stripe")
        action(self.driver).move_to_element(ebony_racing_stripe).click().perform()

        less_racing_stripe = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div[4]/ul/li[1]/div/div[1]/div')
        print("found less racing stripe")
        action(self.driver).move_to_element(less_racing_stripe).click().perform()
        change_requirement_yes = self.driver.find_element_by_xpath('/html/body/div[21]/div/div/div/div[8]/div[3]/a[2]')
        print("found and selected yes change button")
        action(self.driver).move_to_element(change_requirement_yes).click().perform()
        return

    def hood_and_side_stripes(self):
        metallic_gray_hood_stripe = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div[5]/ul/li[1]/div/div[1]/div')
        print("found metallic gray hood stripe")
        time.sleep(3)
        action(self.driver).move_to_element(metallic_gray_hood_stripe).click().perform()
        change_requirement_yes = self.driver.find_element_by_xpath('/html/body/div[21]/div/div/div/div[8]/div[3]/a[2]')
        print("found and selected yes change button")
        action(self.driver).move_to_element(change_requirement_yes).click().perform()

        silver_hood_stripe = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div[5]/ul/li[2]/div/div[1]/div')
        print("found silver hood stripe")
        action(self.driver).move_to_element(silver_hood_stripe).click().perform()
        change_requirement_yes = self.driver.find_element_by_xpath('/html/body/div[21]/div/div/div/div[8]/div[3]/a[2]')
        print("found and selected yes change button")
        action(self.driver).move_to_element(change_requirement_yes).click().perform()

        ebony_hood_stripe = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div[5]/ul/li[3]/div/div[1]/div')
        print("found ebony hood stripe")
        action(self.driver).move_to_element(ebony_hood_stripe).click().perform()
        change_requirement_yes = self.driver.find_element_by_xpath('/html/body/div[21]/div/div/div/div[8]/div[3]/a[2]')
        print("found and selected yes change button")
        action(self.driver).move_to_element(change_requirement_yes).click().perform()
        return

    def powertrain(self):
        powertarin_select = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[2]/div[1]/div')
        print("found powertrain select")
        action(self.driver).move_to_element(powertarin_select).click().perform()

        ecoboost_engine = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[2]/div[1]/div')
        print("found ecoboost engine")
        action(self.driver).move_to_element(ecoboost_engine).click().perform()
        close = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[3]')
        action(self.driver).move_to_element(close).click().perform()

        high_performance_ecoboost_engine = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/ul/li[2]/div[1]/div[2]/img')
        print("found high performance ecoboost engine")
        action(self.driver).move_to_element(high_performance_ecoboost_engine).click().perform()
        add = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[4]/div[3]/a')
        action(self.driver).move_to_element(add).click().perform()
        change_requirement_yes = self.driver.find_element_by_xpath('/html/body/div[21]/div/div/div/div[8]/div[3]/a[2]')
        print("found and selected yes change button")
        action(self.driver).move_to_element(change_requirement_yes).click().perform()

        automatic_tramsmission = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/ul/li[1]/div[1]/div[2]/img')
        print("found automatic transmission")
        action(self.driver).move_to_element(automatic_tramsmission).click().perform()
        add = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[4]/div[3]/a')
        action(self.driver).move_to_element(add).click().perform()

        manual_tramsmission = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/ul/li[2]/div[1]/div[2]/img')
        print("found manual transmission")
        action(self.driver).move_to_element(manual_tramsmission).click().perform()
        add = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[4]/div[3]/a')
        action(self.driver).move_to_element(add).click().perform()
        return

'''define ItemSelection SELECT method(self, index): < index arg lets you select a choice from outside the class
        try:
            use explicit wait to find the element
            select the index that is passed as an argument
            print success message
        except:
            print error message

    define ItemSelection RADIO method(self, index)
        try:
            create an if-else statement that selects the radio button based on the index (case-switch works too, probably better)
            i.e.
            if index == 0
                choose radio button option 0 (you will likely need to find this element via label)
                explicit wait doesnt always work here, might have to use a time.sleep
            else if index == 1
                same thing but next label
            else if index == 2
                same thing but next label

            print success message
        except:
            print error message

    define ItemSelection INPUT method(self, text)
        try:
            use explicit wait to find the input element
            use an action chain to click the element, then sendkeys "text"
            print success message
        except:
            print error message
'''
