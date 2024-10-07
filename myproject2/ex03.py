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
url = 'https://nhathuoclongchau.com.vn/thuc-pham-chuc-nang/vitamin-khoang-chat'

# Truy cap
driver.get(url)

# Tam dung 1s
time.sleep(1)

# Tim phan tu body cua trang de gui phim mui ten xuong
body = driver.find_element(By.TAG_NAME, "body")
time.sleep(3)

for k in range(10):
    try:
        # Lấy tất cả các button trên trang
        buttons = driver.find_elements(By.TAG_NAME, "button")

        # Duyệt qua từng button
        for button in buttons:
            # Kiểm tra nếu nội dung của button chứa "Xem thêm" và "sản phẩm"
            if "Xem thêm" in button.text and "sản phẩm" in button.text:
                # Di chuyển tới button và click
                button.click()
                break  # Thoát khỏi vòng lặp nếu đã click thành công

    except Exception as e:
        print(f"Lỗi: {e}")

# Nhan phim mũi tên xuống
for i in range(50):  #Lặp 49 lần mỗi lần cuộn xg 1 ít
    body.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.01)

# Tam dung them vai giau de trang tai hhet noi dung o cuoi tang
time.sleep(1)

#Tao cac list
stt = []
ten_san_pham = []
gia_ban =[]
hinh_anh = []

#Tim tat ca cac button có nội dung là " Chọn mua"
buttons = driver.find_elements(By.XPATH, "//button[text()='Chọn mua']")
print(len(buttons))



# Lay tung san pham
for i, sp in enumerate(buttons, 1):
    # Quay ngược 3 lần để tìm div cha
    parent_div = sp
    for _ in range(3):
        parent_div = parent_div.find_element(By.XPATH, "./..")  # Quay ngược 1 lần

    sp = parent_div


    # Lay ten sp
    try:
        tsp = sp.find_element(By.TAG_NAME, 'h3').text

    except:
        tsp = ''


    # Lay gia sp
    try:
        gsp = sp.find_element(By.CSS_SELECTOR, 'text-blue-5').text

    except:
        gsp = ''


    #Lay hinh anh
    try:
        ha = sp.find_element(By.CSS_SELECTOR, 'img').get_attribute('srcset')
    except:
        ha = ''


    # chi them vao ds neu co ten s
    if (len(tsp) > 0):
        stt.append(i)
        ten_san_pham.append(tsp)
        gia_ban.append(gsp)
        hinh_anh.append(ha)

# Tao df
df = pd.DataFrame({
    "STT": stt,
    "Ten san pham": ten_san_pham,
    "Gia ban": gia_ban,
    "Hinh anh": hinh_anh
})


#in ra excel
df.to_excel('Ds_sp_3.xlsx', index=False)

driver.quit()