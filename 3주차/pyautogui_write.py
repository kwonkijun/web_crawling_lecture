import pyautogui
import time
import pyperclip

time.sleep(3)

# 문자입력
# pyautogui.write("Hello world!", interval=0.25)

# 키 입력
pyautogui.press("enter")
# pyautogui.write("안녕하세요?")

# 클립보드에 복사
pyperclip.copy("안녕하세요?")

# 붙여넣기 
# pyautogui.keyDown("ctrl")
# pyautogui.press("v")
# pyautogui.keyUp("ctrl")

pyautogui.hotkey("ctrl", "v")