from collections import deque

def dfs(v):
    global ans
    if A[v]<minA[-1]:
        minA.append(A[v])
        maxA.append(A[v])
    elif A[v]>maxA[-1]:
        maxA.append(A[v])
        minA.append(A[v])
    else:
        minA.append(minA[-1])
        maxA.append(maxA[-1])
    print(minA,maxA)
    
    ans=max(ans,maxA[-1]-minA[-1])
    for u in G[v]:
        if visited[u]:
            continue
        visited[u]=True
        dfs(u)
        minA.pop()
        maxA.pop()

N,M=map(int,input().split())
A=list(map(int,input().split()))
XY=[list(map(int,input().split())) for _ in range(M)]

G=[[] for _ in range(N)]
for i in range(M):
    X,Y=XY[i]
    G[X-1].append(Y-1)

ans=-float('inf')
visited=[False]*N
minA=[float('inf')]
maxA=[0]
for i in range(N):
    if visited[i]:
        continue
    visited[i]=True
    dfs(i)
    minA.pop()
    maxA.pop()
print(ans)