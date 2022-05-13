#중국집에서 음식 주문하기

food=['짜장면', '짬뽕', '우동', '울면']
print(food)

#탕수육 주문 추가
food.append('탕수육')
print(food)

#잠뽕을 굴짬뽕으로 주문 변경
food[food.index('짬뽕')]='굴짬뽕'
print(food)

#우동을 물만두로 주문 변경
food[food.index('우동')]='물만두'
print(food)
