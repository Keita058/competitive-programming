r,c=map(int,input().split())
A=[]
for _ in range(r):
    a=list(map(int,input().split()))
    x=sum(a)
    a.append(x)
    A.append(a)

al=[]
for j in range(c+1):
    t=0
    for i in range(r):
        t+=A[i][j]
    al.append(t)

A.append(al)
for i in range(r+1):
    print(*A[i])