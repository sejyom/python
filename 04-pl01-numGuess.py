# 1에서 10 사이의 수 맞히기

import random
n = random.randint(1, 10)

print('1에서 10 사이의 수 무얼까요무얼까요무얼까요 ')

while True:
    user = int(input())
    if n == user:
        print('%d 빙고!!' % n)
        break
    else:
        print('땡!!')
        if user < n:
            print('정답 숫자가 더 커요')
        else:
            print('정답 숫자가 더 작아요')
        continue
print('축하합니다!!')
