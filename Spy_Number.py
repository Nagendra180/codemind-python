n=int(input())
s=str(n)
m=list(s)
x=1
y=0
for i in m:
    x=x*int(i)
    y=y+int(i)
if x==y:
    print("Spy Number")
else:print("Not Spy Number")