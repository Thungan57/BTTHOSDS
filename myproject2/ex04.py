from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import pandas as pd

# Duong dan den file thuc thi geckodriver
gecko_path = "D:/OSDS/project2/geckodriver.exe"

# Kho to doi tuong dinh vu voi duong geckodriver
ser = Service(gecko_path)

# Tao tuy chon
options = webdriver.firefox.options.Options()
options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"

# Thiet lap firefox chi hien thi giao dien
options.headless = False

# khoi tao driver
driver = webdriver.Firefox(options=options, service=ser)

# Tao url
url = 'https://pythonscraping.com/pages/files/form.html'

# Truy cap
driver.get(url)

# Tam dung 2s
time.sleep(2)

first_name = driver.find_element(By.XPATH, "//input[@name='firstname']")
last_name = driver.find_element(By.XPATH, "//input[@name='lastname']")

first_name.send_keys('Thi Thu Ngan')
time.sleep(1)
last_name.send_keys('Nguyen')

time.sleep(2)
button = driver.find_element(By.XPATH, "//input[@type='submit']")
button.click()
time.sleep(5)

driver.quit()





