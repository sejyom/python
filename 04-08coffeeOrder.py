# 3회에 걸쳐 커피 주문받기

for i in range(3):
    coffee = input('주문하세요! [아메리카노] [카페라떼] [카푸치노] >> ')
    if coffee == '아메리카노':
        print('%s 주문' % (coffee))
    elif coffee == '카페라떼':
        print('%s 주문' % coffee)
    elif coffee == '카푸치노':
        print('%s 주문' % coffee)
    else:
        print('%s는 없는 메뉴입니다.' % coffee)

else:
    print('주문 종료')
        
        
