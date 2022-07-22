x=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(0,x,2):
    while l[i+1]>0:
        a.append(l[i])
        l[i+1]-=1
print(*a)