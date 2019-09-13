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
        #self.driver.maximize_window()
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
        vehicles_home_page_button = self.driver.find_element_by_xpath('//li[@data-dropdown.class="drop-parent.drop-item.vehicles"]')
        print("found vehicles")
        action(self.driver).move_to_element(vehicles_home_page_button).click().perform()
        print('\tvehicles button on home page has been found and selected')
        print('\t\t***Test A01 has passed***')

        time.sleep(3)

        cars_home_page_button = self.driver.find_element_by_xpath('/html/body/header/div[5]/nav/div[2]/div[2]/ul[1]/li[1]/div/nav/div/ul/li[3]/a')
        print("found cars")
        action(self.driver).move_to_element(cars_home_page_button).click().perform()
        print('\tcars button on home page has been found and selected')
        print('\t\t***Test A02 has passed***')

        time.sleep(3)

        mustang_button_2020 = self.driver.find_element_by_xpath('//*[@id="fgx-mainNavigation-tertiary_menu_2"]/li[3]/a/div/div[2]/span')
        print("found 2020 mustang")
        action(self.driver).move_to_element(mustang_button_2020).click().perform()
        print('\t2020 mustang button on home page has been found and selected')
        print('\t\t***Test A03 has passed***')

        time.sleep(3)

        build_and_price_button = self.driver.find_element_by_xpath('//*[@id="component01"]/div/div/div/div/div[1]/div[2]/div/div[2]/div/div[2]/p/a')
        print("found build & price")
        action(self.driver).move_to_element(build_and_price_button).click().perform()
        print('\tbuild & price button on home page has been found and selected')
        print('\t\t***Test A04 has passed***')

        time.sleep(3)

        print("looking for zip code field")
        time.sleep(2)
        select_zip_button = self.driver.find_element_by_xpath('/html/body/div[20]/div/div/form/div/div[3]/input')       /html/body/div[16]/div/div/form/div/div[3]/input
        print("found enter zip field")
        action(self.driver).move_to_element(select_zip_button).click().send_keys('60448').perform()
        print('\tzip code field has been found, selected, and has had a zip code entered')

        time.sleep(2)

        enter_zip_button = self.driver.find_element_by_xpath('/html/body/div[20]/div/div/form/div/button')
        print("found enter")
        action(self.driver).move_to_element(enter_zip_button).click().perform()
        print('\tzip code enter button has been found and selected')
        print('\t\t***Test A05 has passed***')

        time.sleep(3)

        build_your_own_button = self.driver.find_element_by_xpath('/html/body/div[9]/div[7]/div/div/div/div/div/div[2]/div[1]/a')
        print("found bouild your own")
        action(self.driver).move_to_element(build_your_own_button).click().perform()
        print('\tbuild your own button has been found and selected')
        print('\t\t***Test A06 has passed***')
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
        print('\t\t***Test B01 has passed***')
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

        twister_orange = self.driver.find_element_by_xpath('//*[@id="accordion-body-1"]/div/div[2]/div/div[2]/div[1]/ul/li[10]/div/div[1]/div')
        print("found twister orange")
        action(self.driver).move_to_element(twister_orange).click().perform()

        shadow_black = self.driver.find_element_by_xpath('//*[@id="accordion-body-1"]/div/div[2]/div/div[2]/div[1]/ul/li[10]/div/div[1]/div')
        print("found shadow black")
        action(self.driver).move_to_element(shadow_black).click().perform()

        print("\tall paint types have been selected")
        return

    # Selecting all possible tape stripe options in the paint type category (Test Case C01)
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
        print("looking for yes change requirement button")
        change_requirement_yes = self.driver.find_element_by_xpath('/html/body/div[21]/div/div/div/div[8]/div[3]/a[2]')
        print("found and selected yes change button")
        action(self.driver).move_to_element(change_requirement_yes).click().perform()

        print("\tall tape stripes have been selected")
        return

    # Selecting all possible racing stripe options in the paint type category (Test Case C01)
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

        print("\tall racing stripes have been selected")
        return

    # Selecting all possible paint options in the paint type category (Test Case C01)
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

        print("\tall hood and side stripes have been selected")
        print("\t\t***Test Case C01 has passed***")
        return

    # Selecting all possible engine and transmission options in the powertrain category (Test Case C02)
    def powertrain(self):
        powertrain_select = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[2]/div[1]/div/div/span[3]')
        action(self.driver).move_to_element(powertrain_select).click().perform()
        print("powertrain drop-down has been selected")

        time.sleep(2)

#TODO fix close button so it fucntions properly on the mustang convertible customization page
        #ecoboost_engine = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[2]/div[1]/div')
        #print("found ecoboost engine")
        #action(self.driver).move_to_element(ecoboost_engine).click().perform()
        #print("ecoboost engine has been selected")
        #print("looking for close button")
        #time.sleep(1)
        #close = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[3]/span[2]')
        #action(self.driver).move_to_element(close).click().perform()

        high_performance_ecoboost_engine = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/ul/li[2]/div[1]/div[2]/img')
        print("found high performance ecoboost engine")
        time.sleep(1)
        action(self.driver).move_to_element(high_performance_ecoboost_engine).click().perform()
        time.sleep(1)
        add = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[4]/div[3]/a')
        action(self.driver).move_to_element(add).click().perform()
        change_requirement_yes = self.driver.find_element_by_xpath('/html/body/div[21]/div/div/div/div[8]/div[3]/a[2]')
        print("found and selected yes change button")
        action(self.driver).move_to_element(change_requirement_yes).click().perform()
        print("\thigh performance ecoboost engine has been selected")

        automatic_tramsmission = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/ul/li[1]/div[1]/div[2]/img')
        print("found automatic transmission")
        action(self.driver).move_to_element(automatic_tramsmission).click().perform()
        print("looking for add button")
        time.sleep(1)
        add = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[4]/div[4]/a')
        action(self.driver).move_to_element(add).click().perform()
        print("\tautomatic transmission has been selected")

        manual_tramsmission = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/ul/li[2]/div[1]/div[2]/img')
        print("found manual transmission")
        action(self.driver).move_to_element(manual_tramsmission).click().perform()
        time.sleep(1)
        add = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[4]/div[3]/a')
        action(self.driver).move_to_element(add).click().perform()
        print("\tmanual transmission has been selected")

        print("\t\t***Test Case C02 has paseed***")
        return

    # Selecting all possible equipment group, exterior, and interior package options in the packages category (Test Case C03)
    def packages(self):
        packages_select = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[3]/div[1]/div/div')
        action(self.driver).move_to_element(packages_select).click().perform()
        print("packages drop-down has been selected")

        equipment_group_100A_radio_button = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[3]/div[2]/div[1]/ul/li[1]/div[2]/div/div[1]/div[1]/div/span')
        print("found equipment group 100A engine")
        action(self.driver).move_to_element(equipment_group_100A_radio_button).click().perform()
        print("equipment group 100A has been selected")

        equipment_group_101A_radio_button = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[3]/div[2]/div[1]/ul/li[2]/div[2]/div/div[1]/div[1]/div/span')
        print("found equipment group 101A engine")
        action(self.driver).move_to_element(equipment_group_101A_radio_button).click().perform()
        print("equipment group 101A has been selected")

#TODO fix close button for high performance package selection
        #high_performance_package_23L = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[3]/div[2]/div[2]/ul/li[1]/div[1]/div[2]/img')
        #print("found 2.3L high performance package")
        #action(self.driver).move_to_element(high_performance_package_23L).click().perform()
        #print("2.3L high performance package has been selected")
        #add = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[4]/div[3]/a')
        #action(self.driver).move_to_element(add).click().perform()
        #change_requirement_yes = self.driver.find_element_by_xpath('/html/body/div[21]/div/div/div/div[8]/div[3]/a[2]')
        #print("found and selected yes change button")
        #action(self.driver).move_to_element(change_requirement_yes).click().perform()

        black_accent_package = self.driver.find_element_by_xpath("/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[3]/div[2]/div[2]/ul/li[2]/div[1]/div[2]/img")
        print("found black accent package")
        action(self.driver).move_to_element(black_accent_package).click().perform()
        time.sleep(1)
        print("looking for add button")
        add = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[4]/div[4]/a')
        print("black accent package has been added")
        action(self.driver).move_to_element(add).click().perform()
        change_requirement_yes = self.driver.find_element_by_xpath('/html/body/div[21]/div/div/div/div[8]/div[3]/a[2]')
        print("found and selected yes change button")
        action(self.driver).move_to_element(change_requirement_yes).click().perform()
        print("\tblack accent package has been selected")

        # TODO fix close button for security package selection
        #enhanced_security_package = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[3]/div[2]/div[2]/ul/li[3]/div[1]/div[3]/img')
        #print("found enhanced security package")
        #action(self.driver).move_to_element(enhanced_security_package).click().perform()
        #print("enhanced security package has been selected")
        #close = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[3]')
        #action(self.driver).move_to_element(close).click().perform()

        wheel_and_stripe_package = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[3]/div[2]/div[2]/ul/li[4]/div[1]/div[2]/img')
        action(self.driver).move_to_element(wheel_and_stripe_package).click().perform()
        time.sleep(1)
        add = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[4]/div[4]/a')
        action(self.driver).move_to_element(add).click().perform()
        time.sleep(1)
        change_requirement_yes = self.driver.find_element_by_xpath('/html/body/div[21]/div/div/div/div[8]/div[3]/a[2]')
        print("found and selected yes change button")
        action(self.driver).move_to_element(change_requirement_yes).click().perform()
        print("\twheel and stripe package has been selected")

        ford_safe_and_smart_package = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[3]/div[2]/div[3]/ul/li/div[1]/div[2]/img')
        action(self.driver).move_to_element(ford_safe_and_smart_package).click().perform()
        time.sleep(1)
        add = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[4]/div[4]/a')
        action(self.driver).move_to_element(add).click().perform()
        print("\tford safe and smart package has been selected")

        print("\t\t***Test Case C03 has passed***")
        return

    # Selecting all possible wheel type, exterior options, tire type, and rear axle options in the exterior category (Test Case C04)
    def exterior(self):
        exterior_select = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[4]/div[1]/div/div/span[3]')
        print("found exterior select")
        action(self.driver).move_to_element(exterior_select).click().perform()
        print("exterior drop-down has been selected")

#TODO look into this wheel option, keeps breaking
        #sparkle_silver_painted_aluminum_wheel_17inch = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[4]/div[2]/div[1]/ul/li[1]/div[1]/div[3]/img')
        #print("found 17inch sparkle silver painted aluminum wheel")
        #time.sleep(1)
        #action(self.driver).move_to_element(sparkle_silver_painted_aluminum_wheel_17inch).click().perform()
        #time.sleep(1)
        #add = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[4]/div[3]/a')
        #action(self.driver).move_to_element(add).click().perform()
        #change_requirement_yes = self.driver.find_element_by_xpath('/html/body/div[21]/div/div/div/div[8]/div[3]/a[2]')
        #print("found and selected yes change button")
        #action(self.driver).move_to_element(change_requirement_yes).click().perform()

        machined_face_aluminum_wheels_high_gloss_painted_pockets = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[4]/div[2]/div[1]/ul/li[2]/div[1]/div[2]/img')
        print("found 18inch machined face aluminum wheels high gloss painted pockets")
        time.sleep(1)
        action(self.driver).move_to_element(machined_face_aluminum_wheels_high_gloss_painted_pockets).click().perform()
        add = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[4]/div[3]/a')
        action(self.driver).move_to_element(add).click().perform()
        print("\tmachined face aluminum wheels high gloss painted pockets have been selected")

        machined_face_aluminum_wheels_low_gloss_painted_pockets_18inch = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[4]/div[2]/div[1]/ul/li[3]/div[1]/div[2]/img')
        print("found 18inch machined face aluminum wheels low gloss painted pockets")
        action(self.driver).move_to_element(machined_face_aluminum_wheels_low_gloss_painted_pockets_18inch).click().perform()
        time.sleep(1)
        add = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[4]/div[3]/a')
        action(self.driver).move_to_element(add).click().perform()
        print("\t18 inch machined face aluminum wheels low gloss painted pockets have been selected")

        machined_face_aluminum_wheels_dark_tarnish_painted_pockets = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[4]/div[2]/div[1]/ul/li[4]/div[1]/div[2]/img')
        print("found 19 inch machined face aluminum wheels dark tarnished painted pockets")
        action(self.driver).move_to_element(machined_face_aluminum_wheels_dark_tarnish_painted_pockets).click().perform()
        add = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[4]/div[3]/a')
        action(self.driver).move_to_element(add).click().perform()
        print("\tmachined face aluminum wheels dark tarnish painted pockets have been selected")

        ebony_black_painted_aluminum_wheels = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[4]/div[2]/div[1]/ul/li[5]/div[1]/div[2]/img')
        print("found 19 inch x 8.5 inch ebony black painted aluminum wheels")
        action(self.driver).move_to_element(ebony_black_painted_aluminum_wheels).click().perform()
        add = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[4]/div[3]/a')
        action(self.driver).move_to_element(add).click().perform()
        print("\t19 inch x 8.5 inch ebony black painted aluminum wheels have been selected")

        polished_aluminum_wheels = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[4]/div[2]/div[1]/ul/li[6]/div[1]/div[2]/img')
        print("found 19 inch x 8.5 inch polished aluminum wheels")
        action(self.driver).move_to_element(polished_aluminum_wheels).click().perform()
        add = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[4]/div[3]/a')
        action(self.driver).move_to_element(add).click().perform()
        print("\t19 inch x 8.5 inch polished aluminum wheels have been selected")

        luster_painted_nickel_painted_aluminum_wheels = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[4]/div[2]/div[1]/ul/li[7]/div[1]/div[2]/img')
        print("found luster painted nickel painted aluminum wheels")
        action(self.driver).move_to_element(luster_painted_nickel_painted_aluminum_wheels).click().perform()
        add = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[4]/div[3]/a')
        action(self.driver).move_to_element(add).click().perform()
        print("\tluster painted nickel painted aluminum wheels have been selected")

        machined_face_aluminum_wheels_low_gloss_painted_pockets_19inch = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[4]/div[2]/div[1]/ul/li[8]/div[1]/div[2]/img')
        print("found 19inch machined face aluminum wheels low gloss painted pockets")
        action(self.driver).move_to_element(machined_face_aluminum_wheels_low_gloss_painted_pockets_19inch).click().perform()
        time.sleep(1)
        add = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[4]/div[3]/a')
        action(self.driver).move_to_element(add).click().perform()
        print("\t19 inch machined face aluminum wheels low gloss painted pockets have been selected")

        active_valve_performance_exhaust = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[4]/div[2]/div[2]/ul/li[1]/div[1]/div[2]/img')
        print("found active valve performance exhaust")
        action(self.driver).move_to_element(active_valve_performance_exhaust).click().perform()
        time.sleep(1)
        add = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[4]/div[3]/a')
        action(self.driver).move_to_element(add).click().perform()
        print("\tactive valve performance exhaust has been selected")

        adaptive_cruise_control = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[4]/div[2]/div[2]/ul/li[2]/div[1]/div[2]/img')
        print("found adaptive cruise control")
        action(self.driver).move_to_element(adaptive_cruise_control).click().perform()
        time.sleep(1)
        add = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[4]/div[3]/a')
        action(self.driver).move_to_element(add).click().perform()
        print("\tadaptive cruise control has been selected")

        engine_block_heater = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[4]/div[2]/div[2]/ul/li[3]/div[1]/div[2]/img')
        print("found engine block heater")
        action(self.driver).move_to_element(engine_block_heater).click().perform()
        time.sleep(1)
        add = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[4]/div[3]/a')
        action(self.driver).move_to_element(add).click().perform()
        print("\tengine block heater has been selected")

        mini_spare_wheel_and_tire = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[4]/div[2]/div[2]/ul/li[4]/div[2]/div/div[1]/div[2]/div/span[1]')
        print("found mini spare wheel and tire")
        action(self.driver).move_to_element(mini_spare_wheel_and_tire).click().perform()
        time.sleep(1)
        add = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[4]/div[3]/a')
        action(self.driver).move_to_element(add).click().perform()
        print("\tmini spare wheel and tire has been selected")

        rear_spoiler_delete = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[4]/div[2]/div[2]/ul/li[5]/div[1]/div[2]/img')
        print("found reaer spoiler delete")
        action(self.driver).move_to_element(rear_spoiler_delete).click().perform()
        time.sleep(1)
        add = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[4]/div[3]/a')
        action(self.driver).move_to_element(add).click().perform()
        print("\trear spoiler delete has been selected")

        rear_spoiler_blade_decklid = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[4]/div[2]/div[2]/ul/li[6]/div[1]/div[2]/img')
        print("found rear spoiler blade decklid")
        action(self.driver).move_to_element(rear_spoiler_blade_decklid).click().perform()
        time.sleep(1)
        add = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[4]/div[3]/a')
        action(self.driver).move_to_element(add).click().perform()
        print("\trear spoiler blade decklid has been selected")

        remote_start_system = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[4]/div[2]/div[2]/ul/li[6]/div[1]/div[2]/img')
        print("found remote start system")
        action(self.driver).move_to_element(remote_start_system).click().perform()
        time.sleep(1)
        change_requirement_yes = self.driver.find_element_by_xpath('/html/body/div[21]/div/div/div/div[8]/div[3]/a[2]')
        print("found and selected yes change button")
        action(self.driver).move_to_element(change_requirement_yes).click().perform()
        print("\tremote start system has been selected")

        reverse_sensing_system = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[4]/div[2]/div[2]/ul/li[8]/div[1]/div[3]/img')
        print("found reverse sensing system")
        action(self.driver).move_to_element(reverse_sensing_system).click().perform()
        print("reverse sensing system has been selected")
        close = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[3]')
        action(self.driver).move_to_element(close).click().perform()
        print("\treverse sensing system has been selected")

        wheel_locking_kit = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[4]/div[2]/div[2]/ul/li[9]/div[1]/div[3]/img')
        print("found wheel locking kit")
        action(self.driver).move_to_element(wheel_locking_kit).click().perform()
        print("wheel locking kit has been selected")
        close = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[3]')
        action(self.driver).move_to_element(close).click().perform()
        print("\twheel locking kit has been selected")

        w_rated_tires_235 = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[4]/div[2]/div[3]/ul/li[1]/div[2]/div/div[1]/div/div/span[1]')
        print("found 235 tires")
        action(self.driver).move_to_element(w_rated_tires_235).click().perform()
        print("235 tires has been selected")
        close = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[3]')
        action(self.driver).move_to_element(close).click().perform()
        print("\t235 tires has been selected")

        all_season_tires = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[4]/div[2]/div[3]/ul/li[2]/div[2]/div/div[1]/div[2]/div/span')
        print("found all season tires")
        action(self.driver).move_to_element(all_season_tires).click().perform()
        time.sleep(1)
        change_requirement_yes = self.driver.find_element_by_xpath('/html/body/div[21]/div/div/div/div[8]/div[3]/a[2]')
        print("found and selected yes change button")
        action(self.driver).move_to_element(change_requirement_yes).click().perform()
        print("\tall season tires has been selected")

        summer_only_tires = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[4]/div[2]/div[3]/ul/li[3]/div[2]/div/div[1]/div[2]/div/span')
        print("found summer only tires")
        action(self.driver).move_to_element(summer_only_tires).click().perform()
        time.sleep(1)
        change_requirement_yes = self.driver.find_element_by_xpath('/html/body/div[21]/div/div/div/div[8]/div[3]/a[2]')
        print("found and selected yes change button")
        action(self.driver).move_to_element(change_requirement_yes).click().perform()
        print("\tsummer only tires has been selected")

        w_rated_tires_255 = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[4]/div[2]/div[3]/ul/li[4]/div[2]/div/div[1]/div[2]/div/span')
        print("found 255 tires")
        action(self.driver).move_to_element(w_rated_tires_255).click().perform()
        time.sleep(1)
        change_requirement_yes = self.driver.find_element_by_xpath('/html/body/div[21]/div/div/div/div[8]/div[3]/a[2]')
        print("found and selected yes change button")
        action(self.driver).move_to_element(change_requirement_yes).click().perform()
        print("\t255 tires has been selected")

        limited_slip_rear_axle_3o15 = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[4]/div[2]/div[4]/ul/li[1]/div[2]/div/div[1]/div[1]/div/span')
        print("found 3.15 rear axle")
        action(self.driver).move_to_element(limited_slip_rear_axle_3o15).click().perform()
        time.sleep(1)
        change_requirement_yes = self.driver.find_element_by_xpath('/html/body/div[21]/div/div/div/div[8]/div[3]/a[2]')
        print("found and selected yes change button")
        action(self.driver).move_to_element(change_requirement_yes).click().perform()
        print("\t3.15 rear axle has been selected")

        limited_slip_rear_axle_3o31 = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[4]/div[2]/div[4]/ul/li[2]/div[2]/div/div[1]/div[1]/div/span')
        print("found 3.31 rear axle")
        action(self.driver).move_to_element(limited_slip_rear_axle_3o31).click().perform()
        print("\t3.31 rear axle has been selected")

        limited_slip_rear_axle_3o55 = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[4]/div[2]/div[4]/ul/li[3]/div[2]/div/div[1]/div[1]/div/span')
        print("found 3.55 rear axle")
        action(self.driver).move_to_element(limited_slip_rear_axle_3o55).click().perform()
        time.sleep(1)
        change_requirement_yes = self.driver.find_element_by_xpath('/html/body/div[21]/div/div/div/div[8]/div[3]/a[2]')
        print("found and selected yes change button")
        action(self.driver).move_to_element(change_requirement_yes).click().perform()
        print("\t3.55 rear axle has been selected")

        print("\t\t***Test Case C04 has passed***")
        return

    # Selecting all possible cloth, seat type, interior options, radio type, and audio upgrade options in the interior category (Test Case C04)



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
