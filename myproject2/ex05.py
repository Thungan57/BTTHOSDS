import getpass

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import pandas as pd

# Duong dan den file thuc thi geckodriver
#gecko_path = "D:/OSDS/project2/geckodriver.exe"

# Kho to doi tuong dinh vu voi duong geckodriver
#ser = Service(gecko_path)

# Tao tuy chon
#options = webdriver.firefox.options.Options()
#options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"

# Thiet lap firefox chi hien thi giao dien
#options.headless = False

# khoi tao driver
#driver = webdriver.Firefox(options=options, service=ser)

driver = webdriver.Chrome()

# Tao url
url = 'https://www.reddit.com/login/'

# Truy cap
driver.get(url)
time.sleep(3)

# Nhập thông tin người dùng
my_email = input("Please provide your email:")
my_password = getpass.getpass('Please provide your password:')

# Dang nhap
#username_input = driver.find_element(By.XPATH, "//input[@id='login-username']")
#password_input = driver.find_element(By.XPATH, "//input[@id='login-password']")


# Nhan thong tin va nhan nut enter
#username_input.send_keys(my_email)
#password_input.send_keys(my_password + Keys.ENTER)
#time.sleep(5)




actionChains = ActionChains(driver)

time.sleep(1)

actionChains.key_down(Keys.TAB).perform()

time.sleep(1)

actionChains.key_down(Keys.TAB).perform()

time.sleep(1)

actionChains.key_down(Keys.TAB).perform()

time.sleep(1)

actionChains.key_down(Keys.TAB).perform()

time.sleep(1)

actionChains.key_down(Keys.TAB).perform()

time.sleep(1)

actionChains.send_keys(my_email).perform()

time.sleep(1)

actionChains.key_down(Keys.TAB).perform()

actionChains.send_keys(my_password + Keys.ENTER).perform()

# button_login = driver.find_element(By.XPATH,"//button[text()='Log in']")

# button_login.click()


time.sleep(30)

# Truy cap bai post bai
url2 = 'https://www.reddit.com/user/ThuNgan_57/submit/?type=TEXT'
driver.get(url2)
time.sleep(2)

for i in range(17):

    actionChains.key_down(Keys.TAB).perform()
    

actionChains.send_keys('Vi du post').perform()

actionChains.key_down(Keys.TAB).perform()

actionChains.send_keys('Thu Ngan'+Keys.ENTER).perform()

for i in range(4):
    actionChains.key_down(Keys.TAB).perform()
    time.sleep(1)

actionChains.key_down(Keys.ENTER).perform()

time.sleep(15)
driver.quit()
