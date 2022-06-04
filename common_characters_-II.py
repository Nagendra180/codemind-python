n=input().lower()
m=input().lower()
a=[]
for i in n:
    if i in m and i not in a and i!=' ':
        a.append(i)
print(len(a))
