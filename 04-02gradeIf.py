# 평균 평점 3.8 이상이면 장학금 지급 대상자

grade = float(input('1학기 평균 평점은? >> '))

if grade >= 3.8:
    print('장학금 지급 대상자')
print('당신의 1학기 평균 평점은 %.2f입니다.'%(grade))
