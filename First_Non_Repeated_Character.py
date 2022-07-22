x=int(input())
for i in range(x):
    n=int(input())
    m=input()
    for i in m:
        s=0
        if m.count(i)==1:
            print(i)
            s=1
            break
    if s==0:
        print(-1)