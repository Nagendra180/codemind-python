def a(x):
    n=x
    c=0
    while x!=0:
        r=x%10
        c=c+r
        x=x//10
    return c
n=int(input())
if a(n*n)==n:
    print("Neon Number")
else:print("Not Neon Number")