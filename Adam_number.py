def rev(x):
    s=0
    while x>0:
        r=x%10
        s=s*10+r
        x=x//10
    return s
x=int(input())
b=(rev(x))**2
print(x*x==rev(b))

    