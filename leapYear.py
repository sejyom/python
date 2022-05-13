year=int(input())

if year%4==0 and not year%100: #4의 배수면서 100의 배수가 아닐 때
    print('1')
elif year%4==0 and year%400==0:
    print('1')
else:
    print('0')
