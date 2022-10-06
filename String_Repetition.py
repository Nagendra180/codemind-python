n=input()
m=int(input())
a=m%len(n)
s=0
if a!=0:
    for i in range(a):
        if n[i]=="a":
            s=s+1
l=m//len(n)
print(n.count("a")*l+s)