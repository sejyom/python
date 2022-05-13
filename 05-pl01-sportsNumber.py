#스포츠 종목과 팀원 수를 리스트로 적절히 출력

sports=['축구', '야구', '농구', '배구']
num=[11, 9, 5, 6]
print(sports)
print(num)
print()

#위 두 리스트로 출력
print('위 두 리스트로 출력')
for i in range(len(sports)):
    print('%s: %d명' % (sports[i], num[i]), end=' ')
print()
print()

#2차원 리스트로 생성 후 출력
print('2차원 리스트로 출력')
sptNum=[sports, num]
for i in range(len(sptNum[0])): # len(sptNum[0]) = 4 (0~3)
    print('%s: %d명' % (sptNum[0][i], sptNum[1][i]), end=' ')
print()
print()

#다른 구조의 2차원 리스트 생성을 컴프리헨션으로 처리
sptNum2=[[sports[i], num[i]] for i in range(len(sports))]
print(sptNum2)
print()
print()

#위 리스트에서 출력
for one in sptNum2:
    print('%s: %d명' % (one[0], one[1]), end=' ')
