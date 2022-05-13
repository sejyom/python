# 번호로 버거 메뉴 주문받기

menu = '''버거, 콤보 번호로 주문하세요!
    0. 주문 종료
    1. 올인원팩
    2. 투게더팩
    3. 트리오팩
    4. 패밀리팩
        >> '''
boolean = 1

while boolean:
     select = int(input(menu))
     if select == 1:
         print('%s 주문' % '올인원팩')
     elif select == 2:
         print('%s 주문' % '투게더팩')
     elif select == 3:
         print('%s 주문' % '트리오팩')
     elif select == 4:
         print('%s 주문' % '패밀리팩')
     elif select == 0:
         print('주문종료')
         boolean == 0
     else:
         print('???')
        
