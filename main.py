#### Calling classes and functions ####

# import class and functions
from DM import DeviceMagic
from PREP import *

# calling function for preparation
# of the main file for destination
transform_and_save()

# main instance:
my_selenium = DeviceMagic(headless = False,
                          kiosk = True)

# calling methods on a object:
my_selenium.setup().login("form_destination",
                          "username",
                          "password").sleep_time(1).rem_dest().sleep_time(1).add_destination().close_browser()