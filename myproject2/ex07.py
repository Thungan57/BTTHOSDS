from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas




# Khởi tạo driver cho Chrome
driver = webdriver.Chrome()

# Tạo url
url = 'https://gochek.vn/collections/all'

# Truy cập trang web
driver.get(url)


time.sleep(2)


links = driver.find_elements(By.XPATH, "//div[@class='content-product-list product-list filter clearfix']//div[@class='box-pro-detail']/h3/a")

# Lưu tất cả các liên kết sản phẩm
list_links = []
for l in links:
    link = l.get_attribute("href")
    list_links.append(link)

# In ra danh sách liên kết sản phẩm
sanpham =[]
# Lặp qua từng trang chi tiết sản phẩm để lấy thông tin
for link in list_links:
    driver.get(link)
    time.sleep(2)

    # Lấy thông tin sản phẩm
    try:
        tsp = driver.find_element(By.XPATH, "//div[@class='product-title']/h1").text
    except:
        tsp = ""

    try:
        sale = driver.find_element(By.XPATH, "//div[@class='product-price']/span[@class='pro-sale']").text
    except:
        sale = ""

    try:
        price_sale = driver.find_element(By.XPATH, "//div[@class='product-price']/span[@class='pro-price']").text
    except:
        price_sale = ""

    try:
        price_origin = driver.find_element(By.XPATH, "//div[@class='product-price']/del").text
    except:
        price_origin = ""

    sanpham.append({'link sản phẩm': link, 'tên sản phẩm': tsp, 'giá khuyến mãi': price_sale, 'giá gốc': price_origin, 'giảm giá': sale })


sanpham_df = pandas.DataFrame(sanpham)

#lưu thành file excel
a = "gocheck.xlsx"
sanpham_df.to_excel(a, index=False)
driver.quit()