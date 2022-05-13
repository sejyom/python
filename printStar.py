'''
for문 >>
n = int(input())
for i in range(1, n+1):
    print('*' * i) '''

#comprehension 코드
[print('*' * i) for i in range(1, int(input())+1)]
