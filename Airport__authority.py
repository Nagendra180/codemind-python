n=int(input())
a=[]
for i in range(n):
    k=int(input())
    a.append(k)
m=int(input())
s=0
for i in a:
    if i<=m:
        s=s+1
    else:s=s+2
print(s)