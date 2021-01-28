import requests
from bs4 import BeautifulSoup

url = "https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC"

response = requests.get(url)
response.raise_for_status()
html = response.text

soup = BeautifulSoup(html, 'html.parser')
title = soup.select_one('dl > dt > a').text
date = soup.select_one('dd.txt_inline').text
content = soup.select_one('dd:nth-child(3)').text

print(title, date, content)