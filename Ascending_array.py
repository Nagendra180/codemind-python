x=int(input())
l=list(map(int,input().split()))
s=0
for i in range(x-1):
    if l[i]<(l[i+1]):
        s=s+1
if s==len(l)-1:
    print('yes')
else:
    print('no')