from random import randint
li = []
for i in range(10):
    li.append(randint(1, 99))

print('리스트', li)
print('정렬 리스트', sorted(li))
print('역순 리스트', sorted(li, reverse=True))
            


