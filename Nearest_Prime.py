def p(x):
    if x==1:
        return 0
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return 0
    else:
        return 1
def np(x):
    while p(x)==0:
        x=x+1
    return x
def pp(x):
    while p(x)==0:
        x=x-1
    return x
for i in range(int(input())):
    x=int(input())
    a=np(x)
    b=pp(x)
    if x-b<=a-x:
        print(b)
    else:
        print(a)