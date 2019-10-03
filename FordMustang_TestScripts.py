'''
(PROJECTNAME)TestScripts

This is a template class for building test scripts using functionality
from the ItemSelectorClass
'''

from FordMustang_ItemSelectorClass import ItemSelectorClass   # import functionality
import time

TestModule = ItemSelectorClass()

  #  def __init__(self):

#Test A01 - Vehicle Customization Set-Up - "Vehicles"
def Survey_Handler_Method():

        TestModule.open_browser()

def Test_A01_A05():

        print("***Beginning Tests A01 through A06***")
        TestModule.get_to_car_build()

def Test_A06():

        TestModule.build_your_own()

#Vehicle Model Selection - Convertible
def Test_B01():

        print("***Beginning Test B01***")
        TestModule.choose_your_model_convertible()
        print('***Test B01 has passed***')

#Vehicle Model Customization - Paint Type
def Test_C01():

        print("***Beginning Test C01***")
        TestModule.paint_type()
        TestModule.tape_stripe()
        TestModule.racing_stripe()
        TestModule.hood_and_side_stripes()
        print("***Test Case C01 has passed***")

#Vehicle Model Customization - Powertrain
def Test_C02():

        print("***Beginning Test C02***")
        TestModule.zip_code_on_car_customization()
        time.sleep(2)
        TestModule.powertrain()
        TestModule.engine()
        TestModule.transmissions()
        print("***Test Case C02 has passed***")

#Vehicle Model Customization - Packages
def Test_C03():

        print("***Beginning Test C03***")
        TestModule.zip_code_on_car_customization()
        TestModule.packages()
        TestModule.equipment_group()
        TestModule.exterior_package()
        TestModule.interior_package()
        print("***Test Case C03 has passed***")

#Vehicle Model Customization - Exterior
def Test_C04():

        print("***Beginning Test C04***")
        TestModule.exterior()
        TestModule.wheel_type()
        TestModule.exterior_options()
        TestModule.tire_type()
        TestModule.rear_axle_ratios()
        print("***Test Case C04 has passed***")

#Vehicle Model Customization - Interior
def Test_C05():

        print("***Beginning Test C05***")
        TestModule.interior()
        TestModule.cloth()
        TestModule.interior_options()
        TestModule.radio_type()
        TestModule.audio_upgrade()
        print("***Test Case C05 has passed***")

#Post Customization - Summary
def Test_D01():

        print("***Beginning Test D01***")
        TestModule.summary()
        TestModule.get_internet_price()
        TestModule.special_offers()
        TestModule.trade_in_value()
        TestModule.search_inventory()
        time.sleep(2)
        #TestModule._continue_()
        print("***Test D01 has passed***")

#Let Us Find It For You - Select
def Test_E01():

        print("***Beginning Test E01***")
        TestModule.let_us_find_it_for_you_select()
        print("***Test E01 has passed***")

#Let Us Find It For You - Your Model
def Test_E02():

        print("***Beginning Test E02***")
        TestModule.let_us_find_it_for_you_your_model()
        print("***Test E02 has passed***")

#Let Us Find It For You - Exterior Colors
def Test_E03():

        print("***Beginning Test E03***")
        TestModule.let_us_find_it_for_you_exterior_colors()
        print("***Test E03 has passed***")

#Let Us Find It For You - Interior Colors
def Test_E04():

        print("***Beginning Test E04***")
        TestModule.let_us_find_it_for_you_interior_colors()
        print("***Test E04 has passed***")

#Let Us Find It For You - Your Preferences
def Test_E05():

        print("***Beginning Test E05***")
        TestModule.let_us_find_it_for_you_your_preferences()
        print("***Test E05 has passed***")

#Let Us Find It For You - Optional Upgrades
def Test_E06():

        print("***Beginning Test E06***")
        TestModule.let_us_find_it_for_you_optional_upgrades()
        print("***Test E06 has passed***")

def Test_F01():

        print("***Beginning Test F01***")
        TestModule._continue_()
        print("***Test F01 has passed***")

def Test_F02():

        print("***Beginning Test F02***")
        time.sleep(2)
        TestModule.change_dealer_mileage()
        TestModule.change_dealer_zipcode()
        #TestModule.select_from_list_of_dealers()
        #TestModule.body_style()
        TestModule.select_model()
        TestModule.year()
        print("***Test F02 has passed***")

def  Test_F03():

        print("***Beginning Test F03***")
        TestModule.power_and_handling()
        print("***Test F03 has passed***")

def Test_F04():

        print("***Beginning Test F04***")
        TestModule.exterior_color()
        print("***Test F04 has passed***")

def Test_F05():

        print("***Beginning Test F05***")
        TestModule.interior_color()
        print("***Test F05 has passed***")

def Test_F06():

        print("***Beginning Test F06***")
        TestModule.exterior_features()
        print("***Test F06 has passed***")

def Test_F07():

        print("***Beginning Test F07***")
        TestModule.let_us_find_your_vehicle()
        print("***Test F07 has passed***")

def Test_G01():

        print("***Beginning Test G01***")
        TestModule.view_details()
        print("***Test G01 has passed***")

def Test_G02():

        print("***Beginning Test G02***")
        TestModule.get_internet_price()
        print("***Test G02 has passed***")

def Test_G03():

        print("***Beginning Test G03***")
        TestModule.schedule_test_drive()
        print("***Test G03 has passed***")

Survey_Handler_Method()
Test_A01_A05()
Test_A06()
Test_B01()
Test_C01()
Test_C02()
Test_C03()
Test_C04()
Test_C05()
Test_D01()
'''Test_F01()
Test_F02()
Test_F03()
Test_F04()
Test_F05()
Test_F06()
Test_F07()
Test_G01()
Test_G02()
Test_G03()'''
print("opening new page")
time.sleep(5)
Survey_Handler_Method()
Test_A01_A05()
Test_E01()
Test_E02()
Test_E03()
Test_E04()
Test_E05()
Test_E06()
print("closing browser")
time.sleep(5)
TestModule.close_browser()