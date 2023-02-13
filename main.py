from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# This code stores a list of upcoming python conferences into an object called schedule
chrome_driver_path = Service(r"C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
driver.get("https://python.org")

dates = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
events = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")

schedule = {}

for n in range(len(dates)):
    schedule[n] = {
        "time": dates[n].text,
        "name": events[n].text
    }

print(schedule)

# This is testing code for reference

# driver.get("https://gurbax.lol")
# content = driver.find_element(by=By.XPATH, value="/html/body/ul[1]/li[2]/strong")
# print(content.text)
#
# headlines = driver.find_elements(by=By.CLASS_NAME, value="h3")
#
# for headline in headlines:
#     print(headline.text)

driver.quit()
