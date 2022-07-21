def pri(x):
    if x==1:
        return 0
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return 0
    else:
        return 1
x=int(input())
s=0
for i in range(1,x+1):
    if x%i==0:
        if i!=(x//i) and pri(i)==1 and pri(x//i)==1:
            s=1
            break
if s==1:
    print(i,x//i)
else:
    print(-1)
            
        