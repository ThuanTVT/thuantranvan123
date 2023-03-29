
from selenium import webdriver
import time
driver = webdriver.Chrome("chromedriver.exe")
driver.get('http://facebook.com')
time.sleep(3)
driver.quit()