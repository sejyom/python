#리스트로 편의점에서 구입할 품목 만들기

goods=[]

for _ in range(3): # 변수 i는 사용하지 않으므로 _ 사용 가능
    goods.append(input('구입할 항목은? '))
    print(goods)
print('길이: %d' % len(goods))
