from itertools import permutations

N=int(input())
A=[list(map(int,input().split())) for _ in range(N)]

discord=[set() for _ in range(N)]
M=int(input())
for _ in range(M):
    X,Y=map(int,input().split())
    discord[X-1].add(Y-1)
    discord[Y-1].add(X-1)

L=[i for i in range(N)]
L=list(permutations(L))

ans=float('inf')
for x in L:
    cnt=0
    flag=True
    for i in range(N):
        if i>0:
            if x[i] in discord[x[i-1]]:
                flag=False
                break
        cnt+=A[x[i]][i]
    if flag:
        ans=min(ans,cnt)
print(ans if ans!=float('inf') else -1)