a=input()
b=[]
for i in a:
    if i!=' ':
        b.append(i)
c=min(b)
d=max(b)
print(c,b.count(c),d,b.count(d))