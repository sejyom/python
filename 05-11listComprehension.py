#간단한 리스트 컴프리헨션

#for-1
a =[]
for i in range(10):
    a.append(i)
print(a)

#comprehension-1
b=[i for i in range(10)]
print(b)

#for-2
c=[]
for i in range(10):
    if i%2==1:
        c.append(i**2)
print(c)

#comprehension-2
d=[i**2 for i in range(10) if i%2==1]
print(d)

