from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
#import time

class Expedia:
    driver = webdriver.Firefox()

    def navigateTo(self, URL):
        Expedia.driver.get(URL)

    def findByXPath(self, xpath):
        return Expedia.driver.find_element_by_xpath(xpath)

    def explicitWaitForClickableByXpath(self, timeOut, xpath):

        wait = WebDriverWait(driver=Expedia.driver, timeout=timeOut, poll_frequency=2,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotInteractableException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                         xpath)))
        return element

    def explicitWaitForTextBoxByXpath(self, timeOut, xpath):

        wait = WebDriverWait(driver=Expedia.driver, timeout=timeOut, poll_frequency=2,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotInteractableException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                         xpath)))
        return element

