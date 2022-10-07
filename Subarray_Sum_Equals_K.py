n,m=map(int,input().split())
l=list(map(int,input().split()))
j=1
s=0

while j<=n:
    for i in range(n):
        if i+j<=n and sum(l[i:j+i])==m:
            s=s+1
    j=j+1
print(s)