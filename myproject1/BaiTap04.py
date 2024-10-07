from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#khởi tạo Webdriver
driver = webdriver.Chrome()

for i in range(65, 91):
    url = "https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22"+chr(i)+"%22"
    try:
        # Mở trang
        driver.get(url)  # de mo

        # đợi khaongr chừng 2s
        time.sleep(2)

        # lay all cac the <ul>
        ul_tags = driver.find_elements(By.TAG_NAME, "ul")
        print(len(ul_tags))

        # Chon thẻ ul thứ 21
        ul_painters = ul_tags[20]  # list start with index =0

        # lay ra all the <li> thuoc ul_painters
        li_tags = ul_painters.find_elements(By.TAG_NAME, "li")

        # tao ds cac url
        titles = [tag.find_element(By.TAG_NAME, "a").get_attribute("title") for tag in li_tags]

        # in ra
        for title in titles:
            print(title)
    except:
        print("Error")


#Dong website
driver.quit()