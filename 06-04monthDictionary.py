#1월에서 9월의 영어 단어로 구성되는 딕셔너리
month=dict()
month={1:'january', 2:'fabuary', 3:'march', 4:'april'}
month[5]='may'
month[6]='june'
month[7]='july'
month[8]='august'
month[9]='september'
print(month)
print()

from random import randint
#임의로 월 단어 5번 출력
for i in range(5):
    r = randint(1, 9)
    print('%d: %s' % (r, month[r]))
