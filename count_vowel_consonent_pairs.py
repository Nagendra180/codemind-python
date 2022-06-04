n=input()
a='aeiouAEIOU'
c=0
for i in range(len(n)):
    if n[i] not in a and n[i]!=' ' and n[(len(n)-1)-i] in a:
        c=c+1
print(c)