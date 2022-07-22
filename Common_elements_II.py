a,b=map(int,input().split())
n=list(map(int,input().split()))
m=list(map(int,input().split()))
x=[]
for i in n:
    if i not in m:
        x.append(i)
for i in m:
    if i not in n:
        x.append(i)
print(*x)