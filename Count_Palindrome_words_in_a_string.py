lst=list(map(str,input().split()))
c=0
for i in lst:
    a=i.lower()
    if a[::-1]==a:
        c=c+1
print(c)