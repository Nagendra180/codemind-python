n=int(input())
for i in range(n):
    m=int(input())
    l=list(map(int,input().split()))
    c=[]
    a=m//2
    while a!=0:
        c.append(max(l))
        c.append(min(l))
        l.remove(max(l))
        l.remove(min(l))
        a=a-1
    if len(l)%2==0:
        print(*c)
    else:
        c.append(l[-1])
        print(*c)
        