import requests
from bs4 import BeautifulSoup
import re

url = 'https://qiita.com/'

# 生のHTMLレスポンス
res = requests.get(url)

print(res.url)
print(res.text)
print(res.status_code)
print(res.__attrs__)

soup = BeautifulSoup(res.text, "lxml")

elements = soup.find_all(class_="css-2p454n")

for elem in elements:
    title = elem.text
    print(title)
