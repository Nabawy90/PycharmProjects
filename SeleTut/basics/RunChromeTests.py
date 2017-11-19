from selenium import webdriver
import os

driverLocation = r'E:\Apps\chromedriver_win32'
os.environ["webdriver.chrome.driver"] = driverLocation
driver = webdriver.Chrome(driverLocation)

driver.get("https://www.facebook.com/")