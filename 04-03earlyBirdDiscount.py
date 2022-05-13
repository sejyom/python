# 영화 조조 할인 판정

from time import localtime
hour = localtime().tm_hour
minute = localtime().tm_min

if hour < 10:
    print('현 시각은 %d시 %d분 입니다. 할인 받으세요 !! '% (hour, minute))
else:
    print('현 시각은 %d시 %d분 입니다. 할인 안 돼요 !! '% (hour, minute))
    
