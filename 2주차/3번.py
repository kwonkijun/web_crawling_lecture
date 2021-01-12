# 문제3.
# 사용자로부터 두 숫자를 입력 받고
# 곱한 결과를 출력하기 

num1 = int(input("첫번째 숫자를 입력하세요")) # input 함수로 사용자로 부터 입력을 받을 수있다.
num2 = int(input("두번째 숫자를 입력하세요")) # 입력 받은 값은 문자열형태이므로 int함수로 형변환을 해준다. 

result = num1 * num2
print(result)