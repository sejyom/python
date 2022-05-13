#햄버거 주문 구현
#콤보의 종류와 수량을 입력받음 -> 주문 내역과 가격, 총 주문 가격 출력
#0을 입력하면 주문 종료, 콤보 종류와 수량을 한 번에 입력받으면 주문 내역과 총 가격을 표시
#주문 종료시 총 주문 가격 출력
menu=('주문종료', '올인원팩', '투게더팩', '트리오팩', '패밀리팩')
price=(0, 6000, 7000, 8000, 10000)
msg='주문할 콤보 번호와 수량을 계속 입력하세요!'
for i in range(len(menu)):
    msg+='\n\t %d %s' % (i, menu[i])
    if i != 0:
        msg+= '%5d원 '% price[i]
print(msg)

total=0
pay=0
boolean = True
while(boolean):
    countSpace = input() #입력받기
    if countSpace.count(' ') >= 1: #입력 문자에 공백이 있는지
        food, num = countSpace.split() #공백단위로 나눠서 각각 food, num에 저장
        num=int(num) #num 자료형을 int로
        food=int(food)#food 자료형을 int로
        if 1 <= food <= 4 :#입력 문자가 1~4 중 하나인지
            pay = price[food]*num
            total+=pay
            print('%s %d개 %d원' % (menu[food], num, pay))
            print('총 가격: %d원' % total)
            print()
            
    elif countSpace.count(' ') == 0: #입력 문자에 공백이 없는지
        print('주문종료')
        boolean=False #시퀀스 종료
print('-' * 30)
print('총 주문 가격은 %d원 입니다.' % total)
print('-' * 30)
