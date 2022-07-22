n=input()
a=set(n)
b=[]
c=0
for i in a:
    b.append(n.count(i))
for i in a:
    if n.count(i)!=max(b):
        c=c+1
if c>1:
    print('Not Valid')
else:
    print('Valid String')