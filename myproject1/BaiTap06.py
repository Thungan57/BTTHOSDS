import re

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd


# 1.Tao dataframe rong
all_links = []
d = pd.DataFrame({'name': [], 'birth': [], 'death': [], 'nationality': []})

###############################################################################

# 2. Khoi tao webdriver
driver = webdriver.Chrome()

for i in range(65, 91):
    url = "https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22" + chr(i) + "%22"
    try:
        # Mở trang
        driver.get(url)

        # Đợi một chút để trang tải
        time.sleep(3)

        # Lay ra tat cac ca the ul
        ul_tags = driver.find_elements(By.TAG_NAME, "ul")
        print(len(ul_tags))

        # Chon the ul thu 21
        ul_painters = ul_tags[20]  # list start with index=0

        # Lay ra tat ca the <li> thuoc ul_painters
        li_tags = ul_painters.find_elements(By.TAG_NAME, "li")

        # Tao danh sach cac url
        links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href") for tag in li_tags]
        all_links.extend(links)
    except Exception as e:
        print(f"Error at letter {chr(i)}: {e}")


######################################################
# III. Lay thong tin cua tung hoa si

for link in all_links:

    try:
        # Khoi tao webdriver
        #driver = webdriver.Chrome()
        # Mo trang
        #url = link
        driver.get(link)

        # Doi 2 giay
        time.sleep(2)

        # Lay ten hoa si
        try:
            name = driver.find_element(By.TAG_NAME, "h1").text
        except:
            name = ""
        # Lay ngay sinh
        try:
            birth_element = driver.find_element(By.XPATH, "//th[text()='Born']/following-sibling::td")
            birth = birth_element.text
            birth = re.findall(r'[0-9]{1,2} +\s+[A-Za-z]+\s+[0-9]{4}', birth)[0]  # regex
        except:
            birth = ""
        # Lay ngay mat
        try:
            death_element = driver.find_element(By.XPATH, "//th[text()='Died']/following-sibling::td")
            death = death_element.text
            death = re.findall(r'[0-9]{1,2} +\s+[A-Za-z]+\s+[0-9]{4}', death)[0]
        except:
            death = ""
        # Lay quoc tich
        try:
            nationality_element = driver.find_element(By.XPATH, "//th[text()='Nationality']/following-sibling::td")
            nationality = nationality_element.text
        except:
            nationality = ""

        # Tao dictionary thong tin cua hoa si
        painter = {'name': name, 'birth': birth, 'death': death, 'nationality': nationality}

        # CHuyen doi dictionary thanh DataFrame
        painter_df = pd.DataFrame([painter])

        # Them thong tin vao DF chinh
        d = pd.concat([d, painter_df], ignore_index=True)

    except Exception as e:
        print(f"Error with link {link}: {e}")

####################################################

#4. In thong tin
print(d)

file_name = 'Painters.xlsx'

# saving the excel
d.to_excel(file_name, index = False) #index =false: để kh lưu chỉ số
print('DataFrame is written to Excel File successfully.')

driver.quit()

