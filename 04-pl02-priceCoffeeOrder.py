# 커피 주문받아 주문 가격 표시

menu = '''Coffee menu!
    1. 아메리카노 2000
    2. 카페라떼 2500
    3. 카푸치노 3000
    4. 카라멜마끼아또 4000
    0. 주문종료 >>'''

print(menu)

while True:
    n = int(input('번호 입력 >> '))
    if n == 1:
        ame1 = int(input('아메리카노 몇 잔?? >> '))
        americano = ame1 * 2000
        continue
    elif n == 2:
        cafe2 = int(input('카페라떼 몇 잔?? >> '))
        cafelatte = cafe2 * 2500
        continue
    elif n == 3:
        capu3 = int(input('카푸치노 몇 잔?? >> '))
        capuccino = capu3 * 3000
        continue
    elif n == 4:
        caramel4 = int(input('카라멜마끼아또 몇 잔?? >> '))
        caramelMacchiato = caramel4 * 4000
        continue
    elif n == 0:
        price = americano+cafelatte+capuccino+caramelMacchiato
        print('주문 끝!! 총 가격: %d' % price)
        break
    
        
        
