import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/'
response = requests.get(url)
response.raise_for_status()

html = response.text
soup = BeautifulSoup(html, 'html.parser')

prices = soup.select('ul#exchangeList span.value')

for price in prices:
    print(price.text)