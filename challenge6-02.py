#주식 가격을 딕셔너리로 만들어 표준입력으로 검색해 가격을 출력하는 프로그램 작성
#검색을 계속하며, 주식 이름이 없으면 종료

name=['삼성에스디에스', '삼성전자', '엔씨소프트', '핸디소프트', '골프존' ,'기아']
price=[242000, 47000, 52600, 5120, 215000, 56300]
company=dict((zip(name, price)))
print(company)

while True:
    user = input('주식 이름? ')
    if user in company:
        print('{}: {}'.format(user, company[user]))
    else:
        print('주식 이름이 없습니다.')
        break
   
                    
    
        
