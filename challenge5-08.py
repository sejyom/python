'''1에서 99까지의 난수 10개로 리스트를 만든 후, 다시 이 리스트를 튜플로 변환하고,
    다음과 같이 정렬된 리스트와 합, 항목수, 최대, 최소, 평균을 출력하는 프로그램을 작성하시오.'''

from random import randint

li = []
for i in range(10):
    li.append(randint(1, 99))
print('리스트: ', li)
tup = tuple(li)
print('튜플: ', tup)
print('튜플 정렬된 리스트: ', sorted(tup))
print()

print('합: %d, 항목수: %d' % (sum(tup), len(tup)))
print('최대: %d, 최소: %d, 평균: %.2f' % (max(tup), min(tup), (sum(tup)/len(tup))))
