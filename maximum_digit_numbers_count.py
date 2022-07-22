x=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    c.append(len(str(i)))
for i in l:
    if len(str(i))==max(c):
        print(i,end=' ')