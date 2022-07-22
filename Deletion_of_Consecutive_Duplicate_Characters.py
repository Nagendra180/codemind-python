x=int(input())
for i in range(x):
    n=input()
    a=[]
    for i in range(len(n)-1):
        if n[i]==n[i+1]:
            a.append(n[i])
    print(len(a))
        