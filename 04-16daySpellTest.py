# 월, 화, 수 중 영어 철자 하나 검사

days = ['monday', 'tuesday', 'wednsday']

while True:
    user = input('월? 화? 수?')
    if user in days:
        print('굿굿')
        break
    else:
        print('땡!!!')
        continue

