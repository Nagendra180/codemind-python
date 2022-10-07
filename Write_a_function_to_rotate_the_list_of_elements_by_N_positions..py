n=int(input())
l=list(map(int,input().split()))
m=int(input())
while m!=0:
    l.insert(0,l[-1])
    l.pop()
    m=m-1
print(*l)