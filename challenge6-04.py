#철수와 영희의 가위바위보 게임
#가위바위보 게임의 회수는 20으로 하고 매번 승자의 승리 회수 또는 비긴 회수 출력
#마지막에는 비긴 회수와 각각의 승률이 출력

#이기는 패 : 지는 패
dcs=dict(가위='보오', 바위='가위', 보오='바위')

#주요 출력 단어로 구성된 리스트
tit=['비김', '영희', '철수', '승자']

#rock scissors paper(tuple)
rsp=('가위', '바위', '보오')

#승리 횟수를 저장
cnt={tit[0]:0, tit[1]:0, tit[2]:0}


print('*'*17)
print('{:^5} {:^5} {:^5}'.format(tit[1], tit[2], tit[3]))
print('*'*17)

from random import choice

for _ in range(20):
    yh=choice(rsp)
    cs=choice(rsp)

    print('{:4} {:4}'.format(yh, cs), end=' ')

    if yh==cs: #비긴 경우
        index=0
        
    elif dcs[yh]==cs: #영희가 이긴 경우
        index=1

    else: #철수가 이긴 경우
        index=2
    cnt[tit[index]]+=1 #이긴 경우의 인덱스값을 찾아 +1

    print('{:^5}{}'.format(tit[index], cnt[tit[index]]))

print()
print('총 게임 회수: %d 비긴 회수: %d' % (20, cnt[tit[0]]))
vgame=cnt[tit[1]]+cnt[tit[2]]

print('철수 승률: {:.2f}'.format(cnt[tit[2]]/vgame))
print('영희 승률: {:.2f}'.format(cnt[tit[1]]/vgame))
