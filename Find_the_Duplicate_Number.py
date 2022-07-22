x=int(input())
l=list(map(int,input().split()))
b=set(l)
a=[]
for i in b:
    if l.count(i)>1:
        a.append(i)
print(*a)