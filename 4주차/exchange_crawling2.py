import requests
from bs4 import BeautifulSoup
import pyautogui

# menu = int(pyautogui.prompt(text='국가선택 1. 미국 2. 일본 3. 유럽 4. 중국', title='국가선택'))
# user_price = float(pyautogui.prompt(text='금액을 입력하세요 : 단위(원)', title='금액입력'))

url = 'https://finance.naver.com/marketindex/'
response = requests.get(url)
response.raise_for_status()

html = response.text
soup = BeautifulSoup(html, 'html.parser')

prices = soup.select('ul#exchangeList span.value')
print(prices)
# result = user_price / float(prices[menu-1].text.replace(',', ''))

# print(result)