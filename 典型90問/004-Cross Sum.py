H,W=map(int,input().split())
A=[]
for _ in range(H):
    a=list(map(int,input().split()))
    A.append(a)

B=[[0 for _ in range(W)] for _ in range(H)]

tate=[0 for _ in range(W)]
yoko=[0 for _ in range(H)]

for i in range(H):
    for j in range(W):
        yoko[i]+=A[i][j]
        tate[j]+=A[i][j]

for i in range(H):
    for j in range(W):
        B[i][j]=yoko[i]+tate[j]-A[i][j]

for i in range(H):
    print(*B[i])