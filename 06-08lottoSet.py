#로또 번호를 randrange()와 sample() 함수로 생성

from random import randrange
from random import sample

#randrange()함수와 집합을 이용, 중복제거
mylotto = set()
while len(mylotto)<6:
    num=randrange(1,46)
    print(num, end=' ')
    mylotto.add(num)
print()
print('집합: {}'.format(mylotto))
print('정렬리스트: {}'.format(sorted(mylotto)))

#sample()함수를 이용하면 매우 간편
lotto=sample(range(1,46),6)
print('집합: {}'.format(lotto))
print('정렬리스트: {}'.format(sorted(lotto)))
