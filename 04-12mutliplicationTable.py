# 구구단 출력

for i in range(2,10):
    print('%d단' % i)
    for j in range(1,10):
        print('%d * %d = %d' % (i, j, i*j), end=' ')
    print()
