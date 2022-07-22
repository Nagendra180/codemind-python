x=int(input())
l=list(map(int,input().split()))
a=set(l)
b=0
for i in a:
    c=l.count(i)//2
    b=b+c
print(b)
    