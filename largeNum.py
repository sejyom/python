n = int(input()) #nę°ė ė ė
a=list(map(int, input().split()))
max=a[0]; min=a[0]

for i in a[1:]:
    if i>max: max=i
    elif i<min: min=i

print(min, max) 
