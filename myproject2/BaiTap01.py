from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Tạo dataframe rỗng để lưu dữ liệu
d = pd.DataFrame({'Name of brand': [], 'year active': []})

# Khởi tạo webdriver
driver = webdriver.Chrome()

url = 'https://en.wikipedia.org/wiki/Lists_of_musicians'
driver.get(url)

time.sleep(3)

# Tìm tất cả các thẻ ul trên trang
ul_tags = driver.find_elements(By.TAG_NAME, "ul")

# Lặp ul_tags tìm lk chứa "List of" và bd = chữ "A"
musician_links = []

for ul in ul_tags:
    li_tags = ul.find_elements(By.TAG_NAME, "li")

    # Lặp li_tags tìm thẻ a
    for li in li_tags:
        try:
            a_tag = li.find_element(By.TAG_NAME, "a")
            link_text = a_tag.text
            link_href = a_tag.get_attribute("href")

            # Ktra nếu văn bản liên kết chứa "List of" và bd vs chữ "A"
            if "List of" in link_text and link_text.startswith("List of A"):
                musician_links.append(link_href)
                print(f"Thêm link: {link_href}")
        except:
            continue

# Lấy các liên kết từ danh sách
ul_tags = driver.find_elements(By.TAG_NAME, "ul")
print(len(ul_tags))

ul_artist = ul_tags[21]  # list start with index=0

# Lay ra tat ca the <li> thuoc ul_ảtist
li_tags = ul_artist.find_elements(By.TAG_NAME, "li")

# Tao ds cac url
links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href") for tag in li_tags]

#Xuat thong tin
for link in links:
    print(link)

# Truy cập lk first
url1 = driver.get(links[0])
ul1_tags = driver.find_elements(By.TAG_NAME, "ul")
print(len(url))

ul_artist = ul1_tags[21]  # list start with index=0

# Lay ra tat ca the <li> thuoc ul_artist
li1_tags = ul_artist.find_elements(By.TAG_NAME, "li")

# Tao ds cac url
artist_links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href") for tag in li1_tags]

for link1 in artist_links:
    print(link1)
    driver.get(link1)
    time.sleep(2)

    # Lấy tên ban nhạc
    try:
        band_name = driver.find_element(By.TAG_NAME, "h1").text
    except:
        band_name = ""

    # Lấy thời gian hoạt động
    try:
        years_active = driver.find_element(By.XPATH,
                                           "//th[span[text()='Years active']]/following-sibling::td").text
    except:
        years_active = ""

    # Tạo
    artist = {'Name of brand': band_name, 'year active': years_active}
    artist_df = pd.DataFrame([artist])

    # Kết hợp vào dataframe chính
    d = pd.concat([d, artist_df], ignore_index=True)

# Xuất dữ liệu ra excel
d.to_excel('musicians.xlsx', index=False) #index =false: để kh lưu chỉ số
print("Đã xuất dữ liệu ra file 'musiciannhap.xlsx'")



# Đóng trình duyệt
driver.quit()