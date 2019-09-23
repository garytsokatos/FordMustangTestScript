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


def dictionary_iterater(self, dictionary):
    for el in dictionary:
        button = self.driver.find_element_by_xpath(dictionary[el][0])
        print("Found " + dictionary[el][1])
        action(self.driver).move_to_element(button).click().perform()
        print("\t" + dictionary[el][1] + " has been selected")
        self.change_requirement()

class ItemSelectorClass:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('-icognito')
        self.driver = webdriver.Chrome(r"C:\drivers\chromedriver.exe", options=self.chrome_options)
        self.CurrentModule = "Initialization"
        self.ErrorCount = 0
        self.driver.get("https://www.ford.com/")
        #self.driver.get("https://shop.ford.com/build/mustang/#/config/Config%5B%7CFord%7CMustang%7C2020%7C1%7C1.%7C100A.P8U.....CON.MST.~YZKAA.EBST.LESS.%5D")
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



#Selecting the buttons on the home page to initiate the customization process flow (Test Cases A01 - A06)
    def get_to_car_build(self):
        vehicles_home_page_button = self.driver.find_element_by_class_name('dropdown.dropdown-item')
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
        select_zip_button = self.driver.find_element_by_xpath('/html/body/div[20]/div/div/form/div/div[3]/input')
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

        '''build_your_own_button = self.driver.find_element_by_xpath('/html/body/div[9]/div[7]/div/div/div/div/div/div[2]/div[1]/a')
        print("found bouild your own")
        time.sleep(2)
        action(self.driver).move_to_element(build_your_own_button).click().perform()
        print('\tbuild your own button has been found and selected')
        print('\t\t***Test A06 has passed***')'''
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

    # Selecting all possible tape stripe options in the paint type category (Test Case C01)
    def tape_stripe(self):
        tape_stripe_selection = {
            0: ("//div[contains(text(), 'Silver Tape Stripe')]", 'Silver Tape Stripe'),
            1: ("//div[contains(text(), 'Ebony Tape Stripe')]",  'Ebony Tape Stripe'),
            2: ("//div[contains(text(), 'Less Tape Stripe')]", 'Less Tape Stripe'),
        }
        dictionary_iterater(self, tape_stripe_selection)

        print("\t\tall tape stripes have been selected")
        return

    # Selecting all possible racing stripe options in the paint type category (Test Case C01)
    def racing_stripe(self):
        racing_stripe_selection = {
            0:  ("//div[contains(text(), 'Ebony Racing Stripe')]", 'Ebony Tape Stripe'),
            1:  ("//div[contains(text(), 'Less Racing Stripe')]", 'Less Racing Stripe'),
        }
        dictionary_iterater(self, racing_stripe_selection)

        print("\t\tall racing stripes have been selected")
        return

    # Selecting all possible paint options in the paint type category (Test Case C01)
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

    # Selecting all possible engine and transmission options in the powertrain category (Test Case C02)
    def powertrain(self):
        powertrain_select = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[2]/div[1]/div/div/span[3]')
        action(self.driver).move_to_element(powertrain_select).click().perform()
        print("powertrain drop-down has been selected")

        time.sleep(2)
        return

    def engine(self):
        engine_selection = {
            0:  ("//span[contains(text(), '2.3L High Performance EcoBoost® Engine')]", '2.3L High Performance EcoBoost® Engine'),
            1:  ("//span[contains(text(), '2.3L EcoBoost® Engine')]", '2.3L EcoBoost® Engine')
        }
        dictionary_iterater(self, engine_selection)
        return

    def transmissions(self):
        transmissions_selection = {
            0: ("//span[contains(text(), '10-Speed SelectShift® Automatic Transmission')]", '10-Speed SelectShift® Automatic Transmission'),
            1: ("//span[contains(text(), '6-Speed Manual Transmission')]", '6-Speed Manual Transmission')
        }
        dictionary_iterater(self, transmissions_selection)

        print("\tAll engines and transmissions have been selected")
        print("\t\t***Test Case C02 has paseed***")
        return

    # Selecting all possible equipment group, exterior, and interior package options in the packages category (Test Case C03)
    def packages(self):
        packages_select = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[3]/div[1]/div/div')
        action(self.driver).move_to_element(packages_select).click().perform()
        print("packages drop-down has been selected")
        return

    def equipment_group(self):
        equipment_group_selection = {
            0: ("//span[contains(text(), '101A Equipment Group')]", '101A Equipment Group'),
            1: ("//span[contains(text(), '100A Equipment Group')]", '100A Equipment Group')
        }
        dictionary_iterater(self, equipment_group_selection)
        return

    def exterior_package(self):
        exterior_packasge_selection = {
            0: ("//span[contains(text(), 'Black Accent Package')]", '101A Equipment Group'),
            1: ("//span[contains(text(), '2.3L High Performance Package')]", '2.3L High Performance Package'),
            2: ("//span[contains(text(), 'Wheel & Stripe Package')]", 'Wheel & Stripe Package')
        }
        dictionary_iterater(self, exterior_packasge_selection)
        return

    def interior_package(self):
        ford_safe_and_smart_package = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[3]/div[2]/div[3]/ul/li/div[1]/div[2]/img')
        action(self.driver).move_to_element(ford_safe_and_smart_package).click().perform()
        time.sleep(1)
        add = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[4]/div[4]/a')
        action(self.driver).move_to_element(add).click().perform()
        print("\tford safe and smart package has been selected")

        print("\t\tall packages have been selected")
        print("\t\t\t***Test Case C03 has passed***")
        return


    # Selecting all possible wheel type, exterior options, tire type, and rear axle options in the exterior category (Test Case C04)
    def exterior(self):
        exterior_select = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[4]/div[1]/div/div/span[3]')
        print("found exterior select")
        action(self.driver).move_to_element(exterior_select).click().perform()
        print("exterior drop-down has been selected")
        return

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

    def interior(self):
        interior_select = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[5]/div[1]/div/div')
        print("found interior select")
        action(self.driver).move_to_element(interior_select).click().perform()
        print("interior drop-down has been selected")
        return

    def cloth(self):
        ceramic = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[5]/div[2]/div[1]/div[2]/div/div[2]/div[1]/ul/li[2]/div/div[1]/img')
        print("found ceramic cloth")
        action(self.driver).move_to_element(ceramic).click().perform()
        print("ceramic cloth has been selected")

        ebony = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[5]/div[2]/div[1]/div[2]/div/div[2]/div[1]/ul/li[1]/div/div[1]/img')
        print("found ebony cloth")
        action(self.driver).move_to_element(ebony).click().perform()
        print("ebony cloth has been selected")
        return

    #def seat_type(self):

    def interior_options(self):
        rear_axle_selection = {
            0: ("//span[contains(text(), '\"Silver Arrow\" Aluminum Instrument Panel Finish')]", '\"Silver Arrow\" Aluminum Instrument Panel Finish'),
            1: ("//span[contains(text(), 'Adaptive Cruise Control')]", 'Adaptive Cruise Control'),
            2: ("//span[contains(text(), 'Premium Floor Liners Front and Rear')]", 'Premium Floor Liners Front and Rear')
        }
        dictionary_iterater(self, rear_axle_selection)

        print("\tall interior options have been selected")
        return

    def radio_type(self):
        radio_selection = {
            0: ("//span[contains(text(), 'AM/FM Stereo with MP3 Capability and Six (6) Speakers')]", 'AM/FM Stereo with MP3 Capability and Six (6) Speakers'),
            1: ("//span[contains(text(), 'Nine (9) Speaker Sound System with Amplifier')]", 'Nine (9) Speaker Sound System with Amplifier')
        }
        dictionary_iterater(self, radio_selection)
        print("\tall radio types have been selected")
        return

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

    def summary(self):
        summary_button = self.driver.find_element_by_xpath('/html/body/div[9]/div[6]/div[3]/div[3]/div[2]/div/div/div[6]/div/span/div')
        print("found summary button")
        action(self.driver).move_to_element(summary_button).click().perform()
        print("summary button has been selected")

        #summary_close = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[1]')
        #print("found close button")
        #action(self.driver).move_to_element(summary_close).click().perform()
        #print("close button has been selected")

    def special_offers(self):
        special_offers = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[6]/div[3]/div[7]/div[3]/a')
        print("found special offers")
        time.sleep(1)
        action(self.driver).move_to_element(special_offers).click().perform()
        print("special offers has been selected")

        time.sleep(3)

        special_offers_close = self.driver.find_element_by_xpath('/html/body/div[21]/div/div/div/div[1]')
        print("found special offers close button")
        action(self.driver).move_to_element(special_offers_close).click().perform()
        print("special offers close button has been selected")

    def trade_in_value(self):
        look_up_trade_in_value = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[6]/div[3]/div[7]/div[4]/a')
        print("found look up trade-in-value")
        action(self.driver).move_to_element(look_up_trade_in_value).click().perform()
        print("look up trade-in-value has been selected")

        time.sleep(3)

        look_up_trade_in_value_close = self.driver.find_element_by_xpath('/html/body/div[21]/div/div/div/div[1]')
        print("found look up trade-in-value close button")
        action(self.driver).move_to_element(look_up_trade_in_value_close).click().perform()
        print("look up trade-in-value button has been selected")

    def search_inventory(self):
        search_inventory = self.driver.find_element_by_xpath('/html/body/div[9]/div[8]/div[6]/div[3]/div[7]/div[2]/a')
        print("found search inventory")
        action(self.driver).move_to_element(search_inventory).click().perform()

#Test Case Category E, make sure to set test case category A in the test script as a precondition
    def let_us_find_it_for_you_select(self):
        let_us_find_it_for_you_button = self.driver.find_element_by_xpath('/html/body/div[9]/div[7]/div/div/div/div/div/div[2]/div[2]/a/div/img')
        print("found let us find it for you button")
        action(self.driver).move_to_element(let_us_find_it_for_you_button).click().perform()
        print("let us find it for you button has been selected")

#TODO clean up full xpath
    def let_us_find_it_for_you_your_model(self):
        your_model_selection = {
            0: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div/span', 'EcoBoost® Fastback'),
            1: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/span', 'EcoBoost® Premium Fastback'),
            2: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[1]/div/span', 'EcoBoost® Convertible'),
            3: ('/html/body/div[8]/div[6]/div/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[1]/div[2]/div/div[4]/div[1]/div[1]/div[1]/div/span', 'GT Fastback'),
            4: ('//span[@class="feature-unchecker.icon-unchecker-checkbox", "EcoBoost® Premium Convertible"]', 'EcoBoost® Premium Convertible'),
            5: ('//span[@class="feature-unchecker.icon-unchecker-checkbox", "GT Premium Fastback"]', 'GT Premium Fastback'),
            6: ('//span[@class="feature-unchecker.icon-unchecker-checkbox", "GT Premium Convertible"]', 'GT Premium Convertible'),
            7: ('//span[@class="feature-unchecker.icon-unchecker-checkbox", "BULLITT™"]', 'BULLITT™'),
            8: ('//span[@class="feature-unchecker.icon-unchecker-checkbox", "Shelby GT350®"]', 'Shelby GT350®'),
            9: ('//span[@class="feature-unchecker.icon-unchecker-checkbox", "Shelby GT500®"]', 'Shelby GT500®'),
            10: ('//span[@class="feature-unchecker.icon-unchecker-checkbox", "Shelby® GT350R"]', 'Shelby® GT350R')
        }
        dictionary_iterater(self, your_model_selection)
        print("all models have been selected")
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
