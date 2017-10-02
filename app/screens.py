# coding=utf-8

import logging

from selenium.webdriver.support.wait import WebDriverWait

from app import locators
from app.constants.countries import ARGENTINA, COLOMBIA, MEXICO, ARG, COL, MEX
from app.constants.err import ERR_001
from app.constants.messages import TOUCH_ARG_LINK_MSG, TOUCH_COL_LINK_MSG, TOUCH_MEX_LINK_MSG, WAITING_FOR_MSG, \
    SEGUIR_COMO_INVITADO_MSG
from app.constants.webelements import LINK, SEGUIR_COMO_INVITADO


class BaseScreen(object):
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, description, obj):
        self.logger.info(WAITING_FOR_MSG + " [" + description + "] " + obj)
        WebDriverWait(self.driver, 100).until(lambda driver: driver.find_element_by_xpath(locator))
        return self.driver.find_element_by_xpath(locator)

    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)


class WelcomeScreen(BaseScreen):
    def touch_argentina(self):
        element = self.wait_for_element(locators.WelcomeScreen.ARGENTINA_LINK, ARGENTINA, LINK)
        self.logger.info(TOUCH_ARG_LINK_MSG)
        element.click()

    def touch_colombia(self):
        element = self.wait_for_element(locators.WelcomeScreen.COLOMBIA_LINK, COLOMBIA, LINK)
        self.logger.info(TOUCH_COL_LINK_MSG)
        element.click()

    def touch_mexico(self):
        element = self.wait_for_element(locators.WelcomeScreen.MEXICO_LINK, MEXICO, LINK)
        self.logger.info(TOUCH_MEX_LINK_MSG)
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
        return LoginScreen(self)


class LoginScreen(BaseScreen):
    def touch_seguir_como_invitado(self):
        element = self.wait_for_element(locators.LoginScreen.SEGUIR_COMO_INVITADO_LNK, SEGUIR_COMO_INVITADO, LINK)
        self.logger.info(SEGUIR_COMO_INVITADO_MSG)
        element.click()
