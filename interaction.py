from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

# This code stores a list of upcoming python conferences into an object called schedule
chrome_driver_path = Service(r"C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
driver.get("https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/")

# num_of_articles = driver.find_element(by=By.CSS_SELECTOR, value="#mp-otd p b")
# # num_of_articles.click()
# nominate_link = driver.find_element(by=By.LINK_TEXT, value="Nominate an article")
# # nominate_link.click()
#
# search_box = driver.find_element(by=By.CSS_SELECTOR, value="#searchform input")
# search_box.send_keys("Python")
# search_box.send_keys(Keys.ENTER)

first_name = driver.find_element(by=By.CSS_SELECTOR, value="input[name='fName']")
last_name = driver.find_element(by=By.CSS_SELECTOR, value="input[name='lName']")
email = driver.find_element(by=By.CSS_SELECTOR, value="input[name='email']")
first_name.send_keys("My name")
last_name.send_keys("My surname")
email.send_keys("my_email@address.com")
submit = driver.find_element(by=By.CSS_SELECTOR, value="form button")
submit.click()

sleep(2)
driver.quit()
