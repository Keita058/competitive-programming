n,m,l=map(int,input().split())
A=[]
B=[]
for _ in range(n):
    a=list(map(int,input().split()))
    A.append(a)
for _ in range(m):
    b=list(map(int,input().split()))
    B.append(b)

C=[[0 for _ in range(l)] for _ in range(n)]
for i in range(n):
    for j in range(l):
        for k in range(m):
            C[i][j]+=A[i][k]*B[k][j]

for i in range(n):
    print(*C[i])