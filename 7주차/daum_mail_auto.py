from selenium import webdriver
import time
import pyautogui

driver = webdriver.Chrome(r'C:\chromedriver.exe')

url = "https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F"
driver.get(url)
driver.maximize_window() # 화면을 최대 크기로 만듬

# id 입력 
driver.find_element_by_css_selector("#id").send_keys("아이디")
time.sleep(1)

# pw 입력
driver.find_element_by_css_selector('#inputPwd').send_keys("비밀번호")
time.sleep(1)

# 로그인 버튼 클릭
driver.find_element_by_css_selector("#loginBtn").click()
time.sleep(2)

# 메일함으로 이동
driver.get("https://mail.daum.net")
time.sleep(3)

# 메일 쓰기 버튼 클릭
driver.find_element_by_css_selector("button.btn_comm.btn_write").click()
time.sleep(1)

# 받는사람 입력 (팝업창에 가려질 수 있다 - 오류 발생 시 팝업닫기 후 클릭하기)
sender = driver.find_element_by_css_selector("#toTextarea")
sender.click()
sender.send_keys("kkj63691126@daum.net")
time.sleep(2)

# 제목 입력
title = driver.find_element_by_css_selector("#mailSubject")
title.click()
title.send_keys("셀레니움")
time.sleep(2)

# 메일 내용 쓰기
# 프레임 전환
driver.switch_to.frame('tx_canvas_wysiwyg')
content = driver.find_element_by_css_selector("body.tx-content-container")
content.send_keys("정말 쉽고 재미있습니다~!")

# 원래 프레임으로 돌아가기
driver.switch_to.default_content()

# 메일 보내기 버튼 클릭
time.sleep(2)
driver.find_element_by_css_selector("button.btn_toolbar.btn_write").click()