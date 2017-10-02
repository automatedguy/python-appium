# coding=utf-8

import logging

from selenium.webdriver.support.wait import WebDriverWait

from app import locators
from app.constants.countries import ARGENTINA, COLOMBIA, MEXICO, ARG, COL, MEX
from app.constants.err import ERR_001
from app.constants.messages import TOUCH_ARG_LINK, TOUCH_COL_LINK, TOUCH_MEX_LINK, WAITING_FOR
from app.constants.webelements import LINK


class BaseScreen(object):
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, description, obj):
        self.logger.info(WAITING_FOR + " [" + description + "] " + obj)
        WebDriverWait(self.driver, 100).until(lambda driver: driver.find_element_by_xpath(locator))
        return self.driver.find_element_by_xpath(locator)

    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)


class WelcomeScreen(BaseScreen):
    def touch_argentina(self):
        element = self.wait_for_element(locators.WelcomeScreen.ARGENTINA_LINK, ARGENTINA, LINK)
        self.logger.info(TOUCH_ARG_LINK)
        element.click()

    def touch_colombia(self):
        element = self.wait_for_element(locators.WelcomeScreen.COLOMBIA_LINK, COLOMBIA, LINK)
        self.logger.info(TOUCH_COL_LINK)
        element.click()

    def touch_mexico(self):
        element = self.wait_for_element(locators.WelcomeScreen.MEXICO_LINK, MEXICO, LINK)
        self.logger.info(TOUCH_MEX_LINK)
        element.click()

    def errhandler(self):
        self.logger.error(ERR_001)

    def select_country(self, country):
        if country == ARG:
            self.touch_argentina()
        elif country == COL:
            self.touch_colombia()
        elif country == MEX:
            self.touch_mexico()
        else:
            self.errhandler()
