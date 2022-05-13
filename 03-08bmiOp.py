# BMI 계산기
# 키 단위는 cm

height = float(input('키를 cm 단위로 입력하세요 >> '))
weight = float(input('체중을 입력하세요 >> '))

bmi = weight / ((height/100)**2)


print('height: ', height, 'cm', '/ weight: ', weight, 'kg', '/ BMI: ', bmi)

print('고도비만: ', bmi >= 40)
print('중등도 비만: {}'.format(35 <= bmi < 40))
print('비만: {}'.format(30 <= bmi < 35))
print('과체중: {}'.format(25 <= bmi < 30))
print('정상: {}'.format(18.5 <= bmi < 25))
print('저체중: {}'.format(bmi < 18.5))
