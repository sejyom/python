# 10진수 정수를 입력받아 2진수, 8진수, 10진수, 16진수 출력

data = int(input('정수 입력 >> '))
print('2진수 ', bin(data))
print('8진수 ', oct(data))
print('10진수 ', data)
print('16진수 ', hex(data))
