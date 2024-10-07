from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#khai bao webdriver
driver = webdriver.Chrome()

#mo mot  trang web
driver.get("http://gomotungkinh.com")
time.sleep(5)

#tìm phần tử img có id là "bonk"
bonk_img = driver.find_element(By.ID, "bonk")

#click liên tục vào img "bonk"

while True:
   bonk_img.click()
   print("Clicked on the bonk image")
   time.sleep(0.1)  #muốn càng nhanh càng giảm số xg
