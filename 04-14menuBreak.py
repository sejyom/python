# 0에서 9까지의 수 중에서 7이 나오면 반복 종료

from random import randint
lucky = 7

while True:
    n = randint(0, 9)
    if n==lucky:
        print('end ')
        break
    else:
        print('%d' %n)
