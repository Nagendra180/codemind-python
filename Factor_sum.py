def f(a):
    s=0
    for i in range(1,a+1):
        if a%i==0:
            s=s+i
    return s
l=list(map(int,input().split(",")))
c=[]
for i in l:
    k=f(i)
    if k in l:
        c.append(i)
c=sorted(c)
if len(c)==0:
    print(-1)
else:print(*c)