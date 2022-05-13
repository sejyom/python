#가위바위보 리스트 항목 참조

from random import choice
rsp=['가위', '바위', '보']

#가위바위보 출력
for i in range(len(rsp)):
    print(rsp[i], end=' ')
print()
#가위바위보 5개
for i in range(5):
    print(choice(rsp), end=' ')
