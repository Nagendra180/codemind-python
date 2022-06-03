n=input().lower()
c=0
for i in n:
    if n.count(i)==1:
        c=c+1
print(len(n)==c)