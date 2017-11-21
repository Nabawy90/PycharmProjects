from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By

class Expedia:

    '''
    profile = webdriver.FirefoxProfile()
    profile.set_preference('dom.popup_maximum', 0)
    profile.set_preference('privacy.popups.showBrowserMessage', False)
    '''
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

    def extract_flights_count(self, text):
        # Text comes in this format "2 direct flights from £90", to extract the number a split on space will take place
        # and first element will be returned.
        splitted = text.split(' ')
        return splitted[0]

    def extract_flights_lowest_price(self, text):
        '''

        Text comes in this format "2 direct flights from £90", to extract the number a split on space will take place
        and last element will be returned.

        :param text: text string cought from the web
        :return: number of direct flights
        '''

        splitted = text.split('£')
        return splitted[-1]

    def write_to_csv(self, dataFrame, csv_file_location):
        '''

        writes the data obtained from expedia to the csv file

        :param csv_file_location: location of csv file to be used.
        :return: true if write operation was successful
        '''

        dataFrame.to_csv(csv_file_location)

    def close_driver(self):
        Expedia.driver.close()