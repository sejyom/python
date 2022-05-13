#강좌 정보로 구성된 딕셔너리 생성과 참조

lect = dict() # 빈 딕셔너리 생성
lect['강좌명']='파이썬 기초'
lect['개설년도']=[2020, 1] # value가 리스트
lect['학점시수']=(3, 3) # value가 튜플
lect['교수']='김민국'
print(lect)
print(len(lect))
print()

#딕셔너리의 항목 참조
print(lect['개설년도'], lect['학점시수'])
print(lect['강좌명'], lect['교수'])
