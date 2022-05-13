# 월을 입력받아 계절을 출력

user = int(input('월 입력 >> '))

if user == 4 or user == 5:
    print('%d월 봄' % user)
elif 6 <= user <= 8:
    print('%d월 여름' % user)
elif user == 9 or user == 10:
    print('%d월 가을' % user)
elif 1 <= user <= 3 or user == 11 or user == 12:
    print('%d월 겨울' % user)
else:
    print('%d월은 없어요' % user)
