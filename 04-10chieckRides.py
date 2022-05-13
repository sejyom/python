# 어린이를 위한 놀이 기구 탑승 검사


height = 0
lcv = 0

while lcv <= 4:
    height = float(input(('키는? ')))
    if height < 130:
        lcv+=1
        print('%d명째 탑승' % lcv)
    else:
        print('키가 너무 커요')
    if lcv == 4:
        print('끝!!')
        break



        
