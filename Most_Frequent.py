n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
a=0
b=0
for k,v in d.items():
    if v>a:
        a=v
        b=k
print(b)
    