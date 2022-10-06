n=input()
s=0
r=0
for i in range(len(n)-1):
    if n[i]==n[i+1]:s=s+1
    else:s=0
    if s>r:
        r=s
print(r+1)
