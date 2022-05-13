# 다양한 문자열 슬라이싱

str = '일요일 기러기'
print(str[:3], str[4:])
print(str[:-4], str[-3:])
print(str[:], str[::], str[::1])
print(str[::2]) # 한문자씩 건너뛰기
print(str[::3]) # 두문자씩 건너뛰기
print(str[::-2]) # 역순으로 한 문자씩 건너뛰기
print(str[::-1]) # 역순으로 출력
