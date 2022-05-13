# 실수의 모든 자릿수 더하기

value = input('실수를 입력하세요(세자리.두자리 조합) >> ')
num = value.replace('.', '')
sum=0

sum+=(int(num[0]))
sum+=(int(num[1]))
sum+=(int(num[2]))
sum+=(int(num[3]))
sum+=(int(num[4]))

print('입력값:', value)
print('모든 자릿수 합:',sum)
