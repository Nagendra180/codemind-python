l=list(map(int,input().split()))
q=list(map(int,input().split()))
a=0
b=0
for i in range(len(l)):
    if l[i]>q[i]:
        a=a+1
    elif l[i]==q[i]:
        pass
    else:
        b=b+1
print(a,b)