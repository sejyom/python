# 표준 입력으로 두 개의 실수를 입력받아 더하기, 빼기, 곱하기, 나누기의 연산을 출력한다.
# 이후 다시 표준 입력으로 하나의 연산식을 한 줄에 입력받아 그 결과를 출력하는 프로그램을 작성해 보자.

num1 = float(input('숫자1 입력: '))
num2 = float(input('숫자2 입력: '))

print('sum = ', num1+num2)
print('sub = ', num1-num2)
print('mult = ', num1*num2)
print('div = ', num1/num2)

expression = input('연산식 입력: ')
print('연산식: ', expression, '결과: ', eval(expression))
