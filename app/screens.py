# coding=utf-8

import logging

from selenium.webdriver.support.wait import WebDriverWait

from app import locators


class BaseScreen(object):
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, description, obj):
        self.logger.info("Waiting for: [" + description + "] " + obj)
        WebDriverWait(self.driver, 100).until(lambda driver: driver.find_element_by_xpath(locator))
        return self.driver.find_element_by_xpath(locator)

    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)


class WelcomeScreen(BaseScreen):
    def touch_argentina(self):
        element = self.wait_for_element(locators.WelcomeScreen.ARGENTINA_LINK, "Argentina", "Link")
        self.logger.info("Touching: [Argentina] link.")
        element.click()

    def touch_colombia(self):
        element = self.wait_for_element(locators.WelcomeScreen.COLOMBIA_LINK, "Colombia", "Link")
        self.logger.info("Touching: [Colombia] link.")
        element.click()

    def touch_mexico(self):
        element = self.wait_for_element(locators.WelcomeScreen.MEXICO_LINK, "México", "Link")
        self.logger.info("Touching: [México] link.")
        element.click()

    def errhandler(self):
        self.logger.error("Your input has not been recognised")

    def select_country(self, country):
        if country == "ARGENTINA":
            self.touch_argentina()
        elif country == "COLOMBIA":
            self.touch_colombia()
        elif country == "MEXICO":
            self.touch_mexico()
        else:
            self.errhandler()
