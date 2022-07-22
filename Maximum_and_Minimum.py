x=int(input())
l=list(map(int,input().split()))
s=set(l)
a=[]
c=0
for i in s:
    if l.count(i)==i:
        c=1
        a.append(i)
if c==1:
    print(min(a),max(a))
else:
    print(-1)