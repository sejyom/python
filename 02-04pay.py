#식당에서 식비 지불하기와 잔돈받기

#78000원

# 오만원권 구하기
print('오만원권')
print(78000 // 50000)
pay = 78000 % 50000

# 만원권 구하기
print('만원권')
print(pay // 10000)
pay = pay % 10000

# 오천원권 구하기
print('오천원권')
print((pay // 5000)+1)
pay = pay % 5000

# 거스름돈 구하기
print('거스름돈')
print(5000-pay,'원')
