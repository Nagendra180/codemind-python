n=input()
s=n[-2]+n[-1]
n=n.split(":")
a=int(n[0])
b=n[1][0]+n[1][1]
if a==12 and s=="AM":
    print("00:00")
elif a!=12 and s=="PM":
    print("{}:{}".format(12+a,b))
elif s=="PM" and a==12:
    print("{}:{}".format(a,b))
else:
    print("{}:{}".format(n[0],b))