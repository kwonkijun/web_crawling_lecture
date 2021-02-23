# 2021.02.23 
# by startcoding
# RISS 사이트(국내외 학술 논문 사이트) 크롤러 (멘토링 프로그램)

from bs4 import BeautifulSoup
import pyautogui
from selenium import webdriver
import time

keyword = pyautogui.prompt(title="논문검색", text="검색어를 입력하세요:")


# 사이트의 URL이 복잡하다 -> 파라미터를 제거 또는 추가해 가면서 테스트하기 
url = f"http://riss.kr/search/Search.do?&pageNumber=1&query={keyword}&colName=re_a_kor&pageScale=10&iStartCount=0" 

# 필요한 파라미터 종류 
# query : 키워드
# colName : 논문 구분 
# pageScale : 페이지 요청개수 
# iStartCount : 페이지 시작넘버 

# 상세페이지로 들어갈 경우 동적으로 데이터를 가져오기 때문에 Selenium을 사용한다
driver = webdriver.Chrome(r"C:\chromedriver.exe")
driver.get(url)
time.sleep(4)

# 상세페이지로 들어갈 링크들을 수집
links = driver.find_elements_by_css_selector("div.srchResultListW p.title > a")

sub_urls = []
for link in links:
    sub_urls.append(link.get_attribute('href'))


for sub_url in sub_urls:
    driver.get(sub_url)
    time.sleep(4)

    # Selenium 에서 Beautifulsoup 사용하기 (크롤링 속도 및 텍스트 데이터 가져오기가 용이)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one("div.thesisInfoTop > h3.title").get_text(strip=True)
    title = " ".join(title.split()) # 제목에서 중간 공백을 제거할 때
    
    # 부가정보는 0~3개 까지 있다 국문초록, 다국어초록, 목차
    # 부가정보(전체내용)은 div.text.off 안에 있다
    add_infos = soup.select("div.text.off")

    total_add_info = "" # 부가정보를 합치기 위한 변수

    # 부가정보가 있을 경우, for 문을 돌면서 합쳐준다.
    if len(add_infos) > 0:
        for add_info in add_infos:
            total_add_info += add_info.get_text(strip=True) + "\n"

    print(f'제목 : {title}\n\n')
    print(f'부가정보 : {total_add_info}')