#1에서 20까지의 난수 5개를 두 번 얻어서 집합 변수 A B에 저장하고
#각각 합집합과 교집합, 차집합, 여집합을 구하여 출력하는 프로그램

from random import sample

a=set(sample(list(range(1,21)),5))
b=set(sample(list(range(1,21)),5))

print('A = {}'.format(a))
print('B = {}'.format(b))

#합집합 union(), update()
print('A | B = {}'.format(a|b))
#교집합 intersection()
print('A & B = {}'.format(a&b))
#차집합 difference()
print('A - B = {}'.format(a-b))
#여집합 symmetric_difference()
print('A ^ B = {}'.format(a^b))
