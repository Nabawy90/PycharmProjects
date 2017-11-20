from ExpediaPriceLocator.GUIAutomation import ExpediaSearch
from selenium.webdriver.support.select import Select
import time
import pandas as pd


def get_lowest_prices():
    expediaTest = ExpediaSearch.Expedia()
    flightsDataFrame = pd.read_csv('flights_input.csv')

    numOfFlights = len(flightsDataFrame.index)

    flightsDataFrame["Num Direct Flights"] = 0
    flightsDataFrame["Starting From"] = 0

    for i in range(numOfFlights):
        # Go to Expedia.co.uk
        expediaTest.navigateTo(r'https://www.expedia.co.uk/')

        # Selecting Flight only option
        btn_flightOnly = expediaTest.explicitWaitForClickableByXpath(10, r"//*[@id='tab-flight-tab-hp']")
        assert btn_flightOnly!=None
        btn_flightOnly.click()

        # Selecting One Way option
        btn_oneWay = expediaTest.explicitWaitForClickableByXpath(10, r"//*[@id='flight-type-one-way-label-hp-flight']")
        btn_oneWay.click()

        # Sending the origin of the flight
        txt_flightOrigin = expediaTest.explicitWaitForClickableByXpath(10, r"//*[@id='flight-origin-hp-flight']")
        txt_flightOrigin.clear()
        txt_flightOrigin.send_keys(str(flightsDataFrame.loc[i, 'from']))


        # Selecting the destination of the flight
        txt_flightDest = expediaTest.explicitWaitForClickableByXpath(10, r"//*[@id='flight-destination-hp-flight']")
        txt_flightDest.clear()
        txt_flightDest.send_keys(str(flightsDataFrame.loc[i, 'to']))

        # selecting the departure date
        txt_departingDate = expediaTest.explicitWaitForClickableByXpath(10, r"//*[@id='flight-departing-single-hp-flight']")
        txt_departingDate.clear()
        txt_departingDate.send_keys(str(flightsDataFrame.loc[i, 'date']))

        btn_closeCalander = expediaTest.explicitWaitForClickableByXpath(10, r"//*[@id='flight-departing-wrapper-single-hp-"
                                                                            r"flight']/div/div/div[1]/button")
        btn_closeCalander.click()

        # Selecting the Drop Down for Adult number
        DD_adult = expediaTest.explicitWaitForClickableByXpath(10, r"//*[@id='flight-adults-hp-flight']")
        selector = Select(DD_adult)
        selector.select_by_value(str(flightsDataFrame.loc[i, 'adults']))

        btn_search = expediaTest.explicitWaitForClickableByXpath(10, r"//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button")
        time.sleep(2)
        btn_search.click()

        chk_bx_direct = expediaTest.explicitWaitForClickableByXpath(10,r"//*[@id='stopFilter_stops-0']")
        chk_bx_direct.click()

        lbl_directChkBxLable = expediaTest.explicitWaitForClickableByXpath(10, r"//*[@id='Direct-stop-flights-checkbox']")
        print(lbl_directChkBxLable.text)

        flightsDataFrame.loc[i, "Num Direct Flights"] = expediaTest.extract_flights_count(lbl_directChkBxLable.text)
        flightsDataFrame.loc[i, "Starting From"] = expediaTest.extract_flights_lowest_price(lbl_directChkBxLable.text)

        # end of for loop

    expediaTest.write_to_csv(flightsDataFrame,"flights_output.csv")


get_lowest_prices()