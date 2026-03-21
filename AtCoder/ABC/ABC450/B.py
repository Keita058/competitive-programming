N=int(input())
A=[[0 for i in range(N)] for _ in range(N)]

for i in range(N-1):
    L=list(map(int,input().split()))
    for j in range(len(L)):
        A[i][i+j+1]=L[j]
flag=False
for a in range(N-2):
    for b in range(a+1, N-1):
        for c in range(b+1, N):
            cost1=A[a][c]
            cost2=A[a][b]+A[b][c]
            if cost2<cost1:
                flag=True

print('Yes' if flag else 'No')
