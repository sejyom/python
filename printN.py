# 한 줄에 하나씩 1부터 n 출력

n = int(input(''))
lcv=1
if n>100000 or n<1:
    print('잘못된 입력입니다.')
else:
    while lcv<=n:
        print(lcv)
        lcv+=1
