n=input()
n=n.split(":")
a=int(n[0])
b=a%12
s='0'
if a==0:
    print("12:{} AM".format(n[1]))
elif a>12 and b<10:
    s=s+str(b)
    print("{}:{} PM".format(s,n[1]))
elif a<12 and b<10:
    s=s+str(b)
    print("{}:{} AM".format(s,n[1]))
elif a<12 and b>9:
    print("{}:{} AM".format(b,n[1]))
elif a>12 and b>9:
    print("{}:{} PM".format(b,n[1]))
else:
    print("12:{} PM".format(n[1]))