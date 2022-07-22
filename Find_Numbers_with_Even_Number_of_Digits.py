x=int(input())
l=list(map(int,input().split()))
b=[]
for i in l:
    a=str(i)
    if (len(a))%2==0:
        b.append(a)
print(len(b))