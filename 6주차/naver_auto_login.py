from selenium import webdriver
import time
import credentials
import pyperclip
import pyautogui

driver = webdriver.Chrome(r'C:\chromedriver.exe') 

url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
driver.get(url)

# id 입력
driver.find_element_by_css_selector("#id").click()
pyperclip.copy("아이디") # 아이디를 클립보드에 복사
pyautogui.hotkey("ctrl", "v") # ctrl + v 동시에 누르기
time.sleep(1)

# pw 입력
driver.find_element_by_css_selector("#pw").click()
pyperclip.copy("패스워드")
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

# 로그인 버튼 클릭
driver.find_element_by_css_selector("input.btn_global").click()