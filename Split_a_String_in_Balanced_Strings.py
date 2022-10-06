s=input()
a=0
b=0
for i in s:
    if i=="R":
        a=a+1
    else:
        a=a-1
    if a==0:
        b=b+1
print(b)