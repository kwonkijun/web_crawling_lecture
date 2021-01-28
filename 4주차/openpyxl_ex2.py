import openpyxl

# 엑셀읽기
workbook = openpyxl.load_workbook(r'C:\Users\스타트코딩\Desktop\웹크롤링\4주차\result.xlsx')

# 시트 이름으로 불러오기
sheet = workbook['새로운시트']

# 셀 주소로 값 가져오기
title_a = sheet['A1'].value
title_b = sheet['B1'].value

print(title_a, title_b)