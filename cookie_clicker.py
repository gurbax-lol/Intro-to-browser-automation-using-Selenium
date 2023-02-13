from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

chrome_driver_path = Service(r"C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

big_cookie = driver.find_element(by=By.ID, value="cookie")
sleep(5)

i = 0
while i < 100:
    big_cookie.click()
    i += 1

sleep(5)

driver.quit()
