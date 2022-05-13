# 위치 인자와 키워드 형태 가변 인자 함수 구현

def sumvalue(value, **kwargs):
    hap = value
    for key in kwargs:
        hap+=kwargs[key]
    return hap

coffeeprice ={'에스프레소': 2000, '아메리카노': 2800, '카페라떼': 3200}
print(sumvalue(1000, **coffeeprice))
print(sumvalue(value=2000, **coffeeprice))
print(sumvalue(**coffeeprice, value = 2000))

