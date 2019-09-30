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

def Test_A01_A06():

        TestModule.open_browser()
        TestModule.get_to_car_build()

def Test_B01():

        TestModule.choose_your_model_convertible()

def Test_C01():

        TestModule.paint_type()
        TestModule.tape_stripe()
        TestModule.racing_stripe()
        TestModule.hood_and_side_stripes()

def Test_C02():

        TestModule.powertrain()
        TestModule.engine()
        TestModule.transmissions()

def Test_C03():

        TestModule.packages()
        TestModule.equipment_group()
        TestModule.exterior_package()
        TestModule.interior_package()

def Test_C04():

        TestModule.exterior()
        TestModule.wheel_type()
        TestModule.exterior_options()
        TestModule.tire_type()
        TestModule.rear_axle_ratios()

def Test_C05():

        TestModule.interior()
        TestModule.cloth()
        TestModule.interior_options()
        TestModule.radio_type()
        TestModule.audio_upgrade()

def Test_D01():

        TestModule.summary()
        #TestModule.special_offers()
        #TestModule.trade_in_value()
        TestModule.search_inventory()
        TestModule._continue_()

def Test_E01():

        TestModule.let_us_find_it_for_you_select()
        TestModule.let_us_find_it_for_you_your_model()
        TestModule.let_us_find_it_for_you_exterior_colors()
        TestModule.let_us_find_it_for_you_interior_colors()
        TestModule.let_us_find_it_for_you_your_preferences()
        TestModule.let_us_find_it_for_you_optional_upgrades()

def Test_F01():

        TestModule._continue_()

def Test_F02():

        TestModule.change_dealer_mileage()
        TestModule.change_dealer_zipcode()
        TestModule.select_from_list_of_dealers()
        TestModule.body_style()
        TestModule.select_model()
        TestModule.year()

def Test_F03():

        TestModule.power_and_handling()

def Test_F04():

        TestModule.exterior_color()

def Test_F05():

        TestModule.interior_color()

def Test_F06():

        TestModule.exterior_features()

def Test_F07():

        TestModule.let_us_find_your_vehicle()

def Test_G01():

        TestModule.view_details()

def Test_G02():

        TestModule.get_internet_price()

def Test_G03():

        TestModule.schedule_test_drive()

#Survey_Handler_Method()

Test_A01_A06()
Test_B01()
Test_C01()
Test_C02()
Test_C03()
Test_C04()
Test_C05()
Test_D01()
'''Test_E01()
Test_F01()
Test_F02()
Test_F03()
Test_F04()
Test_F05()
Test_F06()
Test_F07()
Test_G01()
Test_G02()
Test_G03()'''
print("closing browser")
time.sleep(5)
TestModule.close_browser()