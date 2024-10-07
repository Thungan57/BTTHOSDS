from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#khởi tạo Webdriver
driver = webdriver.Chrome()

#Mở trang
url = "https://en.wikipedia.org/wiki/List_of_painters_by_name"
driver.get(url)  #de mo

# đợi khaongr chừng 2s
time.sleep(2)

# lay all cac the <a> voi title chứa "List of painters"
tags = driver.find_elements(By.XPATH, "//a[contains(@title, 'List of painters')]")  #// là tương đối, tìm tất cả

#tao ra ds cac lien ket
links = [tag.get_attribute("href") for tag in tags]

#xuat thong tin
for link in links:
    print(link)

#dong webdriver
driver.quit()  # quit: thoát ra đường dẫn