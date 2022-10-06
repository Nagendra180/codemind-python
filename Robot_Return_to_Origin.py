s=input()
a=0
for i in s:
    if i=="R":
        a=a+1
    elif i=="U":
        a=a+1
    elif i=="D":
        a=a-1
    else:
        a=a-1
print(a==0)