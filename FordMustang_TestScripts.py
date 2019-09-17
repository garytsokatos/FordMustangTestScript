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
def Test_A01_A06():

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

def Test_C03():

        TestModule.packages()

def Test_C04():

        TestModule.exterior()

def Test_C05():

        TestModule.interior()

Test_A01_A06()
Test_B01()
Test_C01()
Test_C02()
Test_C03()
Test_C04()
Test_C05()
time.sleep(5)
TestModule.close_browser()