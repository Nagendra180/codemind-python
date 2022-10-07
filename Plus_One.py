n=int(input())
l=list(map(int,input().split()))
s=""
for i in l:
    s=s+str(i)
a=int(s)+1
a=str(a)
c=[]
for i in a:
    c.append(int(i))
print(*c)
    
    
    