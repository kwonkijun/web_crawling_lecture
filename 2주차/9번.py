# 5개의 문자열을 입력 받고
# 리스트에 저장하기
# 리스트에 저장된 내용 출력

title_list = []

for i in range(5):
    title = input("제목을 입력해주세요 >>>")
    title_list.append(title)

print(title_list)