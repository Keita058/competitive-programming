n,m=map(int,input().split())
A=[]
for _ in range(n):
    a=list(map(int,input().split()))
    A.append(a)
b=[]
for i in range(m):
    x=int(input())
    b.append(x)

for i in range(n):
    ans=0
    for j in range(m):
        ans+=A[i][j]*b[j]
    print(ans)
