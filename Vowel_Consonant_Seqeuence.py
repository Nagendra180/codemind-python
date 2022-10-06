a=input()
l=list(a)
s=""
for i in range(len(l)):
    if l[i]=="a" or l[i]=="e" or l[i]=="i" or l[i]=="o" or l[i]=="u":
        l[i]="V"
    else:
        l[i]="C"
for i in range(len(l)-1):
    if l[i]!=l[i+1]:
        s=s+l[i]
print(s+l[-1])
        