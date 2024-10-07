from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


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
url = 'http://pythonscraping.com/pages/javascript/ajaxDemo.html'

# Truy cap
driver.get(url)

# in  ra noi dung cua trang web
print("Before: ===============================\n")
print(driver.page_source)

# Tam dung khoang 3s
time.sleep(3)

# In lai
print("\n\n\n\nAfter: =========================\n")
print(driver.page_source)

#Dong brower
driver.quit()
