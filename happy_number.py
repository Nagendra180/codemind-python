def sum(x):
    s=0
    while x>0:
        r=x%10
        s=s+r**2
        x=x//10
    if s>9:
        s=sum(s)
    return s
x=int(input())
print(sum(x)==1)