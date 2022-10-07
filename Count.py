n=int(input())
l=list(map(int,input().split()))
a=[i for i in l if i%2==0 ]
print(len(a),len(l)-len(a))
