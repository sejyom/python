# 한 줄에 하나씩 n부터 1 출력

n = int(input(''))

if n>100000 or n<1:
    print('잘못된 입력입니다.')
else:
    while True:
        print(n)
        n-=1
        if n==0:
            break
