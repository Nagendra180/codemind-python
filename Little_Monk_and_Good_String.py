s=input()
a=0
r=0
for i in range(len(s)):
    if s[i]=="a":
        a=a+1
    elif s[i]=="e":
        a=a+1
    elif s[i]=="i":
        a=a+1
    elif s[i]=="u":
        a=a+1
    elif s[i]=="o":
        a=a+1
    else:
        a=0
    if a>r:
        r=a
print(r)
        