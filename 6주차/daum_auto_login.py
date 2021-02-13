from selenium import webdriver
import time
import credentials

driver = webdriver.Chrome(r'C:\chromedriver.exe')

url = "https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F"
driver.get(url)

# id 입력 
driver.find_element_by_css_selector("#id").send_keys("아이디")
# id = driver.find_element_by_css_selector("#id")
# id.send_keys("kkj63691126")
time.sleep(1)

# pw 입력
driver.find_element_by_css_selector('#inputPwd').send_keys("패스워드")
time.sleep(1)

# 로그인 버튼 클릭
driver.find_element_by_css_selector("#loginBtn").click()
