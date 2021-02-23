import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# 네이버 쇼핑은 동적으로 상품데이터를 받아 온다 -> 셀레니움 사용하기 
url = "https://search.shopping.naver.com/search/all?query=%EB%B4%84%EC%98%B7&cat_id=&frm=NVSHATC" # 봄옷을 검색했을 때 URL 
driver = webdriver.Chrome(r"C:\chromedriver.exe")
driver.get(url)

time.sleep(3)

# 상품중 첫번째 이미지 요소 가져오기
img = driver.find_element_by_css_selector("div.thumbnail_thumb_wrap__1pEkS._wrapper > a > img")

# 이미지의 주소 저장하기
img_url = img.get_attribute('src')

# 이미지 주소로 requests 요청하기
response = requests.get(img_url)
response.raise_for_status()

# 이미지 파일로 저장하기
with open(r'C:\Users\스타트코딩\Desktop\웹크롤링\8주차\봄옷.jpg', 'wb') as f:
	f.write(response.content)