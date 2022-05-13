#키워드 형태 가변 인자 함수 구현

def mykeyprint(**kwargs):
    for key in kwargs:
        print('{}: {}'.format(key, kwargs[key]), end=' ')
    print()


mykeyprint(여자친구=6, 마마무=4)
mykeyprint(엑소=9, 트와이스=9, 블랙핑크=4, 방탄소년단=7)

coffeeprice = {}
coffeeprice['에스프레소']=2500
coffeeprice['아메리카노']=2800
coffeeprice['카페라떼']=3200

mycar={"brand": "현대", "model": "제네시스", "year": 2016}
mykeyprint(**coffeeprice)
mykeyprint(**mycar)
