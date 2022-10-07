s=int(input())
l=list(map(int,input().split()))
q=list(map(int,input().split()))
a=[]
for i in range(s):
    a.append(l[i]+q[i])
print(*a)