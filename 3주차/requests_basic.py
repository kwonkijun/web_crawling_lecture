import requests
from bs4 import BeautifulSoup

response = requests.get("https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC")

# 응답코드 가져오기 
response.raise_for_status() # 통신이 정상적으로 이루어 졌을 때만 다음 코드를 실행

# HTML 코드 가져오기
html = response.text

# BeautifulSoup 로 예쁘게 만들기 
soup = BeautifulSoup(html, 'html.parser')

# soup 출력해보기
# print(soup.prettify())

# 원하는 요소 출력하기
title = soup.select("dl > dt > a")
print(title)