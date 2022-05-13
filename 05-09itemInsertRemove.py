#학용품 리스트의 항목 삽입과 삭제

item=['pencil', 'pen']
print(item)

#연필 1개와 볼펜 세 자루 삽입
item.insert(1, 2)
item.insert(3, 3)

#맨 뒤에 지우개, 1개 삽입
item.append('eraser')
item.append(1)
print(item)

#연필 두 자루 삭제
print(item.pop(1)) #인덱스 1에 저장된 값 반환과 동시에 삭제
item.remove('pencil')
del item[2:]

print(item)
