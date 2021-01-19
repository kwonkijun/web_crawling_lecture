import pyautogui

# confirm() : 확인창

select = pyautogui.confirm(text='계속하시겠습니까?', title='확인창', buttons=['OK', 'Cancel'])

if select == "OK":
    print("확인을 눌렀습니다.")
else:
    print("취소를 눌렀습니다.")

# prompt : 입력창

keyword = pyautogui.prompt(text="검색어를 입력하세요", title='입력창', default='3글자입력')

print(keyword)

# password : 패스워드 입력창

password = pyautogui.password(text="비밀번호를 입력하세요", title='패스워드 입력창', mask='*')

print(password)