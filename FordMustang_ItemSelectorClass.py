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
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


import time
import random

#this will iterate through a dictionary by grabbing an xpath and clicking on the button, and it will print out the button that was selected:
def dictionary_iterater(self, dictionary):
    for el in dictionary:
        #button = self.driver.find_element_by_xpath(dictionary[el][0])
        button = wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, (dictionary[el][0]))))
        print("Found " + dictionary[el][1])
        time.sleep(2)
        button.click()
        #action(self.driver).move_to_element(button).click().perform()
        button.click()
        print("\t" + dictionary[el][1] + " has been selected")
        self.change_requirement()

class ItemSelectorClass:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('-incognito')
        self.driver = webdriver.Chrome(r"C:\drivers\chromedriver.exe", options=self.chrome_options)
        self.CurrentModule = "Initialization"
        self.ErrorCount = 0
        self.driver.get("https://www.ford.com/")
        #self.driver.get("https://shop.ford.com/build/mustang/#/config/Config%5B%7CFord%7CMustang%7C2020%7C1%7C1.%7C100A.P8U.....CON.MST.~YZKAA.EBST.LESS.%5D")
        #self.driver.maximize_window()
        #self.wait = WebDriverWait(self.driver, 10)
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

    def change_requirement(self):
        try:
            change_requirement_yes = self.driver.find_element_by_xpath("//a[contains(text(), 'Yes')]")
            action(self.driver).move_to_element(change_requirement_yes).click().perform()
            print("Found and selected Yes button from Change Requirement")
        except:
            print("Change requirement window not found ")

    def random_selection(self):
        id, color = random.choice(list(id.items()))
        color_button = self.driver.find_element_by_xpath(id[id]['id'])
        action(self.driver).move_to_element(color_button).click().perform()
        print("\t" + id[id]['color'] + " has been selected")
        self.change_requirement()

    def open_browser(self):
        self.driver.get("https://www.ford.com/")
        print('Loaded Ford.com main page.')
        try:
            popupFrame = wait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, 'IPerceptionsEmbed')))
            print('Identified Survey Splash Screen. ')
            self.driver.switch_to.frame(popupFrame)
            print('Switched to Survey Page splash screen.')
            no_survey_button = wait(self.driver, 2).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@class='btn btn-no']")))
            no_survey_button.click()
            print('Clicked No button to Survey Splash Screen.')
            self.driver.switch_to.default_content()
        except:
            print('No Survey Splash Screen loaded. Proceeding to next test.')




#Selecting the buttons on the home page to initiate the customization process flow (Test Cases A01 - A06)
    def get_to_car_build(self):
        vehicles_home_page_button = self.driver.find_element_by_class_name('dropdown.dropdown-item')
        print("found vehicles")
        #action(self.driver).move_to_element(vehicles_home_page_button).click().perform()
        vehicles_home_page_button.click()
        print('\tvehicles button on home page has been found and selected')
        print('\t\t***Test A01 has passed***')

        #time.sleep(3)

        cars_home_page_button = wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Cars']")))
        print("found cars")
        #action(self.driver).move_to_element(cars_home_page_button).click().perform()
        cars_home_page_button.click()
        print('\tcars button on home page has been found and selected')
        print('\t\t***Test A02 has passed***')

        #time.sleep(3)


        mustang_button_2020 = wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "2020 Mustang")]')))
        print("found 2020 mustang")
        #action(self.driver).move_to_element(mustang_button_2020).click().perform()
        mustang_button_2020.click()
        print('\t2020 mustang button on home page has been found and selected')
        print('\t\t***Test A03 has passed***')

        #time.sleep(3)

        build_and_price_button = wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Press here for information on 2020 Ford Mustang Build and Price']")))
        print("found build & price")
        build_and_price_button.click()
        print('\tbuild & price button on home page has been found and selected')
        print('\t\t***Test A04 has passed***')

        #time.sleep(3)

        print("looking for zip code field")
        #time.sleep(2)
        select_zip_button = wait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'postal-input')))
        print("found enter zip field")
        action(self.driver).move_to_element(select_zip_button).click().send_keys('60448').perform()
        print('\tzip code field has been found, selected, and has had a zip code entered')

        #time.sleep(2)

        enter_zip_button = wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Enter")]')))
        print("found enter")
        action(self.driver).move_to_element(enter_zip_button).click().perform()
        print('\tzip code enter button has been found and selected')
        print('\t\t***Test A05 has passed***')

        #build_your_own_button = wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Build Your Own")]')))
        #print("found build your own")
        ##time.sleep(2)
        #build_your_own_button.click()
        #print('\tbuild your own button has been found and selected')
        #print('\t\t***Test A06 has passed***')
        return

#Setting up the mustang model to be tested, includes which model and which option of performance (Test Case B01)
    def choose_your_model_convertible(self):
        #time.sleep(2)
        convertible_button = wait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "tech-list-price-ecoboostconvertible")))
        print("found convertible")
        convertible_button.click()
        print('\tconvertible button has been found and selected')

        #time.sleep(2)
#TODO: Come back to this element and see if we can find a less brittle way of grabbing it. This selection method is the best I've found given the way its coded, but I would like to return to it if time allows. - Cheyanne
        convertible_image = wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//img[@src='//build.ford.com/dig/Ford/Mustang/2020/HD-TILE/Image[|Ford|Mustang|2020|1|1.|100A.P8U..PQ..882.~VIRTUALPKGPART_D5HAB_6.~VIRTUALPKGPART_HNAAJ_7.LTS.CON.~VIRTUALPKGPART_AACAA_16.~VIRTUALPKGPART_AB2AA_18.~VIRTUALPKGPART_D17AA_21.~VIRTUALPKGPART_D2YFY_22.SYN.86C.453.64A.43S.MST.891.ANT.LRS.CLO.99H.RWD.44X.EBST.TDP.LESS.12A.13D.14L.14A.58A.2020 P8U FORD.]/EXT/1/vehicle.png']")))
        print("found configure")
        convertible_image.click()
        print('\tconfigure button has been found and selected')
        print('\t\t***Test B01 has passed***')
        return

    #time.sleep(10)

#Selecting all possible paint options in the paint type category (Test Case C01)
    def paint_type(self):
        paint_selection = {
            0: ("//div[contains(text(), 'Grabber Lime')]", 'Grabber Lime'),
            1: ("//div[contains(text(), 'Oxford White')]",  'Oxford White'),
            2: ("//div[contains(text(), 'Velocity Blue')]", 'Velocity Blue'),
            3: ("//div[contains(text(), 'Iconic Silver')]", 'Iconic Silver'),
            4: ("//div[contains(text(), 'Magnetic')]", 'Magnetic'),
            5: ("//div[contains(text(), 'Race Red')]",  'Race Red' ),
            6: ("//div[contains(text(), 'Rapid Red')]",  'Rapid Red' ),
            7: ("//div[contains(text(), 'Kona Blue')]",  'Kona Blue' ),
            8: ("//div[contains(text(), 'Twister Orange')]",  'Twister Orange' )
        }
        dictionary_iterater(self, paint_selection)
        return

#Selecting all possible tape stripe options in the paint type category (Test Case C01)
    def tape_stripe(self):
        tape_stripe_selection = {
            0: ("//div[contains(text(), 'Silver Tape Stripe')]", 'Silver Tape Stripe'),
            1: ("//div[contains(text(), 'Ebony Tape Stripe')]",  'Ebony Tape Stripe'),
            2: ("//div[contains(text(), 'Less Tape Stripe')]", 'Less Tape Stripe'),
        }
        time.sleep(1)
        dictionary_iterater(self, tape_stripe_selection)

        print("\t\tall tape stripes have been selected")
        return

#Selecting all possible racing stripe options in the paint type category (Test Case C01)
    def racing_stripe(self):
        racing_stripe_selection = {
            0:  ("//div[contains(text(), 'Ebony Racing Stripe')]", 'Ebony Tape Stripe'),
            1:  ("//div[contains(text(), 'Less Racing Stripe')]", 'Less Racing Stripe'),
        }
        dictionary_iterater(self, racing_stripe_selection)

        print("\t\tall racing stripes have been selected")
        return

#Selecting all possible paint options in the paint type category (Test Case C01)
    def hood_and_side_stripes(self):
        hood_side_stripe_selection = {
            0:  ("//div[contains(text(), 'Metallic Gray Hood Stripe')]", 'Metallic Gray Hood Stripe'),
            1:  ("//div[contains(text(), 'Silver Hood Stripe')]", 'Silver Hood Stripe'),
            2:  ("//div[contains(text(), 'Ebony Hood Stripe')]", 'Ebony Hood Stripe')
        }
        dictionary_iterater(self, hood_side_stripe_selection)

        print("\t\tall hood and side stripes have been selected")
        print("\t\t\t***Test Case C01 has passed***")
        return

#Selecting all powertrain drop-down arrow to open the powertrain category (Test Case C02)
    def powertrain(self):
        powertrain_select = wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//div[@aria-label='Powertrain']")))
        powertrain_select.click()
        print("powertrain drop-down has been selected")


        return

#Selecting all possible engine options in the powertrain category (Test Case C02)
    def engine(self):
        engine_selection = {
            0:  ("//span[contains(text(), '2.3L High Performance EcoBoost® Engine')]", '2.3L High Performance EcoBoost® Engine'),
            1:  ("//span[contains(text(), '2.3L EcoBoost® Engine')]", '2.3L EcoBoost® Engine')
        }
        dictionary_iterater(self, engine_selection)
        return

#Selecting all possible transmission options in the powertrain category (Test Case C02)
    def transmissions(self):
        transmissions_selection = {
            0: ("//span[contains(text(), '10-Speed SelectShift® Automatic Transmission')]", '10-Speed SelectShift® Automatic Transmission'),
            1: ("//span[contains(text(), '6-Speed Manual Transmission')]", '6-Speed Manual Transmission')
        }
        dictionary_iterater(self, transmissions_selection)

        print("\tAll engines and transmissions have been selected")
        print("\t\t***Test Case C02 has paseed***")
        return

#Selecting the packages drop-down arrow to open the packages category (Test Case C03)
    def packages(self):
        packages_select = wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//div[@aria-label='Packages']")))
        action(self.driver).move_to_element(packages_select).click().perform()
        print("packages drop-down has been selected")
        return

#Selecting all possible equipment group options in the packages category (Test Case C03)
    def equipment_group(self):
        equipment_group_selection = {
            0: ("//span[contains(text(), '101A Equipment Group')]", '101A Equipment Group'),
            1: ("//span[contains(text(), '100A Equipment Group')]", '100A Equipment Group')
        }
        dictionary_iterater(self, equipment_group_selection)
        return
#TODO Consistently running into click intercept errors with this method. Revisit to find a workaround.
#Selecting all possible exterior package options in the packages category (Test Case C03)
    def exterior_package(self):
        exterior_package_selection = {
            0: ("//span[contains(text(), 'Black Accent Package')]", '101A Equipment Group'),
            1: ("//span[contains(text(), '2.3L High Performance Package')]", '2.3L High Performance Package'),
            2: ("//span[contains(text(), 'Wheel & Stripe Package')]", 'Wheel & Stripe Package')
        }
        dictionary_iterater(self, exterior_package_selection)
        return

#Selecting the Ford Safe and Smart package in the packages category (Test Case C03)
    def interior_package(self):
        ford_safe_and_smart_package = wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//img[@src='//assets.forddirect.fordvehicles.com/assets/2019_Ford_Mustang_J1/BP2/BP3TINGPKGTHM/136B520C-8CFA-72C8-5905-E80E5905E80E.jpg']")))
        ford_safe_and_smart_package.click()
        add = wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Add")]')))
        add.click()
        print("\tford safe and smart package has been selected")

        print("\t\tall packages have been selected")
        print("\t\t\t***Test Case C03 has passed***")
        return

#Selecting exterior drop-down arrow to open the exterior category (Test Case C04)
    def exterior(self):
        exterior_select = wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//div[@aria-label='Exterior']")))
        print("found exterior select")
        exterior_select.click()
        print("exterior drop-down has been selected")
        return

#Selecting all possible wheel type options in the exterior category (Test Case C04)
    def wheel_type(self):
        wheel_type_selection = {
            0: ("//span[contains(text(), '18-Inch Machined-Face Aluminum Wheels with High-Gloss Ebony Black-Painted Pockets')]", '18-Inch Machined-Face Aluminum Wheels with High-Gloss Ebony Black-Painted Pockets'),
            1: ("//span[contains(text(), '17-Inch Sparkle Silver-Painted Aluminum Wheels')]", '17-Inch Sparkle Silver-Painted Aluminum Wheels'),
            2: ("//span[contains(text(), '18-Inch Machined-Face Aluminum Wheels with Low-Gloss Ebony Black-Painted Pockets')]", '18-Inch Machined-Face Aluminum Wheels with Low-Gloss Ebony Black-Painted Pockets'),
            3: ("//span[contains(text(), '19-Inch Machined-Face Aluminum Wheels with Dark Tarnish-Painted Pockets')]", '19-Inch Machined-Face Aluminum Wheels with Dark Tarnish-Painted Pockets'),
            4: ("//span[contains(text(), '19-Inch x 8.5-Inch Ebony Black-Painted Aluminum Wheels')]", '19-Inch x 8.5-Inch Ebony Black-Painted Aluminum Wheels'),
            5: ("//span[contains(text(), '19-Inch x 8.5-Inch Polished Aluminum Wheels')]", '19-Inch x 8.5-Inch Polished Aluminum Wheels'),
            6: ("//span[contains(text(), '19-Inch x 9-Inch Luster Nickel-painted Forged Aluminum Wheels')]", '19-Inch x 9-Inch Luster Nickel-painted Forged Aluminum Wheels'),
            7: ("//span[contains(text(), '19-Inch x 9-Inch Machined-Face Aluminum Wheels with Low-Gloss Ebony Black-Painted Pockets')]", '19-Inch x 9-Inch Machined-Face Aluminum Wheels with Low-Gloss Ebony Black-Painted Pockets')
        }
        dictionary_iterater(self, wheel_type_selection)

        print("\tall wheel types have been selected")
        return

#Selecting all possible exterior options options in the exterior category (Test Case C04)
    def exterior_options(self):
        exterior_options_selection = {
            0: ("//span[contains(text(), 'Active Valve Performance Exhaust')]", 'Active Valve Performance Exhaust'),
            1: ("//span[contains(text(), 'Adaptive Cruise Control')]", 'Adaptive Cruise Control'),
            2: ("//span[contains(text(), 'Engine Block Heater')]", 'Engine Block Heater'),
            3: ("//span[contains(text(), 'Mini Spare Wheel and Tire')]", 'Mini Spare Wheel and Tire'),
            4: ("//span[contains(text(), 'Rear Spoiler Delete')]", 'Rear Spoiler Delete'),
            5: ("//span[contains(text(), 'Rear Spoiler – Blade Decklid')]", 'Rear Spoiler – Blade Decklid'),
            6: ("//span[contains(text(), 'Remote Start System')]", 'Remote Start System'),
        }
        dictionary_iterater(self, exterior_options_selection)
        print("\tall exterior options have been selected")

        return

#Selecting all possible tire type options in the exterior category (Test Case C04)
    def tire_type(self):
        tire_type_selection = {
            0: ("//span[contains(text(), '235/55R17 BSW All-Season (A/S) Tires')]", '235/55R17 BSW All-Season (A/S) Tires'),
            1: ( "//span[contains(text(), '235/50R18 W-Rated Tires')]", '235/50R18 W-Rated Tires'),
            2: ( "//span[contains(text(), '255/40R19 Summer-Only Tires')]", '255/40R19 Summer-Only Tires'),
            3: ( "//span[contains(text(), '255/40R19 W-Rated Tires')]", '255/40R19 W-Rated Tires')
        }
        dictionary_iterater(self, tire_type_selection)
        print("\tall tire types have been selected")
        return

#Selecting all possible rear axle options in the exterior category (Test Case C04)
    def rear_axle_ratios(self):
        rear_axle_selection = {
            0: ("//span[contains(text(), '3.15 Limited Slip Rear Axle')]", '3.15 Limited Slip Rear Axle'),
            1: ("//span[contains(text(), '3.31 Limited Slip Rear Axle')]", '3.31 Limited Slip Rear Axle'),
            2: ("//span[contains(text(), '3.55 Limited Slip Rear Axle')]", '3.55 Limited Slip Rear Axle')
        }
        dictionary_iterater(self, rear_axle_selection)

        print("\tall tire types have been selected")
        print("\t\t***Test Case C04 has passed***")
        return

#Selecting interior drop-down arrow to open the interior category (Test Case C05)
    def interior(self):
        interior_select = wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//div[@aria-label='Interior']")))
        print("found interior select")
        action(self.driver).move_to_element(interior_select).click().perform()
        print("interior drop-down has been selected")
        return

#Selecting all possible cloth options in the interior category (Test Case C05)
    def cloth(self):
        ceramic = wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//div[@aria-label='Ceramic ']")))
        print("found ceramic cloth")
        action(self.driver).move_to_element(ceramic).click().perform()
        print("ceramic cloth has been selected")

        ebony = wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//div[@aria-label='Ebony ']")))
        print("found ebony cloth")
        action(self.driver).move_to_element(ebony).click().perform()
        print("ebony cloth has been selected")
        return

    #def seat_type(self):

#Selecting all possible interior options options in the interior category (Test Case C05)
    def interior_options(self):
        rear_axle_selection = {
            0: ("//span[contains(text(), '\"Silver Arrow\" Aluminum Instrument Panel Finish')]", '\"Silver Arrow\" Aluminum Instrument Panel Finish'),
            1: ("//span[contains(text(), 'Adaptive Cruise Control')]", 'Adaptive Cruise Control'),
            2: ("//span[contains(text(), 'Premium Floor Liners Front and Rear')]", 'Premium Floor Liners Front and Rear')
        }
        dictionary_iterater(self, rear_axle_selection)

        print("\tall interior options have been selected")
        return

#Selecting all possible radio type options options in the interior category (Test Case C05)
    def radio_type(self):
        radio_selection = {
            0: ("//span[contains(text(), 'AM/FM Stereo with MP3 Capability and Six (6) Speakers')]", 'AM/FM Stereo with MP3 Capability and Six (6) Speakers'),
            1: ("//span[contains(text(), 'Nine (9) Speaker Sound System with Amplifier')]", 'Nine (9) Speaker Sound System with Amplifier')
        }
        dictionary_iterater(self, radio_selection)
        print("\tall radio types have been selected")
        return

    # Selecting all possible audio upgrade options options in the interior category (Test Case C05)
    def audio_upgrade(self):
        audio_upgrade_selection = {
            0: ("//span[contains(text(), 'SiriusXM® Radio')]", 'SiriusXM® Radio'),
            1: ("//span[contains(text(), 'SYNC®')]", 'SYNC®'),
            2: ("//span[contains(text(), 'SYNC® 3')]", '2SYNC® 3'),
            3: ("//span[contains(text(), 'Voice-Activated Touchscreen Navigation System with SiriusXM® Traffic and Travel Link')]", 'Voice-Activated Touchscreen Navigation System with SiriusXM® Traffic and Travel Link')
        }
        dictionary_iterater(self, audio_upgrade_selection)

        print("\tall audio upgrade options have been selected")
        print("\t\t\t***Test Case C05 has passed***")
        return
#TODO element selector not working
#Selecting the Summary button after Test Cases C01 - C05 have been completed
    def summary(self):
        time.sleep(1)
        summary_button = wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//div[@aria-label='Show Summary']")))
        print("found summary button")
        #time.sleep(1)
        summary_button.click()
        print("summary button has been selected")

        '''summary_close = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[1]')
        print("found close button")
        action(self.driver).move_to_element(summary_close).click().perform()
        print("close button has been selected")'''

#Selecting and closing out of 'Speacial Offers' upon selecting the Summary button (TC D01.1) after Test Cases C01 - C05 have been completed
    def special_offers(self):
        special_offers = wait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Special Offers')))
        print("found special offers")
        time.sleep(1)
        special_offers.click()
        print("special offers has been selected")

        time.sleep(1)

        special_offers_close = wait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".iframe-modal-close > .close-txt")))
        print("found special offers close button")
        special_offers_close.click()
        print("special offers close button has been selected")

#Selecting and closing out of 'Look Up Trade-In-Value' upon selecting the Summary button (TC D01.1) after Test Cases C01 - C05 have been completed
    def trade_in_value(self):
        look_up_trade_in_value = wait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Look up Trade-In-Value')))
        print("found look up trade-in-value")
        look_up_trade_in_value.click()
        print("look up trade-in-value has been selected")

        time.sleep(1)

        look_up_trade_in_value_close = wait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".iframe-modal-close > .close-txt")))
        look_up_trade_in_value_close.click()
        print("look up trade-in-value Close button has been selected")

#Selecting 'Search Inventory' upon selecting the Summary button (TC D01.1) after Test Cases C01 - C05 have been completed
    def search_inventory(self):
        search_inventory = wait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(),'Search Inventory')])[2]")))
        print("found search inventory")
        time.sleep(4)
        search_inventory.click()
        print("search inventory button has been selected")

#Test Case Category E, make sure to set test case category A in the test script as a precondition (TC D01.1) after Test Cases C01 - C05 have been completed
    def let_us_find_it_for_you_select(self):
        time.sleep(5)
        let_us_find_it_for_you_button = self.driver.find_element_by_xpath("/html/body/div[9]/div[7]/div/div/div/div/div/div[2]/div[2]/a/div/img")
        print("found let us find it for you button")
        let_us_find_it_for_you_button.click()
        print("let us find it for you button has been selected")

#TODO clean up full xpath
#This is a list of all of the possible 2020 Mustang models. Program should loop through and select all of the options in the list
    def let_us_find_it_for_you_your_model(self):
        your_model_selection = {
            0: ("(//div[@role='checkbox'][@aria-label='EcoBoost® Fastback'])", 'EcoBoost® Fastback'),
            1: ('EcoBoost® Premium Fastback'),
            2: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[1]/div/span', 'EcoBoost® Convertible'),
            3: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[1]/div[2]/div/div[4]/div[1]/div[1]/div[1]/div/span', 'GT Fastback'),
            4: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[1]/div[2]/div/div[5]/div[1]/div[1]/div[1]/div/span', 'EcoBoost® Premium Convertible'),
            5: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[1]/div[2]/div/div[5]/div[1]/div[1]/div[1]/div/span', 'GT Premium Fastback'),
            6: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[1]/div[2]/div/div[7]/div[1]/div[1]/div[1]/div/span', 'GT Premium Convertible'),
            7: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[1]/div[2]/div/div[8]/div[1]/div[1]/div[1]/div/span', 'BULLITT™'),
            8: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[1]/div[2]/div/div[9]/div[1]/div[1]/div[1]/div/span', 'Shelby GT350®'),
            9: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[1]/div[2]/div/div[10]/div[1]/div[1]/div[1]/div/span', 'Shelby GT500®'),
            10: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[1]/div[2]/div/div[11]/div[1]/div[1]/div[1]/div/span', 'Shelby® GT350R')
        }
        dictionary_iterater(self, your_model_selection)
        print("all models have been selected")
        return

#This is a list of all of the possible exterior colors for the mustang. Program should loop through and select all of the options in the list
    def let_us_find_it_for_you_exterior_colors(self):
        exterior_colors_button = self.driver.find_element_by_xpath('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[2]')
        print("found exterior colors button")
        action(self.driver).move_to_element(exterior_colors_button).click().perform()
        print("exterior colors button has been selected")

        exterior_colors_selection = {
            0: ("//div[contains(text(), 'Shadow Black')]", 'Shadow Black'),
            1: ("//div[contains(text(), 'Grabber Lime')]",  'Grabber Lime'),
            2: ("//div[contains(text(), 'Oxford White')]", 'Oxford White'),
            3: ("//div[contains(text(), 'Dark Highland Green')]", 'Dark Highland Green'),
            4: ("//div[contains(text(), 'Velocity Blue')]", 'Velocity Blue'),
            5: ("//div[contains(text(), 'Iconic Silver')]",  'Iconic Silver'),
            6: ("//div[contains(text(), 'Magnetic')]",  'Magnetic'),
            7: ("//div[contains(text(), 'Race Red')]",  'Race Red'),
            8: ("//div[contains(text(), 'Rapid Red')]",  'Rapid Red'),
            9: ("//div[contains(text(), 'Ford Performance Blue')]", 'Ford Performance Blue'),
            10: ("//div[contains(text(), 'Kona Blue')]", 'Kona Blue'),
            11: ("//div[contains(text(), 'Twister Orange')]", 'Twister Orange'),
            12: ("//div[contains(text(), 'Shadow Black')]", 'Shadow Black')
        }
        dictionary_iterater(self, exterior_colors_selection)
        return

#This is a list of all of the possible interior colors for the mustang. Program should loop through and select all of the options in the list
    def let_us_find_it_for_you_interior_colors(self):
        interior_colors_button = self.driver.find_element_by_xpath('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[3]')
        print("found interior colors button")
        action(self.driver).move_to_element(interior_colors_button).click().perform()
        print("interior colors button has been selected")

        interior_colors_selection = {
            0: ("//div[contains(text(), 'Ebony')]", 'Ebony'),
            1: ("//div[contains(text(), 'Ceramic')]",  'Ceramic'),
            2: ("//div[contains(text(), 'Tan')]", 'Tan'),
            3: ("//div[contains(text(), 'Showstopper Red')]", 'Showstopper Red'),
            4: ("//div[contains(text(), 'Midnight Blue w/Grabber Blue Stitch')]", 'Midnight Blue w/Grabber Blue Stitch'),
            5: ("//div[contains(text(), 'Ebony with Green Stitch')]",  'Ebony with Green Stitch'),
            6: ("//div[contains(text(), 'Ebony w/Smoke Gray Accents')]",  'Ebony w/Smoke Gray Accents'),
            7: ("//div[contains(text(), 'Ebony w/Red Accents')]",  'Ebony w/Red Accents')
        }
        dictionary_iterater(self, interior_colors_selection)
        return

#This is a list of all of the possible preferences for the mustang. Program should loop through and select all of the options in the list
    def let_us_find_it_for_you_your_preferences(self):
        your_preferences_button = self.driver.find_element_by_xpath('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[4]')
        print("found your preferences button")
        action(self.driver).move_to_element(your_preferences_button).click().perform()
        print("your preferences button has been selected")

        your_preferences_selection = {
            0: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[4]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div/span', '2.3L EcoBoost® Engine'),
            1: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[4]/div[2]/div[1]/div[3]/div/div[1]/div[1]/div/span', '5.0L Ti-VCT V8 Engine'),
            2: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[4]/div[2]/div[1]/div[4]/div/div[1]/div[1]/div/span', '2.3L High Performance EcoBoost® Engine'),
            3: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[4]/div[2]/div[1]/div[5]/div/div[1]/div[1]/div/span', '5.2L Ti-VCT V8 with Flat Plane Crank Engine'),
            4: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[4]/div[2]/div[1]/div[6]/div/div[1]/div[1]/div/span', '5.0L Ti-VCT V8 Engine (BULLITT™)'),
            5: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[4]/div[2]/div[1]/div[7]/div/div[1]/div[1]/div/span', '5.2L Supercharged Cross Plane Crank V8'),
            6: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[4]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/span', 'TREMEC 7-Speed Dual Clutch (DCT)'),
            7: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[4]/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/span', '10-Speed SelectShift® Automatic Transmission'),
            8: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[4]/div[2]/div[2]/div[4]/div/div[1]/div[1]/div/span', '6-Speed Manual Transmission'),
            9: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[4]/div[2]/div[2]/div[5]/div/div[1]/div[1]/div/span', '6-Speed Manual Transmission')
        }
        dictionary_iterater(self, your_preferences_selection)
        print("all preferences have been selected")
        return

#This is a list of all of the possible optional upgrades for the mustang. Program should loop through and select all of the options in the list
    def let_us_find_it_for_you_optional_upgrades(self):
        optional_upgrades_button = self.driver.find_element_by_xpath('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[5]')
        print("found optional upgrades button")
        action(self.driver).move_to_element(optional_upgrades_button).click().perform()
        print("optional upgrades button has been selected")

        optional_upgrades_selection = {
            0: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[5]/div[2]/div[1]/div[2]/div[1]/div[1]/div/span', 'SYNC® 3'),
            1: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[5]/div[2]/div[2]/div[2]/div[1]/div[1]/div/span', 'EcoBoost Handling Package'),
            2: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[5]/div[2]/div[3]/div[2]/div[1]/div[1]/div/span', 'Wheel & Stripe Package'),
            3: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[5]/div[2]/div[4]/div[2]/div[1]/div[1]/div/span', 'Ford Safe and Smart™ Package'),
            4: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[5]/div[2]/div[5]/div[2]/div[1]/div[1]/div/span', '2.3L High Performance Package'),
            5: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[5]/div[2]/div[6]/div[2]/div[1]/div[1]/div/span', 'Black Accent Package')
        }
        dictionary_iterater(self, optional_upgrades_selection)
        print("all optional upgrades have been selected")
        return

#This is selecting the continue button (TC F01), done after Test Case D01, to begin the Search Inventory functionality
    def _continue_(self):
        time.sleep(2)
        continue_button = self.driver.find_element_by_xpath("//div[@class='search-inventory']//button[contains(text(), 'Continue')]")
        print("found continue button")
        action(self.driver).move_to_element(continue_button).click().perform()
        print("continue button has been selected")
        return

#Upon entering a distance, ford will return a list of dealers within the designated mile radius the user selects
    def change_dealer_mileage(self):
        change_mileage = self.driver.find_element_by_xpath("//div[@id='dealer-popdown']")
        print("found dealer mileage drop-down")
        action(self.driver).move_to_element(change_mileage).click().perform()
        print("dealer mileage drop-down has been selected")

#TODO pick a random mile radius
#This is selecting the 10 mile radius option
        _10_miles_select = self.driver.find_element_by_xpath("//ul[@role='group']")   # get parent elemement of unordered list

        mileage_list = _10_miles_select.find_elements_by_xpath("//li[@role='presentation']")  # get all elements from the dropdown list

        print("found 10 miles")
        action(self.driver).move_to_element(mileage_list[0]).click().perform()  # the 0 index of the list is the 10 mile element, click on it
        print("10 miles has been selected")
        return

#Upon entering a zip code, ford will return the dealers in the area, depending on what was selected for the dealer mileage distance (TC F02)
    def change_dealer_zipcode(self):
        change_dealer_x_button = self.driver.find_element_by_xpath("//a[@aria-label='Clear Field']")
        print("found x button in zip field")
        action(self.driver).move_to_element(change_dealer_x_button).click().perform()
        print("x button in zip field has been selected")

        enter_zip_code = self.driver.find_element_by_xpath("//input[@name='Postal Code']")
        print("found zip code field on search inventory page")
        action(self.driver).move_to_element(enter_zip_code).click().send_keys('60448').perform()
        print("zip code has been re-entered")
        return

#This is the list of dealers that have been returned after entering a mileage and zip code (TC F02)
    def select_from_list_of_dealers(self):

        # get the parent element holding a list of the dealers
        parent = self.driver.find_element_by_class_name("dealers-list.checkbox-options")

        # get li elements and store inside of a list
        dealer_list = parent.find_elements_by_xpath("//li[@role='Presentation']")

        # the following can be turned into a loop
        # 0 - currie motors, 1 - joe rizza, 2 - sutton ford
        print("found currie motors")
        action(self.driver).move_to_element(dealer_list[0]).click().perform()
        print("currie motors has been selected")

        print("found joe rizza")
        action(self.driver).move_to_element(dealer_list[1]).click().perform()
        print("joe rizza has been selected")

        print("found sutton ford")
        action(self.driver).move_to_element(dealer_list[2]).click().perform()
        print("sutton ford has been selected")

        print("all dealers have been selected")
        return

#This is a hard coded list of all of the possible body styles for the mustang. Program should procedurally go through and select all of the options in the list (TC F02)
    def body_style(self):

        parent = self.driver.find_element_by_xpath("//ul[@class='checkbox-options']") # get parent element

        body_style_list = parent.find_elements_by_xpath("//li[@role='Presentation']")
        print("found convertible")
        action(self.driver).move_to_element(body_style_list[0]).click().perform()
        print("convertible has been unselected")

        parent = self.driver.find_element_by_xpath("//ul[@class='checkbox-options']")  # get parent element

        body_style_list = parent.find_elements_by_xpath("//li[@role='Presentation']")
        print("found convertible")
        action(self.driver).move_to_element(body_style_list[0]).click().perform()
        print("convertible has been selected")

        parent = self.driver.find_element_by_xpath("//ul[@class='checkbox-options']")  # get parent element

        body_style_list = parent.find_elements_by_xpath("//li[@role='Presentation']")
        print("found couple/fastback")
        time.sleep(3)
        body_style_list[1].click()
        print("couple/fastback has been selected")

        print("all body styles have been selected")
        return

#This is a hard coded list of all of the possible models for the mustang. Program should procedurally go through and select all of the options in the list (TC F02)
    def select_model(self):
        time.sleep(5)

        unselect_ecoboost = self.driver.find_element_by_xpath("//span[@role='checkbox']//span[@contains(text(), 'EcoBoost')]")
        print("found ecoboost")
        action(self.driver).move_to_element(unselect_ecoboost).click().perform()
        print("ecoboost has been unselected")

        select_ecoboost = wait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'checkbox-modeltrim-0')))
        print("found ecoboost")
        time.sleep(3)
        select_ecoboost.click()
        print("ecoboost has been selected")

        time.sleep(10)

        select_ecoboost_100A = self.driver.find_element_by_xpath("//span[@role='checkbox']//span[@contains(text(), '100A')]")
        print("found ecoboost 100a")
        action(self.driver).move_to_element(select_ecoboost_100A).click().perform()
        print("ecoboost 100a has been selected")

        time.sleep(5)

        select_ecoboost_101A = self.driver.find_element_by_xpath("//span[@role='checkbox']//span[@contains(text(), '101A')]")
        print("found ecoboost 101a")
        action(self.driver).move_to_element(select_ecoboost_101A).click().perform()
        print("ecoboost 101a has been selected")

        time.sleep(5)

        select_ecoboost_premium = self.driver.find_element_by_xpath("//span[@role='checkbox']//span[@contains(text(), 'EcoBoost® Premium')]")
        print("found ecoboost premium")
        action(self.driver).move_to_element(select_ecoboost_premium).click().perform()
        print("ecoboost premium has been selected")

        time.sleep(5)

        select_gt = self.driver.find_element_by_xpath("//span[@role='checkbox']//span[@text='GT']")
        print("found GT")
        action(self.driver).move_to_element(select_gt).click().perform()
        print("GT has been selected")

        time.sleep(5)

        select_gt_premium = self.driver.find_element_by_xpath("//span[@role='checkbox']//span[@text='GT Premium']")
        print("found GT premium")
        action(self.driver).move_to_element(select_gt_premium).click().perform()
        print("GT premium has been selected")

        time.sleep(5)

        select_bullitt = self.driver.find_element_by_xpath("//span[@role='checkbox']//span[@contains(text(), 'BULLITT')]")
        print("found bullitt")
        action(self.driver).move_to_element(select_bullitt).click().perform()
        print("bullitt has been selected")

        time.sleep(5)

        select_shelby_gt350 = self.driver.find_element_by_xpath("//span[@role='checkbox']//span[@contains(text(), 'GT350')]")
        print("found shelby gt350")
        action(self.driver).move_to_element(select_shelby_gt350).click().perform()
        print("shelby gt350 has been selected")

        time.sleep(5)

        select_shelby_gt500 = self.driver.find_element_by_xpath("//span[@role='checkbox']//span[@contains(text(), 'GT500')]")
        print("found shelby gt500")
        action(self.driver).move_to_element(select_shelby_gt500).click().perform()
        print("shelby gt500 has been selected")

        time.sleep(5)

        select_shelby_gt350r = self.driver.find_element_by_xpath("//span[@role='checkbox']//span[@contains(text(), 'Shelby®')]")
        print("found shelby gt350r")
        action(self.driver).move_to_element(select_shelby_gt350r).click().perform()
        print("shelby gt350r has been selected")

        print("all models have been selected")
        return

#This is a hard coded list of all of the possible model years for the mustang. Program should procedurally go through and select all of the options in the list (TC F02)
    def year(self):
        select_2019 = self.driver.find_element_by_xpath("//span[@id='check-year-0']")
        print("found 2019")
        action(self.driver).move_to_element(select_2019).click().perform()
        print("2019 has been selected")

        time.sleep(5)

        unselect_2020 = self.driver.find_element_by_xpath("//span[@id='check-year-1]")
        print("found 2020")
        action(self.driver).move_to_element(unselect_2020).click().perform()
        print("2020 has been unselected")

        select_2020 = self.driver.find_element_by_xpath("//span[@id='check-year-1]")
        print("found 2020")
        action(self.driver).move_to_element(select_2020).click().perform()
        print("2020 has been selected")

        print("all years have been selected")
        return

#This is a list of all of the possible power and handling optoins for the mustang. Program should loop through and select all of the options in the list (TC F03)
    def power_and_handling(self):
        power_and_handling_select = self.driver.find_element_by_xpath("//div[@data-ng-switch-when='power_handling']")
        print("found power and handling drop-down")
        action(self.driver).move_to_element(power_and_handling_select).click().perform()
        print("power and handling drop-down has been selected")

        power_and_handling_select = {
            0: ("//ul[@aria-labelledby='filter-title-power-0']//span[@id='check-power-0']", '2.3L EcoBoost'),
            1: ("//ul[@aria-labelledby='filter-title-power-0']//span[@id='check-power-1']", '5.0L Ti-VCT V8'),
            2: ("//ul[@aria-labelledby='filter-title-power-0']//span[@id='check-power-2']", '5.0Litre Ti-VCT V8'),
            3: ("//ul[@aria-labelledby='filter-title-power-0']//span[@id='check-power-3']", '5.2L Ti-VCT V8'),
            4: ("//ul[@aria-labelledby='filter-title-power-0']//span[@id='check-power-4']", '2.3L High Performance Eco Boost'),
            5: ("//ul[@aria-labelledby='filter-title-power-0']//span[@id='check-power-5']", '5.2L Supercharged Cross Plane Crank V8'),
            6: ("//ul[@aria-labelledby='filter-title-power-1']//span[@id='check-power-0']", 'SelectShift Automatic'),
            7: ("//ul[@aria-labelledby='filter-title-power-1']//span[@id='check-power-1']", 'Manual'),
            8: ("//ul[@aria-labelledby='filter-title-power-2']//span[@id='check-power-0']", 'Rear-Wheel Drive')
        }
        dictionary_iterater(self, power_and_handling_select)
        print("all power and handling selections have been selected")
        return

#This is a list of all of the possible exterior colors for the mustang. Program should loop through and select all of the options in the list (TC F04)
    def exterior_color(self):
        exterior_color_select = self.driver.find_element_by_xpath("//div[@data-ng-switch-when='exterior_color']")
        print("found exterior color drop-down")
        action(self.driver).move_to_element(exterior_color_select).click().perform()
        print("exterior color drop-down has been selected")

        exterior_color_selection = {
            0: ("//ul[@aria-label='Exterior Color']//li[@data-popover='Dark Highland Green']", 'Dark Highland Green'),
            1: ("//ul[@aria-label='Exterior Color']//li[@data-popover='Grabber Lime']", 'Grabber Lime'),
            2: ("//ul[@aria-label='Exterior Color']//li[@data-popover='Iconic Silver']", 'Iconic Silver'),
            3: ("//ul[@aria-label='Exterior Color']//li[@data-popover='Ingot Silver']", 'Ingot Silver'),
            4: ("//ul[@aria-label='Exterior Color']//li[@data-popover='Kona Blue']", 'Kona Blue'),
            5: ("//ul[@aria-label='Exterior Color']//li[@data-popover='Magnetic']", 'Magnetic'),
            6: ("//ul[@aria-label='Exterior Color']//li[@data-popover='Need for Green']", 'Need for Green'),
            7: ("//ul[@aria-label='Exterior Color']//li[@data-popover='Orange Fury']", 'Orange Fury'),
            8: ("//ul[@aria-label='Exterior Color']//li[@data-popover='Oxford White']", 'Oxford White'),
            9: ("//ul[@aria-label='Exterior Color']//li[@data-popover='Ford Performance Blue']", 'Ford Performance Blue'),
            10: ("//ul[@aria-label='Exterior Color']//li[@data-popover='Race Red']", 'Race Red'),
            11: ("//ul[@aria-label='Exterior Color']//li[@data-popover='Rapid Red']", 'Rapid Red'),
            12: ("//ul[@aria-label='Exterior Color']//li[@data-popover='Ruby Red']", 'Ruby Red'),
            13: ("//ul[@aria-label='Exterior Color']//li[@data-popover='Shadow Black']", 'Shadow BLack'),
            14: ("//ul[@aria-label='Exterior Color']//li[@data-popover='Twister Orange']", 'Twister Orange'),
            15: ("//ul[@aria-label='Exterior Color']//li[@data-popover='Velocity Blue']", 'Velocity Blue')
        }
        dictionary_iterater(self, exterior_color_selection)
        print("all exterior color selections have been selected")
        return

#This is a list of all of the possible interior colors for the mustang. Program should loop through and select all of the options in the list (TC F05)
    def interior_color(self):
        interior_color_select = self.driver.find_element_by_xpath("//div[@data-ng-switch-when='interior_color']")
        print("found interior color drop-down")
        action(self.driver).move_to_element(interior_color_select).click().perform()
        print("interior color drop-down has been selected")

        interior_color_selection = {
            0: ("//ul[@aria-labelledby='filter-title-interior-color-0']//li[@data-popover='Ceramnic']", 'Cloth - Ceramic'),
            1: ("//ul[@aria-labelledby='filter-title-interior-color-0']//li[@data-popover='Ebony']", 'Cloth - Ebony'),
            2: ("//ul[@aria-labelledby='filter-title-interior-color-1']//li[@data-popover='Ceramnic']", 'Leather - Ceramic'),
            3: ("//ul[@aria-labelledby='filter-title-interior-color-1']//li[@data-popover='Ebony']", 'Leather - Ebony'),
            4: ("//ul[@aria-labelledby='filter-title-interior-color-1']//li[@data-popover='Ebony with Green Stitch / Ebony/Green Stitch']", 'Leather - Ebony with Green Stitch'),
            5: ("//ul[@aria-labelledby='filter-title-interior-color-1']//li[@data-popover='Tan']", 'Leather - Tan'),
            6: ("//ul[@aria-labelledby='filter-title-interior-color-2']//li[@data-popover='Ebony']", 'Leather with Alcantra Inserts - Ebony'),
            7: ("//ul[@aria-labelledby='filter-title-interior-color-3']//li[@data-popover='Ebony']", 'Leather with Miko Inserts - Ebony'),
            8: ("//ul[@aria-labelledby='filter-title-interior-color-3']//li[@data-popover='Ebony']", 'Leather with Miko Inserts - Ebony with Red Stitch'),
            9: ("//ul[@aria-labelledby='filter-title-interior-color-3']//li[@data-popover='Ebony/Smoke Gray Stitch']", 'Leather with Miko Inserts - Ebony/Smoke Gray Stitch'),
            10: ("//ul[@aria-labelledby='filter-title-interior-color-4']//li[@data-popover='Ebony']", 'Premier Leather - Ebony'),
            11: ("//ul[@aria-labelledby='filter-title-interior-color-4']//li[@data-popover='Midnight Blue with Grabber Blue Stitch / Midnight Blue/Grabber Blue Stitch']", 'Premier Leather - Midnight Blue with Grabber Blue Stitch'),
            12: ("//ul[@aria-labelledby='filter-title-interior-color-4']//li[@data-popover='Showstopper Red']", 'Premier Leather - Showstopper Red'),
            13: ("//ul[@aria-labelledby='filter-title-interior-color-5']//li[@data-popover='Ebony']", 'RECARO Cloth - Ebony'),
            14: ("//ul[@aria-labelledby='filter-title-interior-color-6']//li[@data-popover='Ebony with Red Accents / Ebony']", 'RECARO Cloth with Miko Inserts - Ebony'),
            15: ("//ul[@aria-labelledby='filter-title-interior-color-6']//li[@data-popover='Ebony/Red Accents']", 'RECARO Cloth with Miko Inserts - Ebony with Red Accents'),
            16: ("//ul[@aria-labelledby='filter-title-interior-color-7']//li[@data-popover='Ebony']", 'RECARO Leather - Ebony'),
            17: ("//ul[@aria-labelledby='filter-title-interior-color-7']//li[@data-popover='Ebony with Green Stitch / Ebony/Green Stitch']", 'RECARO Leather - Ebony with Green Stitch'),
            18: ("//ul[@aria-labelledby='filter-title-interior-color-7']//li[@data-popover='Ebony/Smoke Gray Accents']", 'RECARO Leather - Ebony/Smoke Gray Accents'),
            19: ("//ul[@aria-labelledby='filter-title-interior-color-8']//li[@data-popover='Ebony']", 'RECARO Premier Leather - Ebony'),
            20: ("//ul[@aria-labelledby='filter-title-interior-color-8']//li[@data-popover='Midnight Blue with Grabber Blue Stitch / Midnight Blue/Grabber Blue Stitch']",  'RECARO Premier Leather - Midnight Blue with Grabber Blue Stitch'),
            21: ("//ul[@aria-labelledby='filter-title-interior-color-8']//li[@data-popover='Showstopper Red']", 'RECARO Premier Leather - Showstopper Red')
        }
        dictionary_iterater(self, interior_color_selection)
        print("all interior color selections have been selected")
        return

#This is a list of all of the possible exterior features for the mustang. Program should loop through and select all of the options in the list (TC F06)
    def exterior_features(self):
        exterior_features_select = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/div/section/div/div[1]/div/div[4]/div[1]/div[2]/div[7]/div/div/div/div[1]')
        print("found exterior features drop-down")
        action(self.driver).move_to_element(exterior_features_select).click().perform()
        print("exterior features drop-down has been selected")

        exterior_features_selection = {
            0: ('/html/body/div[3]/div/div[1]/div/div/div/section/div/div[1]/div/div[4]/div[1]/div[2]/div[7]/div/div/div/div[2]/div/fieldset/ul/li/ul/li[1]/span/span[1]', '17" Wheels'),
            1: ('/html/body/div[3]/div/div[1]/div/div/div/section/div/div[1]/div/div[4]/div[1]/div[2]/div[7]/div/div/div/div[2]/div/fieldset/ul/li/ul/li[2]/span/span[1]', '18" Wheels'),
            2: ('/html/body/div[3]/div/div[1]/div/div/div/section/div/div[1]/div/div[4]/div[1]/div[2]/div[7]/div/div/div/div[2]/div/fieldset/ul/li/ul/li[3]/span/span[1]', '19" Wheels'),
            3: ('/html/body/div[3]/div/div[1]/div/div/div/section/div/div[1]/div/div[4]/div[1]/div[2]/div[7]/div/div/div/div[2]/div/fieldset/ul/li/ul/li[3]/span/span[1]', '19.5" Wheels'),
            4: ('/html/body/div[3]/div/div[1]/div/div/div/section/div/div[1]/div/div[4]/div[1]/div[2]/div[7]/div/div/div/div[2]/div/fieldset/ul/li/ul/li[5]/span/span[1]', '20" Wheels'),
        }
        dictionary_iterater(self, exterior_features_selection)
        print("all exterior features selections have been selected")
        return
 #Selecting the "Let Us Find Your Vehicle" button at the bottom of the Search Inventory Page (TC F07)
    def let_us_find_your_vehicle(self):
        let_us_find_your_vehicle_button = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/div/section/div/div[1]/div/div[4]/div[1]/div[2]/div[12]/a')
        print("found let us find your vehicle button")
        action(self.driver).move_to_element(let_us_find_your_vehicle_button).click().perform()
        print("let us find your vehicle button has been selected")
        return

#Selecting the "View Details" button on one of the matches on the Search Inventory page (TC G01)
    def view_details(self):
        view_details_button = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/div/section/div/div[1]/div/div[4]/div[2]/div[6]/div[2]/div[2]/div/div[1]/div/div[2]/div[8]/div/a')
        print("found view details button")
        action(self.driver).move_to_element(view_details_button).click().perform()
        print("view details button has been selected")
        return

#Selecting the "Get Internet Price" button on one of the matches on the Search Inventory page (TC G02)
    def get_internet_price(self):
        get_an_internet_price_button = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/div/section/div/div/div[4]/div[1]/div[2]/div[1]/div/div/div[2]/button[1]')
        print("found get an internet price button")
        action(self.driver).move_to_element(get_an_internet_price_button).click().perform()
        print("get an internet price button has been selected")
        return

#Selecting the "Schedule a Test Drive" button on one of the matches on the Search Inventory page (TC G03)
    def schedule_test_drive(self):
        schedule_a_test_drive_button = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/div/section/div/div/div[4]/div[1]/div[2]/div[1]/div/div/div[2]/button[2]')
        print("found schedule a test drive button")
        action(self.driver).move_to_element(schedule_a_test_drive_button).click().perform()
        print("schedule a test drive has been selected")
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
