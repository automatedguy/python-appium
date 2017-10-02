import os
import sys
import logging

import unittest

from appium import webdriver

# Returns abs path relative to this file and not cwd
from app.screens import WelcomeScreen
from constants.countries import ARG
from constants.platforms import ANDROID, V5_O1_O1, LOLLIPOP, APK_FILE

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class BaseTest(unittest.TestCase):

    PLATFORM_NAME = ANDROID
    PLATFORM_VERSION = V5_O1_O1
    DEVICE_NAME = LOLLIPOP
    APP = APK_FILE
    COUNTRY = ARG

    desired_caps = {}
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    def setUp(self):
        pass
        logging.info("Setting Up Mobile Capabilities.")
        self.desired_caps['platformName'] = self.PLATFORM_NAME
        self.desired_caps['platformVersion'] = self.PLATFORM_VERSION
        self.desired_caps['deviceName'] = self.DEVICE_NAME
        self.desired_caps['app'] = PATH("../resources/" + self.PLATFORM_NAME + "/" + self.APP)
        self.desired_caps['noReset'] = False

        self.show_capabilities()

        self.logger.info("Starting " + self.PLATFORM_NAME + " driver please wait...")
        self.app = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)

        welcome_screen = WelcomeScreen(self.app)
        welcome_screen.select_country(self.COUNTRY)

    def show_capabilities(self):
        self.logger.info("Platform Name: [" + self.desired_caps['platformName'] + "]")
        self.logger.info("platform Version: [" + self.desired_caps['platformVersion'] + "]")
        self.logger.info("Device Name: [" + self.desired_caps['deviceName'] + "]")
        self.logger.info("App File: [" + self.desired_caps['app'] + "]")
        self.logger.info("Country: [" + self.COUNTRY + "]")

    def tearDown(self):
        pass
        self.logger.info("Tearing Down Driver.")
        self.app.quit()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        BaseTest.PLATFORM_NAME = sys.argv.pop()
        BaseTest.PLATFORM_VERSION = sys.argv.pop()
        BaseTest.DEVICE_NAME = sys.argv.pop()
        BaseTest.APP = sys.argv.pop()
        BaseTest.COUNTRY = sys.argv.pop()
