import re

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Tao dataframe rong
d = pd.DataFrame({'name': [], 'birth': [], 'death': [], 'nationality': []})

#Khoi tao webdriver
driver = webdriver.Chrome()

#Mo trang
url = "https://en.wikipedia.org/wiki/Edvard_Munch"
driver.get(url)

#doi 2s
time.sleep(2)

#Lay ten hoa si
try:
    name = driver.find_element(By.TAG_NAME, "h1").text  #h1 lay o ktra ben ten
except:
    name = " "


#Lay ngay sinh
try:
    birth_element = driver.find_element(By.XPATH, "//th[text()='Born']/following-sibling::td")  # //:tuong doi  following-sibling:chuyển sang tk kế bên
    birth = birth_element.text
    birth = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}', birth)[0]  #\s: space khoang trang

except:
    birth = " "

# Lay ngay mat
try:
    death_element = driver.find_element(By.XPATH, "//th[text()='Died']/following-sibling::td")  # //:tuong doi  following-sibling:chuyển sang tk kế bên
    death = death_element.text
    death = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}', death)[0]  # \s: space khoang trang
                            #co 1 so hoac 2              namsinh 4 so
except:
    death = " "

# Lay nationality
try:
    nationality_element = driver.find_element(By.XPATH, "//th[text()='Nationality']/following-sibling::td")  # //:tuong doi  following-sibling:chuyển sang tk kế bên
    nationality = nationality_element.text

except:
    nationality = " "

# Tao dictionary thong tin cua hoa si
painter = {'name': name, 'birth': birth, 'death': death, 'nationality':nationality}

#Chuyen doi dictionary thanh Dataframe
painter_df = pd.DataFrame([painter])

#Them thong tin vao DF chinh
d = pd.concat([d, painter_df], ignore_index=True)

#in ra DF
print(d)

#Dong webdriver
driver.quit()