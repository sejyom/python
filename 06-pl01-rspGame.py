#철수와 영희의 가위바위보 게임

#이기는 패 : 지는 패
dcs=dict(가위='보오', 바위='가위', 보오='바위')

#주요 출력 단어로 구성된 리스트
tit=['비김', '영희', '철수', '승자']

#rock scissors paper(tuple)
rsp=('가위', '바위', '보오')

print('*'*17)
print('{:^5} {:5} {:5}'.format(tit[1], tit[2], tit[3]))
print('*'*17)

from random import choice

for _ in range(10):
    yh=choice(rsp)
    cs=choice(rsp)

    print('{:^4} {:4}'.format(yh, cs), end='  ')

    if yh==cs:
        index=0
    elif dcs[yh]==cs:
        index=1
    else:
        index=2

    print('{:4}'.format(tit[index]))
