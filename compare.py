lst=input('두 수를 공백 단위로 나누어 입력하세요 >>').split()
a=int(lst[0])
b=int(lst[1])

if a>b:
    print('%d > %d' % (a, b))
elif a<b:
    print('%d < %d' % (a, b))
else:
    print('%d == %d' % (a, b))
    
