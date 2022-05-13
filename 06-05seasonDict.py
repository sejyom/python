#사계절의 영어 사전 생성과 항목 순회

season ={'봄':'spring', '여름':'summer', '가을':'autumn', '겨울':'winter'}
print(season.keys()) #season딕셔너리의 key값들만 뽑아냄(봄 여름 가을 겨울)
print(season.items()) #season딕셔너리의 key, value 값 모두 뽑아냄
print(season.values()) #season딕셔너리의 value값들만 뽑아냄(spring ~ winter)

#메소드 keys(), items()로 항목 순회
for key in season.keys():
    print('%s %s ' % (key, season[key]))

for item in season.items():
    print('{} {} '.format(item[0], item[1]), end=' ')
    #item[0]=keys() item[1]=values

print()

#메소드 items()의 반환 값인 튜플을 한 변수에 저장한 경우, 항목 순회 2
for item in season.items():
    print('{} {} '.format(*item), end=' ')
    #(*item) 의 *: 매개변수가 가변적이다!! 하나일수도 두개일수도 세개일수도...
print()
