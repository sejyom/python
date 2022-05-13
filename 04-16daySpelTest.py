# 월, 화, 수 중 영어 철자 하나 검사

days = ['monday', 'tuesday', 'wednsday']

while True:
    user = input('월? 화? 수? ')
    if user not in days:  
        print('땡!!!')
        continue
    print('%s 굿굿' % user)
    break
print('종료'.center(15, '-'))
