n=input().lower()
b=[]
a=set(n)
for i in a:
    if n.count(i)==1 and i!=' ':
        b.append(i)
print(''.join(sorted(b)))