# 1에서 45까지 6개의 수를 맞히는 로또
import random
winNum = 11, 17, 28, 30, 33, 35
count=0
print(' 모의 로또 당첨 번호 '.center(28, '='))
print(winNum)
print()
print('내 번호 확인 '.center(20, '-'))


for i in range(6):
    n = random.randint(1, 45)
    if n in winNum:
        print('%d O' % n, end = ' ')
        count+=1
    else:
        print('%d X' % n, end = ' ')

print()
print(count, '개 맞음')
