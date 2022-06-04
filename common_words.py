n=list(map(str,input().split()))
m=list(map(str,input().split()))
a=[]
for e in m:
    i=e.lower()
    if i in n and i not in a:
        a.append(i)
for e in n:
    i=e.lower()
    if i in m and i not in a:
        a.append(i)
print(*a)