n=int(input())

a=list(map(int,input().split()))
b=list(map(int,input().split()))
if sum(a)<sum(b):
    print(sum(b)-sum(a))
else:print(0)