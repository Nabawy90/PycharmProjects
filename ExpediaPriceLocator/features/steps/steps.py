from behave import given
from behave import when
from behave import then
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..\\..\\"))
from GUIAutomation import ExpediaSearch
from GUIAutomation import XPATH_STD
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By



@given("I go to Expedia website")
def go_to_expedia_website(context):
    context.expSearch = ExpediaSearch.Expedia()
    context.expSearch.navigateTo(r'https://www.expedia.co.uk/')
    btn_flightOnly = context.expSearch.explicitWaitForClickableByXpath(10, XPATH_STD.BTN_FLIGHTS_ONLY)

    if btn_flightOnly is None:
        raise Exception("Button One way not found")

    btn_flightOnly.click()

    # Selecting One Way option
    btn_oneWay = context.expSearch.explicitWaitForClickableByXpath(10, XPATH_STD.BTN_ONE_WAY)
    if btn_oneWay is None:
        raise Exception("Button One way not found")
    btn_oneWay.click()

@when("{adult_count} adult wants to fly on {date} from {origin} to {dest}")
def submit_flight_data(context, adult_count, date, origin, dest):
    # Sending the origin of the flight
    txt_flightOrigin = context.expSearch.explicitWaitForClickableByXpath(10, XPATH_STD.TXT_FLIGHT_ORIGIN)
    txt_flightOrigin.clear()
    txt_flightOrigin.send_keys(origin)

    # Selecting the destination of the flight
    txt_flightDest = context.expSearch.explicitWaitForClickableByXpath(10, XPATH_STD.TXT_FLIGHT_DEST)
    txt_flightDest.clear()
    txt_flightDest.send_keys(dest)

    # selecting the departure date
    txt_departingDate = context.expSearch.explicitWaitForClickableByXpath(10, XPATH_STD.TXT_DEP_DATE)
    txt_departingDate.clear()
    txt_departingDate.send_keys(date)

    btn_closeCalander = context.expSearch.explicitWaitForClickableByXpath(10, XPATH_STD.BTN_CLOSE_CALANDER)
    btn_closeCalander.click()

    # Selecting the Drop Down for Adult number
    DD_adult = context.expSearch.explicitWaitForClickableByXpath(10, XPATH_STD.DD_ADULT)
    selector = Select(DD_adult)
    selector.select_by_value(adult_count)

    # Pressing the Search button
    btn_search = context.expSearch.explicitWaitForClickableByXpath(10, XPATH_STD.BTN_SEARCH)
    btn_search.click()
    pass

@then("I shall see an error telling me that origin and destination are the same")
def validate_error_message(context):
    error_message = context.expSearch.explicitWaitForClickableByXpath(10,r"//*[@id='gcw-flights-form-hp-flight']/div[2]/div/ul/li/a")

    if error_message.text != "Please choose a different destination from origin.":
        raise Exception("Wrong error message on page")


@then("I shall see an error telling me that the date is in the past")
def validate_date_error_message(context):
    error_message = context.expSearch.explicitWaitForClickableByXpath(10,r"//*[@id='gcw-flights-form-hp-flight']/div[2]/div/ul/li/a")

    if not error_message.text.startswith("Dates must be between"):
        raise Exception("Wrong error message on page")
