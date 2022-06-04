n=input().lower()
m=input().lower()
a=[i for i in n if i not in m and i!=' ' and i.isalpha()]
b=[i for i in m if i not in n and i!=' ' and i.isalpha()]
a.extend(b)
c=set(a)
print(len(c))