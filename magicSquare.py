#마방진 만들기
#n, r, c, row, col, digit, table[][]

int table[15][15]=0

n = int(input('마방진 크기: '))
for i in range(n):
    for j in range(n):
        table[i][j]=0

r=0; c=(n-1)/2 # 첫 행의 중앙 열을 1로

digit=2
for digit in range(n*n):
    row=n-1; col=n-1
    if row<0:
        r=n-1
    if col<0:
        c=n-1
    if table[r][c]: # true면 이미 값이 있음
        r+=1
    else:
        c=col; r=row
    table[r][c]=digit

for r in range(n):
    for c in range(n):
        print(table[r][c])
    print()
        
