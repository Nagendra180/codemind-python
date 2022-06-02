def gcd(x,y):
    while(y):
        x,y=y,x%y
    return x
n=int(input())
lst=list(map(int,input().split()))
n1=lst[0]
n2=lst[1]
gcd1=gcd(n1,n2)
for i in range(2,n):
    gcd1=gcd(gcd1,lst[i])
print(gcd1)