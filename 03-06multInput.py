# 4개의 수를 입력받아 합, 평균값, 최댓값, 최솟값을 출력

a, b, c, d = input('공백 단위로 숫자 네개 입력 >> ').split()
a, b, c, d = int(a), int(b), int(c), int(d)
print('합 =', a+b+c+d)
print('평균값=', (a+b+c+d)/4)
print('최댓값 =', max(a, b, c, d))
print('최솟값 =', min(a, b, c, d))

