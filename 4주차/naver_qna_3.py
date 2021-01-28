import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt(text='검색어를 입력하세요', title='Message')
url = f"https://kin.naver.com/search/list.nhn?query={keyword}"

response = requests.get(url)
response.raise_for_status()
html = response.text

soup = BeautifulSoup(html, 'html.parser')

lists = soup.select('ul.basic1 > li')

for li in lists:
    title = li.select_one('dl > dt > a').text
    date = li.select_one('dd.txt_inline').text
    content = li.select_one('dd:nth-child(3)').text
    print(title, date, content)