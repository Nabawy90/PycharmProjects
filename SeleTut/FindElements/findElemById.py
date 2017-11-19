from selenium import webdriver

driver = webdriver.Firefox()

driver.get('https://www.buytickets.virgintrains.co.uk/buytickets/categorymatrix.aspx?Command=TimeTable')


price = driver.find_element_by_xpath(".//*[@id='ticket_1_OFF-PEAK_0']/td[2]/span/label")


print(price.text)