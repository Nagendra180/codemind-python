def fac(x):
    fac=1
    for i in range(1,x+1):
        fac=fac*i
    return fac
x=int(input())
a=x
s=0
while x>0:
    r=x%10
    s=s+fac(r)
    x=x//10
if s==a:
    print('The number',a,'is a strong number')
else:
    print('The number',a,'is not a strong number')