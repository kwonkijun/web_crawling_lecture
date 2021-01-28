import requests
from bs4 import BeautifulSoup

# 삼성전자
# https://finance.naver.com/item/sise.nhn?code=005930

# LG전자
# https://finance.naver.com/item/sise.nhn?code=066570

codes = ['005930', '066570']

for code in codes:
    url = f'https://finance.naver.com/item/sise.nhn?code={code}'
    response = requests.get(url)
    response.raise_for_status()
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one('strong#_nowVal').text
    print(price)


