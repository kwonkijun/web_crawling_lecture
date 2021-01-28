import openpyxl

# 워크북 생성
workbook = openpyxl.Workbook()

# 시트 생성
sheet = workbook.create_sheet("새로운시트")

# 시트에 데이터 입력
sheet['A1'] = '종목'
sheet['B1'] = '종목코드'

# 엑셀 저장 
workbook.save(r'C:\Users\스타트코딩\Desktop\웹크롤링\4주차\result.xlsx')