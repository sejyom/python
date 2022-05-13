#요일 문자열 원소로 구성된 집합 연산 수행

daysA={'월', '화', '수', '목'}
daysB=set(['수', '목', '금', '토', '일'])
weekends=set(('토', '일'))

#alldays=daysA|daysB
alldays=daysA.union(daysB)
print(alldays)

#workdays=(daysA|daysB)-weekends #alldays-=weekends
workdays=alldays.difference(weekends)
print(workdays)

#print(daysA&daysB)
print(daysA.intersection(daysB))
print(daysA.symmetric_difference(daysB))
