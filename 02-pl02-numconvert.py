# 가장 먼저 변환할 수가 2진수, 8진수, 10진수, 16진수 중에 무엇인지 입력받는다.
# 그런 다음, 표준 입력한 수의 2진수, 8진수, 10진수, 16진수를 출력하는 프로그램을 작성하자.

base = int(input('입력할 정수의 진수는?? '))
invar = input(str(base) + '진수 정수 입력 >> ')
data = int(invar, base) # 입력값을 base 진수로 변환'

print('2진수 ', bin(data))
print('8진수 ', oct(data))
print('10진수 ', data)
print('16진수 ', hex(data))

