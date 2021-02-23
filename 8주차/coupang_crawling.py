# 2021.02.23 
# by startcoding
# 쿠팡 크롤러 (멘토링 프로그램)

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# requests 만으로 크롤링 가능하다 

url = 'https://www.coupang.com/np/search?q=%EA%B3%A0%EC%B6%94%EC%9E%A5&page=1' # 고추장으로 검색했을 때의 URL

response = requests.get(url, headers={'User-Agent' : 'Mozilla/5.0'})
response.raise_for_status()
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# li 태그로 상품리스트 요소를 가져온다 
items = soup.select("ul#productList > li")

# 결과데이터가 담길 리스트
result = []

for i, item in enumerate(items, 1): # enumerate 함수는 구글에서 사용법을 찾아 보세요. (몇 번째 반복인지 나타내기 위함)

    # 광고 상품인 경우 제외
    if len(item.select("span.ad-badge")) > 0:
        print("광고상품입니다.")
    else:
        # 일반 상품인 경우

        # 상품의 a태그를 가져와서 상세페이지 url을 수집한다
        a = item.select_one("a.search-product-link")
        sub_url = "https://www.coupang.com/" + a.attrs['href']
        
        # 제품의 가격은 상세페이지 안에서 가져오기가 힘들다 -> 상세페이지 가기전에 저장해 놓기
        product_price = item.select_one("strong.price-value").text

        # 상세페이지로 request 요청
        response = requests.get(sub_url, headers={'User-Agent' : 'Mozilla/5.0'})
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
        # 브랜드이름은 데이터가 없는 경우가 있음 (그래도 태그는 존재해서 오류가 발생X)
        brand_name = soup.select_one("a.prod-brand-name").text
        product_name = soup.select_one("h2.prod-buy-header__title").text
        print(i, brand_name, product_name, product_price, sub_url)
        result.append([brand_name, product_name, product_price, sub_url])

# DataFrame 사용법과 csv 파일 저장은 구글 검색으로 찾아보세요
cur = datetime.now().strftime("%Y-%m-%d")
filename = f'쿠팡조회결과_{cur}.csv'
df = pd.DataFrame(result, columns=['brand_name', 'product_name', 'product_price', 'sub_url'])
df.to_csv(filename, index=False, encoding='euc-kr')