# 1개월 달력 출력

dates = int(input('최대 일수 입력 >> '))
day = int(input('첫 날 1일의 시작 요일 >> (0일, 1월, 2화 , ... , 6토)'))
day %= 7

# 요일 출력
for lcv in '일월화수목금토':
    print('%s' % lcv, end = ' ')
else:
    print()


cnt = 0
# 빈 공간 출력
if day != 0:
    print('   ' * day)

# 1일부터 말일까지 출력
for i in range(1, dates+1):
    print('%2d' % i, end = ' ')
    cnt += 1
    if cnt % 7 == 0:
        print()
else:
    print()



