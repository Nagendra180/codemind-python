x=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in range(x//2):
    a.append(l[i])
for i in range(x//2,x):
    b.append(l[i])
b.reverse()
print(*b+a)
    