a,b,c=map(int,input().split())
l=list(map(int,input().split()))
while b!=0:
    l.insert(0,l[-1])
    l.pop()
    b=b-1
for i in range(c):
    x=int(input())
    print(l[x])
    