n=int(input())
m=int(input())
l=[i for i in range(n,m+1)]
b=len(l)
j=1
s=0
while j<=b:
    for i in range(b):
        if i+j<=b and sum(l[i:j+i])%2!=0:
            s=s+1
    j=j+1
print(s)