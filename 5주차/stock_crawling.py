import requests
from bs4 import BeautifulSoup
import openpyxl

# 1. 엑셀 파일 불러오기 
book = openpyxl.load_workbook(r"C:\Users\스타트코딩\Desktop\웹크롤링\5주차\주가정보크롤링_결과.xlsx")

# 2. sheet 불러오기
sheet = book['Sheet1']
codes = ['005930', '066570', '000660']


for i in range(len(codes)):
    url = f'https://finance.naver.com/item/sise.nhn?code={codes[i]}'
    response = requests.get(url)
    response.raise_for_status()
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one('strong#_nowVal').text
    
    # 3. 데이터 저장
    sheet[f'C{i + 3}'] = price
    
    # 4. 엑셀 저장
    book.save(r"C:\Users\스타트코딩\Desktop\웹크롤링\5주차\주가정보크롤링_결과.xlsx")
    


