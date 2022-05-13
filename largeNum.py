n = int(input()) #n개의 정수
a=list(map(int, input().split()))
max=a[0]; min=a[0]

for i in a[1:]:
    if i>max: max=i
    elif i<min: min=i

print(min, max) 
