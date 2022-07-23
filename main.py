import requests
from bs4 import BeautifulSoup
import pandas as pd

header1 = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'}
cookies = dict(cookie='value')


# ดึงข้อมูล ดึง HTML ออกมาจาก browser
url = "https://www.amazon.com/s?bbn=16225016011&rh=n%3A16225016011%2Cp_89%3APlayStation&dc&qid=1658579518&rnid=2528832011&ref=lp_16225016011_nr_p_89_2"
req = requests.get(url, headers=header1, cookies=cookies).text

# สกัดข้อมูล นำ HTML มาสกัดข้อมูล
soup = BeautifulSoup(req, 'lxml')

namels = []
pricels = []


# ดึงข้อมูลที่ต้องการ
for i in soup.find_all('span', class_="a-size-medium a-color-base a-text-normal")[0:10]:
    name = i.text.strip()
    namels.append(name)

for i in soup.find_all('span', class_="a-offscreen")[0:10]:
    price = i.text.strip()
    pricels.append(price)

# เก็บข้อมูล บันทึกเป็นไฟล์
df = pd.DataFrame({'รายชื่อสินค้า': namels, 'ราคาสินค้า': pricels})
df.to_excel('Test.xlsx', index=False)