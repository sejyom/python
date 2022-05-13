# 미세먼지 예보
pm = float(input('미세먼지 농도 입력 >> '))

if 151 <= pm:
    print('concentration: {:.2f}, grade: {}'.format(pm, '매우 나쁨'))
elif 81 <= pm:
    print('concentration: {:.2f}, grade: {}'.format(pm, '나쁨'))
elif 31 <= pm:
    print('concentration: {:.2f}, grade: {}'.format(pm, '보통'))
else:
    print('concentration: {:.2f}, grade: {}'.format(pm, '좋음'))
    
    
