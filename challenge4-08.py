# {난수} {사용자 입력 산술연산자} {사용자 입력 피연산자} = ?

from random import randint
num1 = randint(1, 100)
print('첫 값 >> ', num1)

while True:
    what = str(input('산술 연산 종류? >> '))
    if what not in '+-*/%':
        print(' 종료 '.center(15, '*'))
        break
    
    num2 = int(input('두 번째 값? >> '))

    if what == '+':
        print('%d %s %d = %d' % (num1, what, num2, num1+num2))
        print()
    elif what == '-':
        print('%d %s %d = %d' % (num1, what, num2, num1-num2))
        print()        
    elif what == '*':
        print('%d %s %d = %d' % (num1, what, num2, num1*num2))
        print()
    elif what == '/':
        print('%d %s %d = %d' % (num1, what, num2, num1/num2))
        print()
    elif what == '%':
        print('%d %s %d = %d' % (num1, what, num2, num1%num2))
        print()
