# 할인율에 따른 할인 가격

price = int(input('총 가격 입력 >> '))

rate1 = (10000 <= price < 20000) * 0.01
rate2 = (20000 <= price < 40000) * 0.02
rate3 = (40000 < price) * 0.04
rate = rate1+rate2+rate3
discount = price * rate
pay = price - discount

print('할인된 가격:', pay)
print('할인율:', rate)
print('할인액:', discount)
