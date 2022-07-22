x=int(input())
l=list(map(int,input().split()))
a=0
b=0
for i in range(x):
    if i%2==0:
        a=a+l[i]
    else:
        b=b+l[i]
if a-b==0:
    print('YES')
else:
    print('NO')
        