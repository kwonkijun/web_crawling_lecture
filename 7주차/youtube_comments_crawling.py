from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import openpyxl
import os

driver = webdriver.Chrome(r"C:\chromedriver.exe")
driver.get("https://www.youtube.com/watch?v=hVSR02uY7zE")
time.sleep(3)

# 엑셀 저장 경로
save_path = r"C:\Users\스타트코딩\Desktop\웹크롤링\7주차\유튜브_댓글_결과.xlsx"

# 엑셀 생성
if not os.path.exists(save_path):
	openpyxl.Workbook().save(save_path)

# 엑셀 불러오기
workbook = openpyxl.load_workbook(save_path)

# 시트 불러오기
sheet = workbook['Sheet']

# 스크롤 끝까지 내리기
SCROLL_SCRIPT = 'return document.documentElement.scrollHeight'

last_height = driver.execute_script(SCROLL_SCRIPT)

while True:
    # 맨 아래로 스크롤을 내린다.
    driver.find_element_by_css_selector("body").send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(1)

    # 현재 스크롤 높이
    new_height = driver.execute_script(SCROLL_SCRIPT)
    print(f"{last_height} {new_height}")

    if new_height == last_height:
        break

    last_height = new_height

time.sleep(4)
# 데이터 가져오기
nicknames = driver.find_elements_by_css_selector("#author-text > span")
comments = driver.find_elements_by_css_selector("#content-text")

for i in range(len(nicknames)):
    sheet[f'A{i+1}'] = nicknames[i].text
    sheet[f'B{i+1}'] = comments[i].text

workbook.save(save_path)