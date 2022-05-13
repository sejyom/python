# 키워드 global로 전역 변수를 명시적으로 지정

def addone():
    global i
    print('전역 변수 i 읽기, i+1: ', i+1)
    i+=1

i=20
print('i= ', i)
addone()
print('i= ', i)
