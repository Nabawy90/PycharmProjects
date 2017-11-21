import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
#sys.path.append('..')
from GUIAutomation import ExpediaSearch
from GUIAutomation import XPATH_STD
from Validation import Validator
from selenium.webdriver.support.select import Select
import pandas as pd
import time

def get_lowest_prices_test():
    expediaTest = ExpediaSearch.Expedia()

    csv_file = os.path.dirname(os.path.realpath(__file__))+'/flights_input.csv'
    if Validator.validate_flights_data_test(csv_file):
        flightsDataFrame = pd.read_csv(csv_file)

        numOfFlights = len(flightsDataFrame.index)

        flightsDataFrame["Num Direct Flights"] = 0
        flightsDataFrame["Starting From"] = 0

        for i in range(numOfFlights):
            # Go to Expedia.co.uk
            expediaTest.navigateTo(r'https://www.expedia.co.uk/')

            # Selecting Flight only option
            btn_flightOnly = expediaTest.explicitWaitForClickableByXpath(10, XPATH_STD.BTN_FLIGHTS_ONLY)
            assert btn_flightOnly != None
            btn_flightOnly.click()

            # Selecting One Way option
            btn_oneWay = expediaTest.explicitWaitForClickableByXpath(10, XPATH_STD.BTN_ONE_WAY)
            btn_oneWay.click()

            # Sending the origin of the flight
            txt_flightOrigin = expediaTest.explicitWaitForClickableByXpath(10, XPATH_STD.TXT_FLIGHT_ORIGIN)
            txt_flightOrigin.clear()
            txt_flightOrigin.send_keys(str(flightsDataFrame.loc[i, 'from']))

            # Selecting the destination of the flight
            txt_flightDest = expediaTest.explicitWaitForClickableByXpath(10, XPATH_STD.TXT_FLIGHT_DEST)
            txt_flightDest.clear()
            txt_flightDest.send_keys(str(flightsDataFrame.loc[i, 'to']))

            # selecting the departure date
            txt_departingDate = expediaTest.explicitWaitForClickableByXpath(10, XPATH_STD.TXT_DEP_DATE)
            txt_departingDate.clear()
            txt_departingDate.send_keys(str(flightsDataFrame.loc[i, 'date']))

            btn_closeCalander = expediaTest.explicitWaitForClickableByXpath(10, XPATH_STD.BTN_CLOSE_CALANDER)
            btn_closeCalander.click()

            # Selecting the Drop Down for Adult number
            DD_adult = expediaTest.explicitWaitForClickableByXpath(10, XPATH_STD.DD_ADULT)
            selector = Select(DD_adult)
            selector.select_by_value(str(flightsDataFrame.loc[i, 'adults']))

            # Pressing the Search button
            btn_search = expediaTest.explicitWaitForClickableByXpath(10, XPATH_STD.BTN_SEARCH)
            btn_search.click()

            lbl_validation = expediaTest.explicitWaitForClickableByXpath(10, XPATH_STD.LBL_VALIDATION)
            assert lbl_validation.text == "Prices are one way per person, include all taxes and fees."

            # Selecting Direct flights only
            chk_bx_direct = expediaTest.explicitWaitForClickableByXpath(10, XPATH_STD.CHK_BX_DIRECT_FLIGHTS)
            chk_bx_direct.click()

            # Grabbing the text in the checkbox of Direct flights.
            time.sleep(3)
            lbl_directChkBxLable = expediaTest.explicitWaitForClickableByXpath(10, XPATH_STD.LBL_DIRECT_FLIGHTS)
            print(lbl_directChkBxLable.text)

            # adding two new columns in the datafram
            flightsDataFrame.loc[i, "Num Direct Flights"] = expediaTest.extract_flights_count(lbl_directChkBxLable.text)
            flightsDataFrame.loc[i, "Starting From"] = expediaTest.extract_flights_lowest_price(
                lbl_directChkBxLable.text)

            # end of for loop

        expediaTest.write_to_csv(flightsDataFrame, os.path.dirname(os.path.realpath(__file__))+"/flights_output.csv")
    else:
        print('CSV file is not valid, check console for errors')

    expediaTest.close_driver()



get_lowest_prices_test()
