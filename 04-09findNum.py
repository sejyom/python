# 지정된 최소 한 자릿수가 포함된 두 자리 정수 찾기

num = input('10진수의 한 자릿수 입력 >> ')
# num's type: str

print(' 결 과 '.center(53, '='))

for i in range(10, 100):
    snum = str(i)
    if num in snum:
        print(i, end=' ')
