import os
import sys
import logging

import unittest

from appium import webdriver

from app.constants.messages import DRIVER_SUCCESS_MSG, TEAR_DOWN_MSG, STARTING_MSG, CONNECTING_MSG, LOCALLY_MSG, \
    REMOTELY_MSG, SET_UP_MSG, PLATFORM_NAME_MSG, PLATFORM_VERSION_MSG, DEVICE_NAME_MSG, APP_FILE_MSG, COUNTRY_MSG, BRC
from app.constants.saucelabs import USER_NAME, ACCESS_KEY, SAUCELABS_URL, LOCAL_URL, HTTPS_URL, HTTP_URL
from app.screens import WelcomeScreen
from constants.countries import ARG
from constants.platforms import ANDROID, V5_O1_O1, LOLLIPOP, APK_FILE, APPIUM_V1_O6_O4, V7_O0

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class BaseTest(unittest.TestCase):
    PLATFORM_NAME = ANDROID
    PLATFORM_VERSION = V5_O1_O1
    # PLATFORM_VERSION = V7_O0
    DEVICE_NAME = LOLLIPOP
    APP = APK_FILE
    APPIUM_VERSION = None
    # APPIUM_VERSION = APPIUM_V1_O6_O4
    COUNTRY = ARG

    desired_caps = {}
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    def setUp(self):
        pass

        logging.info(SET_UP_MSG)
        self.desired_caps['platformName'] = self.PLATFORM_NAME
        self.desired_caps['platformVersion'] = self.PLATFORM_VERSION
        self.desired_caps['deviceName'] = self.DEVICE_NAME
        self.desired_caps['app'] = PATH("../resources/" + self.PLATFORM_NAME + "/" + self.APP)
        self.desired_caps['noReset'] = False
        self.desired_caps['appiumVersion'] = self.APPIUM_VERSION

        self.show_capabilities()

        if self.desired_caps['appiumVersion'] is None:
            self.launch_app_local()
        else:
            self.launch_app_remote()

        self.navigate_to_home()

    def show_capabilities(self):
        self.logger.info(PLATFORM_NAME_MSG + self.desired_caps['platformName'] + BRC)
        self.logger.info(PLATFORM_VERSION_MSG + self.desired_caps['platformVersion'] + BRC)
        self.logger.info(DEVICE_NAME_MSG + self.desired_caps['deviceName'] + BRC)
        self.logger.info(APP_FILE_MSG + self.desired_caps['app'] + BRC)
        self.logger.info(COUNTRY_MSG + self.COUNTRY + BRC)

    def launch_app_local(self):
        self.logger.info(STARTING_MSG + self.PLATFORM_NAME + LOCALLY_MSG)
        self.app = webdriver.Remote(HTTP_URL + LOCAL_URL, self.desired_caps)
        self.logger.info(self.PLATFORM_NAME + DRIVER_SUCCESS_MSG)

    def launch_app_remote(self):
        self.logger.info(CONNECTING_MSG + self.PLATFORM_NAME + REMOTELY_MSG)
        self.app = webdriver.Remote(HTTPS_URL + USER_NAME + ":" + ACCESS_KEY + SAUCELABS_URL, self.desired_caps)
        self.logger.info(self.PLATFORM_NAME + DRIVER_SUCCESS_MSG)

    def navigate_to_home(self):
        welcome_screen = WelcomeScreen(self.app)
        self.login_selection_screen = welcome_screen.select_country(self.COUNTRY)
        self.login_selection_screen.touch_seguir_como_invitado()

    def tearDown(self):
        pass
        self.logger.info(TEAR_DOWN_MSG)
        self.app.quit()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        BaseTest.PLATFORM_NAME = sys.argv.pop()
        BaseTest.PLATFORM_VERSION = sys.argv.pop()
        BaseTest.DEVICE_NAME = sys.argv.pop()
        BaseTest.APP = sys.argv.pop()
        BaseTest.COUNTRY = sys.argv.pop()
