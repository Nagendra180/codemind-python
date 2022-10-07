n=int(input())
for i in range(n):
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    q=list(map(int,input().split()))
    a=l+q
    print(*(sorted(a)))
