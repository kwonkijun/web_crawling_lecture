import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt(text='검색어를 입력하세요', title='Message')
page = int(pyautogui.prompt(text='몇 페이지까지 크롤링 할까요?', title='Message'))

for i in range(1, page + 1):
    url = f"https://kin.naver.com/search/list.nhn?query={keyword}&page={i}"

    print(f'=================={i}번째 페이지 입니다.====================')
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