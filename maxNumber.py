n = int(input())

a=list() 
for i in range(n):
    b=int(input())
    a.append(b)

print(max(a))
print(a.index(max(a))+1)
