from selenium import webdriver
import time
import pyautogui
import random

driver = webdriver.Chrome(r'C:\chromedriver.exe')

keyword = pyautogui.prompt(text="해시태그를 입력하세요", title="Message")

LOGIN_URL = "https://www.instagram.com/accounts/login/?hl=ko"
USER_ID = "아이디"
USER_PW = "비밀번호"

TAG_URL = f"https://www.instagram.com/explore/tags/{keyword}/?hl=ko"

driver.get(LOGIN_URL)
time.sleep(3)

# 아이디 입력
driver.find_element_by_name("username").send_keys(USER_ID)
time.sleep(1)

# 패스워드 입력
driver.find_element_by_name("password").send_keys(USER_PW)
time.sleep(1)

# 로그인버튼 클릭
driver.find_element_by_css_selector("div.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB").click()
time.sleep(3)

driver.get(TAG_URL)
time.sleep(4)

# 첫 포스팅 클릭
driver.find_element_by_css_selector("div.v1Nh3.kIKUG._bz0w > a").click()
time.sleep(2)

print("좋아요 작업중....")
while True:
    time.sleep(random.randint(2,4))
    # 좋아요 누르기
    driver.find_element_by_css_selector("span.fr66n > button.wpO6b").click()
    time.sleep(random.randint(2,4))

    # 다음 포스팅 화살표 클릭
    try:
        driver.find_element_by_css_selector("a._65Bje.coreSpriteRightPaginationArrow").click()
    except:
        print("마지막 포스팅입니다~!")
        break