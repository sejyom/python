#영어 요일 단어로 구성된 튜플 만들기

day1=('monday', 'tuesday', 'wednesday')
day2=('thursday', 'friday', 'saturday')
day3=('sunday',)
day=day1+day2+day3

print(type(day))
print(day)

day=day1+day2+day3*3
print(day)
